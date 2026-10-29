import datetime

# print today d-h-m-s
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# print hi
print("Hi")

# print lblblblblblb
print("lblblblblblb")


# write a quick sort, 原地排序
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# test
test_arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", test_arr)
quick_sort(test_arr, 0, len(test_arr) - 1)
print("Sorted array:", test_arr)
