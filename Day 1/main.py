

with open('text.txt') as file:
    data = [i for i in file.read().strip().split('\n')]

# print(data)

count = 0
maximum = 0
elf_list = []

for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num

    if count > maximum:
        maximum = count

    if count > 0:
        elf_list.append(count)

print(f"The answer is {maximum}!")

s_list = sorted(elf_list)
winner_list = s_list[-3:]
number = sum(winner_list)
print(f"The top 3 total is {number}.")