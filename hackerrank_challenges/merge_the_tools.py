def merge_the_tools(string, k):
    t = []
    u = []
    sl = len(string) / k
    for i in range(0, len(string), k):
        t.append(string[i:(i+k)])
    for d in t:





if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)