ISOTOPES = \
{
    "Xe124": \
    {
        "label": "$^{124}$Xe",
        "parents": [],
        "processes": \
        {
            "nCapture": \
            {
                "children": \
                {
                    "Xe125": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe124_capture_xe125.txt",
                            "NGATLAS": "xe124_capture_xe125.txt",
                        },
                    },
                    "Xe125m": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": None,
                            "NGATLAS": "xe124_capture_xe125m.txt",
                        },
                    },
                },
            },
            "neutronInelastic": \
            {
                "children": \
                {
                    "Xe124": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": None,
                            "NGATLAS": None,
                        },
                    },
                },
            },
        },
    },
    "Xe125": \
    {
        "label": "$^{125}$Xe",
        "parents": \
        [
            {"Xe124": "nCapture"},
            {"Xe125m": "RadioactiveDecay"},
        ],
        "processes": \
        {
            "nCapture": \
            {
                "children": \
                {
                    "Xe126": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": None,
                            "NGATLAS": None,
                        },
                    },
                },
            },
            "neutronInelastic": \
            {
                "children": \
                {
                    "Xe125": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": None,
                            "NGATLAS": None,
                        },
                    },
                },
            },
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "I125": \
                    {
                        "half_life_days": 16.9/24,
                        "mode": "EC",
                        "spectrum": "xebox_50k_xe125_decay_1869635645_flat.root",
                    },
                },
            },
        },
    },
    "Xe125m": \
    {
        "label": "$^{125m}$Xe",
        "parents": [{"Xe124": "nCapture"}],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Xe125": \
                    {
                        "half_life_days": 57/3600/24,
                        "mode": "IT",
                        "spectrum": None,
                    },
                },
            },
        },
    },
    "Xe126": \
    {
        "label": "$^{126}$Xe",
        "parents": [],
        "processes": \
        {
            "nCapture": \
            {
                "children": \
                {
                    "Xe127": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe126_capture_xe127.txt",
                            "NGATLAS": "xe126_capture_xe127.txt",
                        },
                    },
                    "Xe127m": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": None,
                            "NGATLAS": "xe126_capture_xe127m.txt",
                        },
                    },
                },
            },
            "neutronInelastic": \
            {
                "children": \
                {
                    "Xe126": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe126_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                },
            },
        },
    },
    "Xe127": \
    {
        "label": "$^{127}$Xe",
        "parents": \
        [
            {"Xe126": "nCapture"},
            {"Xe127m": "RadioactiveDecay"},
        ],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "I127": \
                    {
                        "half_life_days": 36.4,
                        "mode": "EC",
                        "spectrum": "xebox_50k_xe127_decay_1951485865_flat.root",
                    },
                },
            },
        },
    },
    "Xe127m": \
    {
        "label": "$^{127m}$Xe",
        "parents": [{"Xe126": "nCapture"}],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Xe127": \
                    {
                        "half_life_days": 69.2/3600/24,
                        "mode": "IT",
                        "spectrum": None,
                    },
                },
            },
        },
    },
    "Xe128": \
    {
        "label": "$^{128}$Xe",
        "parents": [],
        "processes": \
        {
            "nCapture": \
            {
                "children": \
                {
                    "Xe129": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe128_capture_xe129.txt",
                            "NGATLAS": "xe128_capture_xe129.txt",
                        },
                    },
                    "Xe129m": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": None,
                            "NGATLAS": "xe128_capture_xe129m.txt",
                        },
                    },
                },
            },
            "neutronInelastic": \
            {
                "children": \
                {
                    "Xe128": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe128_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                },
            },
        },
    },
    "Xe129": \
    {
        "label": "$^{129}$Xe",
        "parents": \
        [
            {"Xe128": "nCapture"},
            {"Xe129m": "RadioactiveDecay"},
        ],
        "processes": \
        {
            "nCapture": \
            {
                "children": \
                {
                    "Xe130": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe129_capture_xe130.txt",
                            "NGATLAS": "xe129_capture_xe130.txt",
                        },
                    },
                },
            },
            "neutronInelastic": \
            {
                "children": \
                {
                    "Xe129": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe129_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                    "Xe129m": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe129_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                },
            },
        },
    },
    "Xe129m": \
    {
        "label": "$^{129m}$Xe",
        "parents": \
        [
            {"Xe128": "nCapture"}, 
            {"Xe129": "neutronInelastic"}
        ],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Xe129": \
                    {
                        "half_life_days": 8.88,
                        "mode": "IT",
                        "spectrum": "xebox_50k_xe129m_decay_1384900650_flat.root",
                    },
                },
            },
        },
    },
    "Xe130": \
    {
        "label": "$^{130}$Xe",
        "parents": [{"Xe129": "nCapture"}],
        "processes": \
        {
            "nCapture": \
            {
                "children": \
                {
                    "Xe131": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe130_capture_xe131.txt",
                            "NGATLAS": "xe130_capture_xe131.txt",
                        },
                    },
                    "Xe131m": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": None,
                            "NGATLAS": "xe130_capture_xe131m.txt",
                        },
                    },
                },
            },
            "neutronInelastic": \
            {
                "children": \
                {
                    "Xe130": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe130_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                },
            },
        },
    },
    "Xe131": \
    {
        "label": "$^{131}$Xe",
        "parents": \
        [
            {"Xe130": "nCapture"},
            {"Xe131m": "RadioactiveDecay"},
        ],
        "processes": \
        {
            "nCapture": \
            {
                "children": \
                {
                    "Xe132": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe131_capture_xe132.txt",
                            "NGATLAS": "xe131_capture_xe132.txt",
                        },
                    },
                    "Xe132m": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": None,
                            "NGATLAS": None,
                        },
                    },
                },
            },
            "neutronInelastic": \
            {
                "children": \
                {
                    "Xe131": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe131_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                    "Xe131m": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe131_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                },
            },
        },
    },
    "Xe131m": \
    {
        "label": "$^{131m}$Xe",
        "parents": \
        [
            {"Xe130": "nCapture"}, 
            {"Xe131": "neutronInelastic"}
        ],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Xe131": \
                    {
                        "half_life_days": 11.84,
                        "mode": "IT",
                        "spectrum": "xebox_50k_xe131m_decay_1437918812_flat.root",
                    },
                },
            },
        },
    },
    "Xe132": \
    {
        "label": "$^{132}$Xe",
        "parents": \
        [
            {"Xe131": "nCapture"},
            {"Xe132m": "RadioactiveDecay"},
        ],
        "processes": \
        {
            "nCapture": \
            {
                "children": \
                {
                    "Xe133": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe132_capture_xe133.txt",
                            "NGATLAS": "xe132_capture_xe133.txt",
                        },
                    },
                    "Xe133m": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": None,
                            "NGATLAS": "xe132_capture_xe133m.txt",
                        },
                    },
                },
            },
            "neutronInelastic": \
            {
                "children": \
                {
                    "Xe132": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe132_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                    "Xe132m": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe132_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                },
            },
        },
    },
    "Xe132m": \
    {
        "label": "$^{132m}$Xe",
        "parents": \
        [
            {"Xe131": "nCapture"}, 
            {"Xe132": "neutronInelastic"}
        ],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Xe132": \
                    {
                        "half_life_days": 8.39/1000/3600/24,
                        "mode": "IT",
                        "spectrum": None,
                    },
                },
            },
        },
    },
    "Xe133": \
    {
        "label": "$^{133}$Xe",
        "parents": \
        [
            {"Xe132": "nCapture"},
            {"Xe133m": "RadioactiveDecay"},
        ],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Cs133": \
                    {
                        "half_life_days": 5.243,
                        "mode": "$\beta^{-}$",
                        "spectrum": "xebox_50k_xe133_decay_1313591320_flat.root",
                    },
                },
            },
            "neutronInelastic": \
            {
                "children": \
                {
                    "Xe133": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe133_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                    "Xe133m": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe133_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                },
            },
        },
    },
    "Xe133m": \
    {
        "label": "$^{133m}$Xe",
        "parents": \
        [
            {"Xe132": "nCapture"},
            {"Xe133": "neutronInelastic"},
        ],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Xe133": \
                    {
                        "half_life_days": 2.19,
                        "mode": "IT",
                        "spectrum": None,
                    },
                },
            },
        },
    },
    "Xe134": \
    {
        "label": "$^{134}$Xe",
        "parents": [{"Xe134m": "RadioactiveDecay"}],
        "processes": \
        {
            "nCapture": \
            {
                "children": \
                {
                    "Xe135": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe134_capture_xe135.txt",
                            "NGATLAS": "xe134_capture_xe135.txt",
                        },
                    },
                    "Xe135m": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": None,
                            "NGATLAS": "xe134_capture_xe135m.txt",
                        },
                    },
                },
            },
            "neutronInelastic": \
            {
                "children": \
                {
                    "Xe134": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe134_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                    "Xe134m": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe134_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                },
            },
        },
    },
    "Xe134m": \
    {
        "label": "$^{134m}$Xe",
        "parents": [{"Xe134": "neutronInelastic"}],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Xe134": \
                    {
                        "half_life_days": 290/1000/3600/24,
                        "mode": "IT",
                        "spectrum": None,
                    },
                },
            },
        },
    },
    "Xe135": \
    {
        "label": "$^{135}$Xe",
        "parents": \
        [
            {"Xe134": "nCapture"},
            {"Xe135m": "RadioactiveDecay"},
        ],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Cs135": \
                    {
                        "half_life_days": 9.14/24,
                        "mode": "$\beta^{-}$",
                        "spectrum": "xebox_50k_xe135_decay_1629266226_flat.root",
                    },
                },
            },
        },
    },
    "Xe135m": \
    {
        "label": "$^{135m}$Xe",
        "parents": [{"Xe134": "nCapture"}],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Xe135": \
                    {
                        "half_life_days": 15.29/60/24,
                        "mode": "IT",
                        "spectrum": None,
                    },
                },
            },
        },
    },
    "Xe136": \
    {
        "label": "$^{136}$Xe",
        "parents": [],
        "processes": \
        {
            "nCapture": \
            {
                "children": \
                {
                    "Xe137": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe136_capture_xe137.txt",
                            "NGATLAS": "xe136_capture_xe137.txt",
                        },
                    },
                },
            },
            "neutronInelastic": \
            {
                "children": \
                {
                    "Xe136": \
                    {
                        "cross_sections": \
                        {
                            "ENDF/B-VII.1": "xe136_inelastic.txt",
                            "NGATLAS": None,
                        },
                    },
                },
            },
        },
    },
    "Xe137": \
    {
        "label": "$^{137}$Xe",
        "parents": [{"Xe136": "nCapture"},],
        "processes": \
        {
            "RadioactiveDecay": \
            {
                "children": \
                {
                    "Cs137": \
                    {
                        "half_life_days": 3.818/60/24,
                        "mode": "$\beta^{-}$",
                        "spectrum": "xebox_50k_xe137_decay_264330945_flat.root",
                    },
                },
            },
        },
    },
}