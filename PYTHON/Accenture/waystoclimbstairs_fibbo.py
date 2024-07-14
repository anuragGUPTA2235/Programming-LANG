## climb stairs (fibonacci series)
def fibbo_series(num_stairs):
    first = 1
    sec = 2
    for i in range((num_stairs)-2):
        ways = first + sec
        first = sec
        sec = ways

    return ways    
if __name__ == "__main__":
    num_stairs = 5
    ways = fibbo_series(num_stairs)
    print(ways)
