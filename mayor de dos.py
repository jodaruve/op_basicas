print("Ingrese el primer numero")
n1 = int(input())
print("Ingrese le segundo numero")
n2 = int(input())
if n1 == n2:
    print("Los numeros son iguales")
elif n2 > n1:
    print(n2, "es mayor que", n1)
else:
    print(n1, "es mayor que", n2)
