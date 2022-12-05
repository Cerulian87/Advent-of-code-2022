# with open('rucks.txt') as file:
#     data = [i for i in file.read().strip().split('\n')]

# total = 0
# for i in data:
#     first_comp = i[:len(i)//2] 
#     second_comp = i[len(i)//2:]

#     letter_list = []
#     points = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
#     index = 0

#     for a in first_comp:
#         for b in second_comp:
#             if a == b:
#                 letter_list.append(a)

#     matches = list(set(letter_list))

#     for i in matches:
#         for j in points:
#             index = j.index(i)+1
#             total += index
#             # print(index)
    
# print(f"The answer is {total}!")
            
# data = ['vJrwpWtwJgWrhcsFMMfFFhFp',
# 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
# 'PmmdzqPrVvPwwTWBwg',
# 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
# 'ttgJtRGJQctTZtZT',
# 'CrZsJsPPZsGzwwsLwLmpwMDw']

with open('rucks.txt') as file:
    data = [i for i in file.read().strip().split('\n')]

start = 0
end = len(data)
step = 3
total = 0
for i in range(start, end, step):
    x = i
    triple = data[x:x+step]
    # print(triple)
    a = triple[0]
    b = triple[1]
    c = triple[2]
    # print(f"a = {a}, b = {b}, c = {c}")
    letter_list = []
    points = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
    index = 0
    for x in a:
        for y in b:
            for z in c:
                if x == y and y == z:
                    letter_list.append(x)
    matches = list(set(letter_list))
    for i in matches:
        for j in points:
            index = j.index(i)+1
            total += index
            # print(index)
    # print(matches)
print(total)