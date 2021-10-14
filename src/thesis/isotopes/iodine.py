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
                        "spectrum": None,
                    },
                },
            },
        },
    },
}