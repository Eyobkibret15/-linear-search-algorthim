import time

size = int(input("enter the size of an array: "))
result = False

user_array = [0] * size
user_array[size - 1] = 1
searched_value_for_worst_case = user_array[size - 1]
user_array[0] = 2
searched_value_for_best_case = user_array[0]

def simple_linear_search(array_list, searched_value, result):  # continue until the ellement ends
    for i in range(len(array_list)):
        if array_list[i] == searched_value:
            result = True
    return result


def improved_linear_search(array_list, searched_value, result):  # stop seaeching when it gates the matched item
    for i in range(len(array_list)):
        if array_list[i] == searched_value:
            return True
    return result


def improved_linear_search_with_Sentinel(array_list, searched_value, result):  # it's one step faster than the one
    last_element = array_list[len(array_list) - 1]  # we see before it minimize the comprasion
    array_list[len(array_list) - 1] = searched_value
    i = 0
    while array_list[i] != searched_value:
        i += 1
    if i < (len(array_list) - 1) or last_element == searched_value:
        return True
    return result


def binary_search(array, searched_value):  # it is faster than all
    array.sort()  # it search and compare many items ones
    max = len(array) - 1

    min = 0
    while min <= max:
        mid = min + ((max - min) // 2)
        if array[mid] == searched_value:
            return True
        elif array[mid] != searched_value and array[mid] > searched_value:
            max = mid - 1
        elif array[mid] < searched_value:
            min = mid + 1
    return result

    # for worst case scenarios in milli second
# simple_linear_search
print("------simle linear search for worst case ------")
start1 = time.time()
simple_linear_search(user_array, searched_value_for_worst_case, result)
end1 = time.time()
print(f"simple: {(end1 - start1)*1000}ms")

# improved linear search
print("-------improved linear search for worst case-------")
start2 = time.time()
improved_linear_search(user_array, searched_value_for_worst_case, result)
end2 = time.time()
print(f"improved: {(end2 - start2)*1000}ms")

# improved linear search with sentinel
print("-----improved linear searched with sentinel for worst case-----")
start3 = time.time()
improved_linear_search_with_Sentinel(user_array, searched_value_for_worst_case, result)
end3 = time.time()
print(f"improved with sentinel: {(end3 - start3)*1000}ms")


     # for best case scenarios in millisecond
# simple_linear_search
print()
print("------simle linear search for best case------")
start4 = time.time()
simple_linear_search(user_array, searched_value_for_best_case, result)
end4 = time.time()
print(f"simple: {(end4 - start4)*1000}ms")

# imroved linear search
print("-------imporved linear search for bast case-------")
start5 = time.time()
improved_linear_search(user_array, searched_value_for_best_case, result)
end5 = time.time()
print(f"improved: {(end5 - start5)*1000}ms")

# improved linear search with sentinel
print("-----improved linear searched with sentinel for best case-----")
start6 = time.time()
improved_linear_search_with_Sentinel(user_array, searched_value_for_best_case, result)
end6 = time.time()
print(f"improved with sentinel: {(end6 - start6)*1000}ms")

# binary search for worst case scenario in milli second
print()
print("-------binary search for worst case-------")
start7 = time.time()
binary_search(user_array, searched_value_for_best_case)
end7 = time.time()
print(f"binary: {(end7 - start7)*1000}ms")
