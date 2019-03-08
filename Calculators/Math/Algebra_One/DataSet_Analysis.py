def comparing_datasets(list):
    mean = 0
    for number in list:
        mean += number
    new_mean = mean / len(list)
    max_number = max(list)
    min_number = min(list)
    spread = max_number - min_number
    list.sort()
    print(list)
    print(len(list))
    print("-------------------------")
    print("The mean of the data set is:",new_mean)
    print(max_number)
    print(min_number)

comparing_datasets([2,14,1,2,0,1,0,2])
