T = int(input())
for _ in range(T):
    n = int(input())
    dic = {}
    for _ in range(n):
        name, group = input().split()
        if group in dic:
            dic[group].append(name)
        else:
            dic[group] = [name]
        print(dic)
