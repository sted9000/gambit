from os.path import basename

def preview_csv(data_files):
    for file in data_files:
        print(f'File: {basename(file)}\n')
        with open(file, "r") as f:
            lines = f.readlines()
            for line in range(3):
                print(lines[line])
            print('-----')
            
def preview_list_of_lists(list_of_lists):
    for l in list_of_lists:
        for line in l[:3]:
            print(line)
        print('-----')

def preview_list(hands_to_keep):
    for line in hands_to_keep[:5]:
        print(line)
        

def preview_dict_of_lists(dict_of_lists):
    for key in dict_of_lists:
        print(key)
        for item in dict_of_lists[key][:3]:
            print(item)
        print('-----')
        
        
def preview_dict_of_dicts(dict_of_dicts):
    for key in dict_of_dicts:
        print(key)
        counter = 0
        for nest_key in dict_of_dicts[key]:
            print (nest_key, dict_of_dicts[key][nest_key])
            counter += 1
            if counter == 3:
                break
        print('-----')