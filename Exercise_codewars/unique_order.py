def order(iterable):
    if len(iterable) == 0:
        return []

    list_order = [iterable[0]]
    index = 0
    for value in iterable:
        if list_order[index] != value:
            list_order.append(value)
            index += 1
    
    return list_order
    
print(order(""))