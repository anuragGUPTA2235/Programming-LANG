def team(n,m):
    one_ans = (m + n) // 4
    sec_ans = min(n,m)
    if one_ans > sec_ans:
        return sec_ans
    return one_ans
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    max_team = team(n,m)
    print(max_team)
