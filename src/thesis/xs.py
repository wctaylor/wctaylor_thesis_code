import numpy as np
import scipy.interpolate

def get_endf_cross_section(filepath):
    """
    Get cross section vs energy points from ENDF/B-VII.1 data files
    
    Parameters
    ----------
    filepath: str
        Path to the cross section data file
        
    Returns
    -------
    cross_section_data: dict
        A dict containing the cross section vs energy points from the file
    """
    with open(filepath, "r") as data_file:
        data = data_file.readlines()
    temp     = data[0].split()
    library  = temp[1].strip()
    temp     = temp[0].split("(")
    iso      = temp[0].split("-")
    isotope  = f"$^{{{iso[2]}}}${iso[1]}"
    reaction = f"({temp[1]}"
    if (reaction == "(n,&gamma;)"):
        reaction = "$(n, \gamma)$"
            
    energy_eV       = np.zeros(len(data[1:]))
    cross_section_b = np.zeros(len(data[1:]))
    for i in range(1, len(data)):
        temp = data[i].split(",")    
        energy_eV[i-1]       = float(temp[0])
        cross_section_b[i-1] = float(temp[1])
    
    cross_section_data = \
    {
        "energy_eV": energy_eV,
        "cross_section_b": cross_section_b
    }
    
    return cross_section_data

def get_ngatlas_cross_section(filepath):
    """
    Get cross section vs energy points from NGATLAS data files
    
    Parameters
    ----------
    filepath: str
        Path to the cross section data file
        
    Returns
    -------
    cross_section_data: dict
        A dict containing the cross section vs energy points from the file
    """
    NAME_BEGIN = "#name:"
    DATA_BEGIN = "#data..."
    DATA_END = "//"
    
    with open(filepath, "r") as data_file:
        data = data_file.readlines()
    
    data_found = False
    data_start_index = -1
    data_end_index = -1
    for i in range(len(data)):
        if (data[i].startswith(NAME_BEGIN)):
            reaction = data[i].split()[1].split("-")[1]
            if (reaction == "102" or reaction == "402"):
                data_found = True
        if (data_found):
            if (data[i].startswith(DATA_BEGIN)):
                axes = data[i + 1]
                units = data[i + 2]
                data_start_index = i + 3
            if (data[i].startswith(DATA_END)):
                data_end_index = i
    energy_eV       = np.zeros(len(data[data_start_index:data_end_index]))
    cross_section_b = np.zeros(len(data[data_start_index:data_end_index]))
    for i in range(data_start_index, data_end_index):
        temp = data[i].split()
        energy_eV[i - data_start_index]       = float(temp[0])
        cross_section_b[i - data_start_index] = float(temp[1])
    
    cross_section_data = \
    {
        "energy_eV": energy_eV*1e6, # data provided in MeV
        "cross_section_b": cross_section_b
    }
    
    return cross_section_data

def get_cross_section_data(library, filepath):
    """
    Get cross section vs energy points for an isotope and reaction
    
    Parameters
    ----------
    library: str
        Which cross section library is being used
    filepath: str
        Path to the cross section data file
        
    Returns
    -------
    cross_section_data: dict
        A dict containing the cross section vs energy points for
        the input reaction and isotope
    """    
    if (library == "ENDF/B-VII.1"):
        data = get_endf_cross_section(filepath)
    elif (library == "NGATLAS"):
        data = get_ngatlas_cross_section(filepath)
    else:
        raise ValueError(f"{library} is not a supported library.")
    
    return data
    
def interpolate_cross_section_data(cross_section_data, kind="linear"):
    """
    Generate additional data points within the provided cross section data
    via interpolation. 
    Useful for averaging
    
    Parameters
    ----------
    cross_section_data: dict
         A dict containing the cross section vs energy points for
    the input reaction and isotope
    """
    energy_eV = cross_section_data["energy_eV"]
    cross_section_b = cross_section_data["cross_section_b"]
    
    values, indices, counts = np.unique(energy_eV, 
                                        return_index=True, 
                                        return_counts=True)
    duplicates = values[counts > 1]
    
    new_E = energy_eV[indices]
    new_xs = cross_section_b[indices]
    for duplicate in duplicates:
        cut_dupe = (energy_eV == duplicate)
        avg_xs = np.sum(cross_section_b[cut_dupe])/len(cross_section_b[cut_dupe])
        new_index = (new_E == duplicate)
        new_xs[new_index] = avg_xs
    interpolation = scipy.interpolate.interp1d(new_E,
                                               new_xs,
                                               kind=kind,
                                               fill_value="extrapolate")
    return interpolation

def get_averaged_cross_section_data(cross_section_data, bin_range=None,
                                    num_bins=100, num_interpolation_bins=1000):
    energy_eV       = cross_section_data["energy_eV"]
    cross_section_b = cross_section_data["cross_section_b"]
    
    if (bin_range is None):
        bin_range = [np.min(energy_eV), np.max(energy_eV)]
    bins  = np.logspace(np.log10(bin_range[0]), 
                        np.log10(bin_range[1]), 
                        num_bins)
    interpolation_bins = np.logspace(np.log10(bin_range[0]),
                                     np.log10(bin_range[1]),
                                     num_interpolation_bins)
    interpolation = interpolate_cross_section_data(cross_section_data)
    interpolated_cross_sections = interpolation(interpolation_bins)

    data = np.zeros_like(bins)
    for index in range(len(bins)):
        if (index == (len(bins)-1)):
            cut_energy = (interpolation_bins >= bins[index])
        else:
            cut_energy = (  (interpolation_bins >= bins[index]) 
                          * (interpolation_bins < bins[index+1])  )

        energies = interpolation_bins[cut_energy]
        if (len(energies) > 0):
            cross_sections = interpolated_cross_sections[cut_energy]
            avg = np.sum(cross_sections)/len(cross_sections)
            data[index] = avg
        else:
            continue

    avg_data = \
    {
        "energy_eV": bins,
        "cross_section_b": data
    }

    return avg_data