fibo = [1,1]
while len(str(fibo[-1]))<1000:
  fibo.append(fibo[-1]+fibo[-2])
print(len(fibo))
