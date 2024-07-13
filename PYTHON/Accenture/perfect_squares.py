import math

def check_square_plot(arr_areas):
    counter = 0
    for items in arr_areas:
        if items == 1:
            counter += 1
        else:
            for num in range(1,items//2):
                if num * num == items:
                    counter += 1
    return counter

def easy_plot_square_checker(arr_areas):
    counter = 0
    for _ in arr_areas:
        root = math.sqrt(_)
        if root.is_integer():
            counter += 1
    return counter        





if __name__ == "__main__":
    num_plots = int(input())
    arr_areas = input()
    arr_areas = list(map(int,arr_areas.split()))
    res = check_square_plot(arr_areas)
    print(res)     
    res = easy_plot_square_checker(arr_areas)
    print(res)


