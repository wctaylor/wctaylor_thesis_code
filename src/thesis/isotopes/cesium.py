ISOTOPES = \
{
    "Cs133": \
    {
        "label": "$^{133}$Cs",
        "parents": [{"Xe133": "RadioactiveDecay"}],
        "processes": {},
    },
    "Cs135": \
    {
        "label": "$^{135}$Cs",
        "parents": \
        [
            {"Xe135": "RadioactiveDecay"},
        ],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Ba135": \
                    {
                        "half_life_days": 2.3e6*365,
                        "mode": "$\beta^{-}$",
                        "spectrum": "xebox_50k_cs135_decay_444282737_flat.root",
                    },
                },
            },
        },
    },
    "Cs137": \
    {
        "label": "$^{137}$Cs",
        "parents": \
        [
            {"Xe137": "RadioactiveDecay"},
        ],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Ba137": \
                    {
                        "half_life_days": 30.07*365,
                        "mode": "$\beta^{-}$",
                        "spectrum": "xebox_50k_cs137_decay_133316960_flat.root",
                    },
                },
            },
        },
    },
}