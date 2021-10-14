import os
import json
import pathlib

import matplotlib as mpl

def config_env(config_file_path=None):
    if (config_file_path is None):
        config = \
        {
            "THESIS_ROOT": "/users/wctaylor/wctaylor_thesis_code",
            "LATEX_PATH": "/users/wctaylor/.local/texlive/bin/x86_64-linux",
            "CROSS_SECTION_DATA_DIR": "/users/wctaylor/data/cross_sections",
            "SPECTRUM_DATA_DIR": "/users/wctaylor/data/baccarat/wctaylor-5.2.7/XeBox/",
            "FIGURE_DIR": "/users/wctaylor/wctaylor_thesis_code/figures",
        }
    else:
        with open(config_file_path, "r") as config_file:
            config = json.load(config_file)
    for key, value in config.items():
        os.environ[key] = config[key]
    os.environ["TEXINPUTS"] = f"{config['THESIS_ROOT']}/config:"
    os.environ["MATPLOTLIBRC"] = f"{config['THESIS_ROOT']}/config/mpl_thesis_rc"
    os.environ["PATH"] = f"{config['LATEX_PATH']}:{os.environ['PATH']}"
        
def use_inline():
    # Based on code from
    # https://stackoverflow.com/questions/26413185/how-to-recover-matplotlib-defaults-after-setting-stylesheet
    DEFAULT_RC = \
    {
        "figure.dpi": 72.0, 
        "figure.edgecolor": (1, 1, 1, 0),
        "figure.facecolor": (1, 1, 1, 0),
        "figure.figsize": [6.0, 4.0],
        "figure.subplot.bottom": 0.125, 
        "interactive": True,
    }
    mpl.use("module://ipykernel.pylab.backend_inline")
    mpl.rcParams.update(mpl.rcParamsDefault)
    mpl.rcParams.update(DEFAULT_RC)

def use_tex():
    TEX_RC = \
    {
        "pgf.rcfonts": False,
        "pgf.texsystem": "lualatex",
        "pgf.preamble": "\n".join([r"\usepackage{amsmath}",
                                   r"\usepackage[T1]{fontenc}",
                                   r"\usepackage{gensymb}",
                                   r"\usepackage{lmodern}",
                                   r"\usepackage{siunitx}"]),
        "text.usetex": True,
        "font.family": "serif",
        "font.size": 12,
        "figure.figsize": (6, 6),  # size in inches
        "legend.fontsize": 12,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
    }
    use_inline()
    mpl.use("pgf")
    mpl.rcParams.update(TEX_RC)