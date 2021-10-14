import os

from . import xenon
from . import iodine
from .. import config

config.config_env()
cs_data_dir = os.environ["CROSS_SECTION_DATA_DIR"]

ISOTOPES = {}
# for isotope, data in ti.ISOTOPES.items():
#     ISOTOPES.update({isotope:data})
for isotope, data in xenon.ISOTOPES.items():
    ISOTOPES.update({isotope:data})
for isotope, data in iodine.ISOTOPES.items():
    ISOTOPES.update({isotope:data})