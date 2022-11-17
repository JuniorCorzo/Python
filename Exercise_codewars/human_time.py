def redable_time(seconds):
    hh = 00
    mm = 00
    ss = 00
    for i in range(seconds):
        ss += 1
        if ss == 60:
            mm +=1
            ss = 0
        if mm == 60:
            hh += 1
            mm = 0
    
    result = "{:02}:{:02}:{:02}".format(hh, mm, ss)
    return result

print(redable_time(359999))