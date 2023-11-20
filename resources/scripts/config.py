screen_positions = {
    'range_percent': {
        5: {
            0: (1881, 72, 100, 16),
            1: (2014, 72, 100, 16),
            2: (2144, 72, 100, 16),
            3: (2277, 72, 100, 16),
            4: (2407, 72, 100, 16)
        },

        4: {
            0: (1881, 72, 100, 16),
            1: (2044, 72, 100, 16),
            2: (2209, 72, 100, 16),
            3: (2375, 72, 100, 16)
        }
    },

    'responses': {
        0: (41, 1444),
        1: (111, 1444),
        2: (173, 1444),
        3: (234, 1444),
        4: (292, 1444),
        5: (350, 1444)
    }
}

sims = {
    'sb_bn_3bp': {
        'steps': [
            {
                'title': 'OP First Acton',
                'setup': None,
                'captures': ['check', '25', '50', '75', '100'],
                'ss_prefix': 'sb_0',
                'trim': True
            },
            {
                'title': 'OP vs Check',
                'setup': [('response', 1)],
                'captures': ['check', '25', '50', '75', '100'],
                'ss_prefix': 'bn_0',
                'trim': True
            },
            {
                'title': 'OP vs 25',
                'setup': [('response', 0), ('response', 2)],
                'captures': ['fold', 'call', '40', '100'],
                'ss_prefix': 'bn_1',
                'trim': False
            },
            {
                'title': 'OP vs 50',
                'setup': [('response', 0), ('response', 3)],
                'captures': ['fold', 'call', '40', '100'],
                'ss_prefix': 'bn_2',
                'trim': False
            },
            {
                'title': 'OP vs 75',
                'setup': [('response', 0), ('response', 4)],
                'captures': ['fold', 'call', '40', '100'],
                'ss_prefix': 'bn_3',
                'trim': False
            },
            {
                'title': 'OP vs 100',
                'setup': [('response', 0), ('response', 5)],
                'captures': ['fold', 'call', '40', '100'],
                'ss_prefix': 'bn_4',
                'trim': False
            }
        ]
    }
}