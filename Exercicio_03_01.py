num = 600851475143
i = 2
while i * i < num:
     while num % i == 0:
         num = num / i
     print str(num) + " - " + str(i)
     i = i + 1

print(num)