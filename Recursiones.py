__author__ = "Brayan Steven Diaz ID : 642704"
__date__ = "23-mar-2018 1:54:58"



def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def fac(f):
    if f == 1:
        return 1
    else:
        return f * fac(f-1)
    
def mul (a,b):
    if b==1:
        return a
    else:
        return a + mul (a , b - 1)
    
def trianpas(n):
    if n==0:
        return[]
    if n==1:
        return [[1]]
    last_list = trianpas(n-1)
    
    this_list =[1]
    
    for i in range (1,n-1):
        this_list.append(last_list[n-2][i-1] + last_list[n-2][i])
    this_list.append(1)
    
    last_list.append(this_list)
    
    return last_list

def linea(n): 
    triangle = trianpas(n) 
    return triangle[n-1]


def triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        new_row = [1]
        last_row = triangle(n-1)
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
    return new_row

def inverso(list):
    if len(list)==1:
        return list
    else:
        return list[-1]+inverso(list[:-1])

def euclides (a,b):
    if b==0:
        return a
    else:
        return euclides (b , a % b)

if __name__ == '__main__':
    
    fibonacci = fib(22)
    print('Fibonacci de orden 10:')
    print(fibonacci)
    
    factorial = fac(8)
    print('factorial de 5:')
    print(factorial)
    
    multiplicacion = mul(12,2)
    print('la multiplicacion es:')
    print(multiplicacion)
 
res = linea(14)
print (res)

re1 = triangle(14)
print (re1)

cadena = inverso("abcdefg")
print('el inverso de la cadena es :')
print(cadena)

mcd = euclides(369,1218)
print('MCD Euclides :')
print(mcd)
