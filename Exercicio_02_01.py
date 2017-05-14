'''
 na  naa  aux
 2    1    0
 3    2    3
 5    3    5
 8    5    8
 13   8    13
'''

# 1,2,3,5,8,13,21,34,55,89,...
na = 2
naa = 1
aux = 0
soma = 2
for i in range(1,4000000):
    #print 'na '+str(na)+' -  naa '+str(naa)+' - aux '+str(aux)
    aux = na
    na = na + naa
    naa = aux
    if na % 2 == 0:
        soma = soma + na
print soma