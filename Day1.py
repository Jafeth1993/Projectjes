
# Getting data
with open("day1.in") as file:
    data = [i for i in file.read().strip().split("\n")]

# print(data)


# Transversing every STRING in our DATA
max = 0
max2 = 0   # Elf with the second greatest amount of calories
max3 = 0   # Elf with the third greatest amount of calories
count = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num

    if count > max:
        max = count
    elif count > max2:
        max2 = count
    elif count > max3:
        max3 = count


    print("Answer to part 1:", max)
    print("Answer to part 2:", max+max2+max3)
