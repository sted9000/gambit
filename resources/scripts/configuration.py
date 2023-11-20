from pathlib import Path

user_name = 'sted9' # 'Ted' | 'Administator'
tree_Path = Path('C:\\Users\\' + user_name + '\\Desktop\\gambitData_28')
monker_Path = Path('C:\\Users\\' + user_name + '\\Desktop\\MonkerSolver\\ranges')
bbs = '100'
rake = '2.5_1.5bb' # 2.0_uncapped | 2.5_0.9bb | 2.5_1.5bb | 4.0_0.3bb | 2.5_0.9bb_ante
players = '6'
base_Path = tree_Path / bbs / rake / players / 'raw'
seats = 6
inicial_sleep = 2 # units: seconds
load_sleep = 2 # units: seconds
save_sleep = 2 # units: seconds

# Suitedness
suitedness_dic = {
    # Note: Still need to split ss hands into 1- SS w/ top; 2- SS w/ Bottom
    "pp" : {
        'ds' : 'xxyy:RR',
        'ss' : 'xxyz:RR',
        '3s' : 'xxx:RR',
        'rb' : 'wxyz:RR'
    },

    # Matrix:
    "np" : {
        'ds': 'xxyy!RR',
        'ss': 'xxyz!RR',
        '3s': 'xxxy!RR',
        '4s': 'xxxx!RR',
        'rb': 'wxyz!RR'
    }
}

# screen positions
screen_dict = {
    'res_1' : (46,1440),
    'res_2' : (96,1440),
    'res_3' : (173,1440),
    'res_4' : (232,1440),
    'action_0' : (575,80),
    'action_1' : (1725,80),
    'action_2' : (2420,80),
    'search_area' : (1416,1540),
    'csv_option' : (1182,768),  # w/o filter
    'save_as_text' : (1300,838),  # w/o filter
    'include_0_hands' : (1231,824)  # with filter
}


