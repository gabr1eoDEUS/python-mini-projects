from time import sleep
n = 21
     #Utilizando o laço while
while True:
    n -=1
    sleep(1)
    print(n)
    if n == 1:
        break
print('\n BOMMMM!!!! POWWWWWW!!! Feliz ano novo :)')

    #Utilizando o laço for
for i in range(20, 1, -1):
    sleep(1)
    print(i)
print('\n BOMMMM!!!! POWWWWWW!!! Feliz ano novo :)')
