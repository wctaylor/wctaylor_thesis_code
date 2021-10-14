import os

import numpy as np
import matplotlib.ticker
import matplotlib.pyplot as plt

import thesis.xs
import thesis.config
import thesis.isotopes

use_tex = True
if (use_tex):
    thesis.config.use_tex()
else:
    thesis.config.use_inline()
config_file_path = "/users/wctaylor/wctaylor_thesis_code/config/config.json"
thesis.config.config_env(config_file_path)

figure_dir = os.environ["FIGURE_DIR"]
figure_dir = f"{figure_dir}/chapter4/cross_sections"
cross_section_dir = os.environ["CROSS_SECTION_DATA_DIR"]
NUM_BINS = 70
NUM_INTERPOLATION_BINS=1000*NUM_BINS
LOWER_BOUND_X = 1e-2
UPPER_BOUND_X = 2e7
LOWER_BOUND_Y = 1e-6

for isotope, isotope_data in thesis.isotopes.ISOTOPES.items():  
    if (len(isotope_data["parents"]) == 0):
        continue    
    fig, axis = plt.subplots(figsize=(6,6))
    do_plot = False
    lower_bound_y = None
    
    for pair in isotope_data["parents"]:
        for parent, process in pair.items():
            production_data = thesis.isotopes.ISOTOPES[parent]["processes"]
            production_data = production_data[process]["children"][isotope]
            if ("cross_sections" in production_data):
                cross_sections = production_data["cross_sections"]
                for library, filename in cross_sections.items():                     if (filename is None):
                        continue
                    else:
                        if (library == "ENDF/B-VII.1"):
                            lib = "endf"
                        if (library == "NGATLAS"):
                            lib = "ngatlas"
                        data_path = f'{cross_section_dir}/{lib}'
                        filepath = f"{data_path}/{filename}"
                        cross_section_data = thesis.xs.get_cross_section_data(
                            library, 
                            filepath
                        )

                        do_plot = True
                        cut = (cross_section_data["cross_section_b"] != 0)
                        if (np.min(cross_section_data["cross_section_b"][cut]) 
                            < LOWER_BOUND_Y):
                                lower_bound_y = LOWER_BOUND_Y
                        avg_data = thesis.xs.get_averaged_cross_section_data(
                            cross_section_data,
                            bin_range=(LOWER_BOUND_X, 
                                       UPPER_BOUND_X), 
                            num_bins=NUM_BINS,
                            num_interpolation_bins=NUM_INTERPOLATION_BINS
                        )
                        cut = (avg_data["cross_section_b"] != 0)
                        if (np.min(avg_data["cross_section_b"][cut]) 
                            < LOWER_BOUND_Y):
                                lower_bound_y = LOWER_BOUND_Y
                        if (process == "nCapture"):
                            reaction = "$(n, \gamma)$"
                            parent_label = thesis.isotopes.ISOTOPES[parent]
                            parent_label = parent_label["label"]
                            isotope_label = thesis.isotopes.ISOTOPES[isotope]
                            isotope_label = isotope_label["label"]
                        elif (process == "neutronInelastic"):
                            reaction = "$(n, n')$"
                            parent_label = thesis.isotopes.ISOTOPES[parent]
                            parent_label = parent_label["label"]
                            isotope_label = parent_label
                        label = f"{parent_label}{reaction}{isotope_label}"
                        label = f"{label}  {library}"
                        axis.plot(cross_section_data["energy_eV"], 
                                  cross_section_data["cross_section_b"],
                                  label=label)
                        axis.step(avg_data["energy_eV"], 
                                 avg_data["cross_section_b"], 
                                 where="post",
                                 linestyle="--",
                                 label=f"Averaged {label}")
    if (do_plot):
        axis.set_xlabel("Energy [eV]")
        axis.set_ylabel("Cross Section [b]")
        axis.set_xscale("log")
        axis.set_yscale("log")
        axis.set_xlim([LOWER_BOUND_X, UPPER_BOUND_X])
        axis.set_ylim(bottom=lower_bound_y)
        axis.legend(loc='lower left')
        axis.set_title(f"{isotope_data['label']} Production Cross Sections")
        axis.xaxis.set_major_locator(matplotlib.ticker.LogLocator(numticks=9))
        axis.xaxis.set_minor_locator(matplotlib.ticker.LogLocator(subs='all', 
                                                                  numticks=90))
        axis.yaxis.set_major_locator(matplotlib.ticker.LogLocator(numticks=9))
        axis.yaxis.set_minor_locator(matplotlib.ticker.LogLocator(subs='all', 
                                                                  numticks=90))
        fig.savefig(f"{figure_dir}/{isotope}_production.pdf",
                    dpi=150)
        plt.show()
    else:
        plt.close(fig)