def my_sort(lst):
    a = len(lst)
    for i in range(a):
        for b in range(0,a-i-1):
            if lst[b] > lst[b+1]:
                lst[b], lst[b+1] = lst[b+1], lst[b]

def meanVsMedian(lst):
    avg_value = sum(lst) / len(lst)

    sorted_list = my_sort(lst)
    n = len(sorted_list)
    if n % 2 != 0:
        mdn_result = sorted_list[n // 2]
    elif n % 2 == 0:
        mdn_result = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
        
    if avg_value > mdn_result:
        print("mean")
    elif avg_value < mdn_result:
        print("median")
    elif avg_value == mdn_result:
        print("same")
    print("Середнє значення: ",avg_value)
    print("Медіана: ",mdn_result)

            



user_list = list(map(int, input('Введіть кілька чисел через пробіл: ').split()))
meanVsMedian(user_list)


