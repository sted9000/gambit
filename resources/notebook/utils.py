"""
These are the functions for the Format MonkerSolver CSV Files Notebook
"""
import os
import json
import ipywidgets as widgets
from IPython.display import display


def find_paths(base_path):
    """
    Creates a list of paths each of which contains a group of csv files to be processed together
    :param base_path: string, relative path to root directory
    :return: list
    """
    dirs_to_process = []
    for root, dirs, files in os.walk(base_path):
        if len(files) > 0:
            temp = []
            for f in files:
                temp.append(os.path.join(root, f))
            dirs_to_process.append(temp)

    return dirs_to_process


def csv_to_list(data_files):
    """
    Take a list of csv files and return a list of formatted python lists
    :param data_files: paths of files to be opened
    :return: list of lists
    """
    list_of_lists = []
    for file in data_files:
        temp_list = []
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                # Don't look at the first line (because those are the labels)
                if not line.startswith('Combo'):
                    split_line = line.split(',')
                    split_line[2] = split_line[2].replace('\n', '')
                    temp_list.append(split_line)

        list_of_lists.append(temp_list)
        print(len(temp_list))

    print('-----')
    return list_of_lists


def compare_weights(csv_lists):
    """
    Compares elements in two lists by looking at which hand has the higher weight.
    :param csv_lists: A lists of lists
    :return: One list of the hands that we want to keep
    """
    hands_to_keep = []
    fold_hands = csv_lists[0]
    raise_hands = csv_lists[1]

    # loop through fold hands as it is always longer
    for fold_hand in fold_hands:

        # if fold is not in raise, then keep fold
        if fold_hand[0] not in [raise_hand[0] for raise_hand in raise_hands]:
            hands_to_keep.append([fold_hand[0], fold_hand[2]])
            continue

        # if it is then find the place where it is and compare weights
        for raise_hand in raise_hands:
            if fold_hand[0] == raise_hand[0]:
                # if raise weight is greater than fold weight
                if float(raise_hand[1]) >= float(fold_hand[1]):
                    hands_to_keep.append([raise_hand[0], raise_hand[2]])
                else:
                    hands_to_keep.append([fold_hand[0], fold_hand[2]])
                break




    return hands_to_keep

    #
    # # loop through all the fold hands
    # for i, fold_hand in enumerate(fold_hands):
    #
    #     # if fold hand is also in raise hands
    #     if fold_hand[0] in [raise_hand[0] for raise_hand in raise_hands]:
    #
    #         print(fold_hand, i)
    #         # keep the higher weighted one
    #         if float(raise_hands[i][1]) >= float(fold_hand[1]):
    #             hands_to_keep.append([raise_hands[i][0], raise_hands[i][2]])
    #         else:
    #             hands_to_keep.append([fold_hand[0], fold_hand[2]])
    #
    #     # else just keep the fold hand
    #     else:
    #         hands_to_keep.append([fold_hand[0], fold_hand[2]])
    #
    # return hands_to_keep


# *** Remove equal hands

def separate_hands(hands):
    """
    Simply split the list of hands into its meaningful parts
    @param hands: [hand, ev]
    @return: [[rank, suit, ev],...]
    """
    sep_hands = []
    for hand in hands:
        rank = hand[0][0] + hand[0][2] + hand[0][4] + hand[0][6]
        suits = hand[0][1] + hand[0][3] + hand[0][5] + hand[0][7]
        sep_hands.append([rank, suits, hand[1]])

    return sep_hands


def normalize_suits(hands):
    """
    Turn the suit element in each hand into wxyz notation from traditional suits.
    :param hands: [[rank, suit, ev],...]
    :return: [[rank, suit_now_normalized, ev],...]
    """
    nor_hands = []
    for hand in hands:
        s = hand[1]  # first card
        c0 = 'w'
        if s[1] == s[0]:  # second card
            c1 = 'w'
        else:
            c1 = 'x'
        if s[2] == s[0]:  # third card
            c2 = 'w'
        elif s[2] == s[1]:
            c2 = 'x'
        else:
            if s[1] == s[0]:
                c2 = 'x'
            else:
                c2 = 'y'
        if s[3] == s[0]:  # fourth card
            c3 = 'w'
        elif s[3] == s[1]:
            c3 = 'x'
        elif s[3] == s[2]:
            c3 = 'y'
        else:
            if s[0] == s[1] == s[2]:
                c3 = 'x'
            elif s[1] == s[0] or s[2] == s[1] or s[2] == s[0]:
                c3 = 'y'
            else:
                c3 = 'z'

        nor_hands.append([hand[0], c0 + c1 + c2 + c3, hand[2]])

    return nor_hands


def remove_duplicates(hands):
    """
    Now that our suits are normalized we simply only keep one of each hand
    :param hands:
    :return:
    """
    singles_list = []
    for hand in hands:
        if hand not in singles_list:
            singles_list.append(hand)

    return singles_list


def pairs_to_front(hands):
    """
    This function takes a list that have elements that are paired hands. Elements are formatted ['rank', 'suit',
    ev]. It returns a new list with the paired elements moved to the front of the rank string. Note: The suit order
    does not change, because rank matters, not pairs vs non-pairs.
    :param hands: [['7664', 'wwxy', '36.65652584723076'],...]
    :return: list: [['6674', 'wxwy', '36.65652584723076'],...]
    """
    new_lst = []
    for items in hands:
        ranks = items[0]
        suits = items[1]
        ev = items[2]
        # two pairs
        if ranks[0] == ranks[1] and ranks[2] == ranks[3]:
            new_lst.append(items)
        # one pair up front
        elif ranks[0] == ranks[1]:
            new_lst.append(items)
        # one pair in the middle
        elif ranks[1] == ranks[2]:
            ranks = ranks[1] + ranks[2] + ranks[0] + ranks[3]
            new_lst.append([ranks, suits, ev])
        # one pair at the back
        else:
            ranks = ranks[2] + ranks[3] + ranks[0] + ranks[1]
            new_lst.append([ranks, suits, ev])
        """
        While there are more categories of paired hands. I don't think they need to be moved around in any special way.
        I could be wrong about this though.
        """

    return new_lst


def group_suits(hands):
    """
    This functions turns a list into a dictionary of lists by sorting the normalized suit element of each item.
    :param hands: [['3322', 'wxwx', 'ev'],... ]
    :return: dictionary of lists: { 'wxyz': ['3322', 'ev'],... }
    """
    suit_dict = {}
    for hand in hands:
        if hand[1] not in suit_dict:
            suit_dict[hand[1]] = []
        if [hand[0], hand[2]] not in suit_dict[hand[1]]:
            suit_dict[hand[1]].append([hand[0], hand[2]])

    return suit_dict


# *** Mapping
def create_open_maps(dict_of_lists):
    """
    Since our maps are grids of every side-card combination for each pair of show-down cards...
    we make each show-down pair into a dictionary with each side-card as a key in that dictionary.
    :param dict_of_lists: { 'wxyz': [['3322', 'ev'],...] }
    :return: dict_of_dicts { 'wxyz': AA: { KQ: ev ...
    """
    main_map = {}
    for key in dict_of_lists:
        suit_map = {}
        for hand in dict_of_lists[key]:
            if hand[0][:2] not in suit_map:
                suit_map[hand[0][:2]] = {}
                suit_map[hand[0][:2]][hand[0][2:]] = hand[1]
            else:
                suit_map[hand[0][:2]][hand[0][2:]] = hand[1]
        main_map[key] = suit_map

    return main_map


def create_impossible_object():
    """
    Create a dictionary with every side-card combo as keys and 'impossible' as each of their values
    :return: a dictionary
    """
    imp_obj = {}
    ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    for i in ranks:
        for j in ranks:
            if ranks.index(i) <= ranks.index(j):
                imp_obj[i + j] = 'impossible'

    return imp_obj


def create_maps_with_opens(opening_maps, impossible_object):
    """
    Adding the opening hands into the impossible dictionaries
    :param opening_maps: A dictionary with suits: sd-combos: sc-combos: ev
    :param impossible_object: Dictionary with all sd_combos: 'impossible'
    :return: A dictionary with suits: sd-combos: sc-combos: ev OR impossible
    """
    # iterate over suit dicts
    for key in opening_maps:
        # iterate over each showdown combo
        for sd_key in opening_maps[key]:
            # copy the impossible object
            temp_imp = impossible_object.copy()
            # iterate over each side-card combination
            for sc_combo in opening_maps[key][sd_key]:
                # replace the value of the side-card into the temp_inp dict
                temp_imp[sc_combo] = opening_maps[key][sd_key][sc_combo]
            # replace dict that only hand opens with one that now has opens and impossible hands
            opening_maps[key][sd_key] = temp_imp

    return opening_maps


def categorize_opens(opening_maps, legend):
    """
    Take the dictionaries objects that are opens and categorize those opens into something resembling css classes
    :param class_prefix: String, beginning of the class name
    :param opening_maps: A dictionary with suits: sd-combos: sc-combos: ev OR impossible OR fold
    :param shades: Int, how many different groupings of ev do you want (six seems good)
    :param shade_width: Int, how wide of bands for each ev groupings (300 seems good for opening ranges)
    :return: A dictionary with suits: sd-combos: sc-combos: group OR impossible OR fold
    """

    # iterate over suit dicts
    for key in opening_maps:
        # iterate over each showdown combo
        for sd_key in opening_maps[key]:
            # iterate over each side-card combination
            for sc_combo in opening_maps[key][sd_key]:
                if opening_maps[key][sd_key][sc_combo] != 'impossible':
                    if float(opening_maps[key][sd_key][sc_combo]) <= 0:
                        opening_maps[key][sd_key][sc_combo] = 'fold'
                    else:
                        for upper_range, css_class in legend.items():
                            if float(opening_maps[key][sd_key][sc_combo]) < upper_range:
                                opening_maps[key][sd_key][sc_combo] = css_class
                                break

    return opening_maps


def split_all(path):
    """
    I took this function from stackoverflow.
    It uses os.path.split and a while loop to return all parts of a path in a list.
    :param path: string
    :return: list
    """
    all_parts_list = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            all_parts_list.insert(0, parts[0])
            break
        elif parts[1] == path:  # sentinel for relative paths
            all_parts_list.insert(0, parts[1])
            break
        else:
            path = parts[0]
            all_parts_list.insert(0, parts[1])

    return all_parts_list


def is_pair(path):
    """
    Takes a path and returns a boolean if the string 'pp' is included in the list.
    Meaning that the file that path represents is a scrape of hands with pairs in them.
    :param path: string
    :return: boolean
    """
    path_parts = split_all(path)
    if "pp" in path_parts:
        return True
    else:
        return False


def save_maps(completed_map, file_path):
    """
    This function takes the maps and saves them. In a parallel directory named 'formattedData' 
    THIS IS A VERY HACKY FUNCTION, BEWARE!
    :param completed_map: A dictionary of suits: sd-combos: sc-combos: actions
    :param file_path: string of the original files that were formatted
    :return:
    """
    p = os.path.split(str(file_path).replace('gambitData', 'gambitFormatted'))[0]
    for key, value in completed_map.items():
        if not os.path.exists(p):
            os.makedirs(p)
        full_path = os.path.join(p, key + '.json')
        with open(full_path, "w+") as new_file:
            new_file.write(json.dumps(value))


def create_legend(class_prefix, number_of_classes, width_of_each_class):
    """
    Take the users inputs for the class_names and format a dictionary to be used as a legend
    :param class_prefix:
    :param number_of_classes:
    :param width_of_each_class:
    :return: Dictionary, the legend
    """
    legend = {}
    for number_of_class in range(number_of_classes):
        if number_of_class == number_of_classes - 1:
            upper_bound = float('inf')
        else:
            upper_bound = (number_of_class + 1) * width_of_each_class
        legend[upper_bound] = class_prefix + '-' + str(number_of_class)

    return legend


def save_legend(legend, path, openning_action):
    """
    Take a legend and insert it into the legend file
    :param openning_action:
    :param legend:
    :param path:
    :return:
    """

    legends_file_path = os.path.join(path, 'legends.json')

    if not os.path.exists(path):
        os.makedirs(path)
        legends_dict = {openning_action: legend}
        with open(legends_file_path, 'w+') as f:
            f.write(json.dumps(legends_dict))

    else:
        with open(legends_file_path, 'r+') as f:
            legends_dict = json.load(f)
            legends_dict[openning_action] = legend
            f.seek(0)  # goes to beginning of file
            f.write(json.dumps(legends_dict))  # writes the dicts
            f.truncate()  # makes the file only as long as as the dict


def format_files(files_to_process, legend):
    """
    This is the main function that a iterates over list of csv files as input and saves the formatted maps...
    as outputs in json files.
    Also it has a widget to display the progress because this function will take a long time to complete.    
    :param files_to_process: list of list [[../1.csv, ../2.csv]
    :return: string, 'Done'
    """

    max_count = len(files_to_process)
    f = widgets.IntProgress(min=0, max=max_count, description='Files Completed:')  # instantiate the bar
    display(f)  # display the bar

    for files in files_to_process:

        csv_lists = csv_to_list(files)
        hands_to_keep = compare_weights(csv_lists)
        separated_hands = separate_hands(hands_to_keep)
        normalized_suits = normalize_suits(separated_hands)
        singles_list = remove_duplicates(normalized_suits)
        if is_pair(files[1]):  # if hands are paired
            singles_list = pairs_to_front(singles_list)  # move the pairs to the front of the string
        suit_groups = group_suits(singles_list)
        open_maps = create_open_maps(suit_groups)
        impossible_object = create_impossible_object()
        maps_with_opens = create_maps_with_opens(open_maps, impossible_object)
        # maps_with_folds = add_folds(maps_with_opens)
        completed_maps = categorize_opens(maps_with_opens, legend)
        save_maps(completed_maps, files[0])
        f.value += 1

    return 'Done'
