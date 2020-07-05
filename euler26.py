# 返回n的循环节长度
def length(n):
    i=1
    while n % 2 == 0:n =n // 2
    while n % 5 == 0:n =n // 5
    while True:
        if (10**i -1) % n ==0:
            return i
        else:
            i+=1


num,l_max = 7,6
for n in range(2,1000):
    if l_max < length(n):
        num,l_max = n,length(n)

print(f"{num}对应的循环节长度为{l_max}")
