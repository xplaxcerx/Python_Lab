print('Минимальное число соответсвующее условию:')
print('\n')
print('Первый вараинт')

check = set()
for n in range(1,10):
    for n1 in range(1, 10):
        for n2 in range(1, 10):
            for n3 in range(1, 10):
                if (n1 != n2 and n2 != n3 and n1!= n3):
                    if (n ** 3 == ((n1 ** 3) + (n2 ** 3) + (n3 ** 3))):
                        check.add(n)
print(min(check))


print('Второй вараинт')
n = 1
n1 = 1
n2 = 1
n3 = 1
while(n > 0):
    while(n1 < 10):
        while(n2 < 10):
            while(n3 < 10):
                if n1 != n2 and n1 != n3 and n2 != n3:
                    if n**3 == n1**3 + n2**3 + n3**3:
                        print(n)
                    break
                  
                n3+=1
            n2+=1
            n3 = 1
        n1+=1
        n2 = 1
    n+=1
    n1 = 1
  
