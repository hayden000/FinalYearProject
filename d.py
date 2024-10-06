def modify_list(lst, item):
    output_list = []
    for i in range(len(lst)):
        temp = [j.copy() for j in lst]
        temp[i].append(item)
        output_list.append(temp)
    temp = [sublist.copy() for sublist in lst]
    temp.append([item])
    output_list.append(temp)
    return output_list


pattern_list = [[1, 2], [3]]
item = 4
print(modify_list(pattern_list, item))
