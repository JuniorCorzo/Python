def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] + numbers[j] == target:
                return [i, j]

    return[]

print(two_sum([1234 ,5678 ,9012], 14690))