n = int(input("Enter a number  "))
lista = [[]for i in range(n)]
num = 2
for i in range(len(lista)) :
    count = n - i
    temp = 0 
    while count >= 1 :
        lista[i].append(num + (2*(temp)))
        count = count - 1
        temp = temp + 1
    num = num + 1  
print(lista)
pattern = [" " for i in range(2*n+1)]
for i in range(len(lista)):
    for m in lista[i]:
        print(m)
            pattern[m] = "*"
    print(" ".join(pattern))