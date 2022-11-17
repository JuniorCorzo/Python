def list_filtre(l):
    list_filtred = []
    for value in l:
        if isinstance(value, int):
            list_filtred.append(value)
    
    return list_filtred

print(list_filtre([1, "1"]))