import sys


def time_delta(t1, t2):
    t1_day, t1_dd, t1_mm, t1_year, t1_time, t1_zone = t1.split(' ')
    t2_day, t2_dd, t2_mm, t2_year, t2_time, t2_zone = t2.split(' ')



    return 0


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
