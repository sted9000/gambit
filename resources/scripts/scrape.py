from increment import *
from configuration import *


# Prepare monker and assocaited directories
first_step()

# loop around for rfi
for seat in range(seats - 1): # loop through openers positions (minus one because bb can't open)
    for suit_dic_key, suit_dic_value in suitedness_dic.items(): # loop suit categories (pp, np)
        for suit_key, suit_value in suit_dic_value.items(): # loop through suits

            # open
            enter_search_syntax(suit_value)
            save_to_monker(suit_key, 2)
            move_to_tree(str(seat), suit_dic_key, suit_key) # move RFI

    fold(1)

'''
            click('open') # open

            # loop around the top gather defend, vs 3b, vs 4b, vs 5b against a single rfi
            for dp_index, dp in enumerate(defend_pos[op_index:]):

                # defend
                if dp_index > 0: incrementDefend() # increment defend
                getDefend() # get defend
                moveDefend(base_Path / 'dfd' / op / dp / (suit_dic_key + '_' + suit_key)) # move defend

                # multiway
                if dp_index == 0:
                    click('call')
                    getVsFlat()
                    moveVsFlat(base_Path / 'mtw' / op / defend_pos[dp_index + 1] / (suit_dic_key + '_' + suit_key)) # move defend)
                    for flat in range(5 - op_index - 2):
                        incrementVsFlat(dp)
                        getVsFlat()
                        moveVsFlat(base_Path / 'mtw' / op / defend_pos[dp_index + flat + 2] / (suit_dic_key + '_' + suit_key)) # move defend)
                    resetFlat(dp)


                # 3bet
                if dp != 'bb': click('raise')
                else: click('call') # raise but only three options
                incrementVsThree(dp) # increment vs3bet - loop to original openers position
                getVsThree() # get vs3bet
                moveVsThree(base_Path / 'v3b' / op / dp / (suit_dic_key + '_' + suit_key)) # move vs3bet

                # 4bet
                click('call') # this is really hitting raise but there are only 3 options
                getVsFour() # get vs4bet
                moveVsFour(base_Path / 'v4b' / op / dp / (suit_dic_key + '_' + suit_key)) # move vs4bet

                # 5bet
                click('call') # this is really hitting raise but there are only 3 options
                getVsFive() # get vs5bet
                moveVsFive(base_Path / 'v5b' / op / dp / (suit_dic_key + '_' + suit_key)) # move vs5bet

                # reset to original open
                resetOpen(dp)

            # reset to inicial state
            resetInicial()

'''