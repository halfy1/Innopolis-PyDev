numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_arr = sum(x for x in numbers if x != None)
None_index = numbers.index(None)
numbers[None_index] = sum_arr / len(numbers)

print("Измененный список:", numbers)
