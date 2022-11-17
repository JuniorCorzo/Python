def split_strings(string):
    
    if len(string) % 2 != 0:
        string += "_"

    index = 0
    list_string_split = []
    while index != len(string) and len(string) > 0:
        list_string_split.append(string[index:index + 2])
        index += 2
    
    return list_string_split

list_split = split_strings("")
print(list_split)