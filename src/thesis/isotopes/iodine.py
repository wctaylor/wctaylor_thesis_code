import numpy as np

ISOTOPES = \
{
    "I125": \
    {
        "label": "$^{125}$I",
        "parents": [{"Xe125": "RadioactiveDecay"}],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Te125": \
                    {
                        "half_life_days": 59.408,
                        "mode": "EC",
                        "spectrum": "xebox_50k_i125_decay_192105495_flat.root",
                    },
                },
            },
        },
    },
    "I127": \
    {
        "label": "$^{127}$I",
        "parents": [{"Xe127": "RadioactiveDecay"}],
        "processes": {},
    },
}