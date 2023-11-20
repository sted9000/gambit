# This is the actual script, but I will run it on my windows os so that pyautogui has access to mouse object
import pyautogui as gui
from time import sleep

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
positions = ['sb', 'bn']
op_options = 5
ip_options = 5
ip_options_vs_bet = 4

def response_click(res_position):
    gui.click(x=screen_positions['responses'][res_position][0], y=screen_positions['responses'][res_position][1])
    sleep(1)

for position in positions:
    for op_option in range(op_options):
        if position == 'sb':
            gui.screenshot(f'./screenshots/{position}_0_{op_option}.png',
                           region=screen_positions['range_percent'][op_options][op_option])


        else:
            response_click(op_option+1)
            if op_option == 0:
                for ip_option in range(ip_options):
                    gui.screenshot(f'./screenshots/{position}_{op_option}_{ip_option}.png',
                                   region=screen_positions['range_percent'][ip_options][ip_option])


            else:
                for ip_option in range(ip_options_vs_bet):
                    gui.screenshot(f'./screenshots/{position}_{op_option}_{ip_option}.png',
                                   region=screen_positions['range_percent'][ip_options_vs_bet][ip_option])

            response_click(0)  # back
