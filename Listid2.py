
#8
# list1 = ['крот', 'белка', 'выхухоль']
# list2 = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
# list3 = ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
# list = max(max(len(s) for s in sublist) for sublist in [list1, list2, list3])
# list1 = [s.ljust(list, '_') for s in list1]
# list2 = [s.ljust(list, '_') for s in list2]
# list3 = [s.ljust(list, '_') for s in list3]
# print(list1)
# print(list2)
# print(list3)

########################################################################
#11

# ['a', 'b', 'c', ...]
# list = [chr(i) for i in range(ord('a'), ord('z')+1)]
# list2 = [char * (index + 1) for index, char in enumerate(list)]
# print(list)
# print(list2)

########################################################################
#12

# import random
# numbers = [random.randint(1, 100) for _ in range(10)]
# print("Исходный список:", numbers)
# min_index = numbers.index(min(numbers))
# max_index = numbers.index(max(numbers))
# numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
# print("Измененный список:", numbers)
