def d(n):
    return sum(i for i in range(1,n//2+1) if n%i ==0)

# 生成过盈数列表和字典
lst= [a for a in range(12,28124-12) if a < d(a)]
dct = dict.fromkeys(lst, True)
print(dct)
ans = 0
for n in range(1, 28124):
    not_sum = True
    # 若 a 是过盈数，n-a也是过盈数，即 n 为两个过盈数之和
    for a in lst:
        if a < n and dct.get(n - a):
            not_sum = False
            break
    if not_sum:
        ans += n

print(ans)
