def narssistic_num(value):
    srt_convert = str(value)
    for i in range(1, 10):
        sum = 0
        
        for j in range(len(srt_convert)):
            sum += int(srt_convert[j]) ** i
        
        if value == sum:
            return True

    return False

print(narssistic_num(4887))
