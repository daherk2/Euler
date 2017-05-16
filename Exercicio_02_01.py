'''
 na  naa  aux
 2    1    0
 3    2    3
 5    3    5
 8    5    8
 13   8    13
'''

# 0,1,2,3,4,5, 6 , 7, 8, 9,...
# 1,2,3,5,8,13,21,34,55,89,...
'''
na = 1
naa = 1
aux = 0
#soma = 2
soma = 0
for i in range(1,4000000):
    #print 'na '+str(na)+' -  naa '+str(naa)+' - aux '+str(aux)
    aux = na
    na = na + naa
    naa = aux
    if na % 2 == 0:
        soma = soma + na
print soma

'''


cache = {}
def fiba(n):
     cache[n] = cache.get(n, 0) or (n <= 1 and 1 or fiba(n-1) + fiba(n-2))
     return cache[n]
n = 0
x = 0
while fiba(x) <= 4000000:
       if not fiba(x) % 2: n = n + fiba(x)
       x=x+1
print(n)
