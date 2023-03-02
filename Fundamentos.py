#Alcantara Gomez Axel Octavio


print("\n 09/02/2023")

def nuevoTema(tema):
    print("         ", tema, "          " )

nuevoTema("Operadores arimeticos")
print("Operador division entera (10//3): ", 10//3 )
print("Operador pitencia (5**3): ", 5**3)


print("")
print("         Operadores logicos          ")
print("Operadores and (True and False): ", True and False)
print("Operadores and (True and True): ", True and True)
print("Operadores and (False and False): ", False and False)
print("")
print("Operadores or (True or False): ", True or False)
print("Operadores or (True or True): ", True or True)
print("Operadores or (False or False): ", False or False)
print("")
print("Operadores not (not False): ", not False)
print("Operadores not (not True): ", not True)


print("")
print("         Operadores de comparacion       ")
print("Operador == (2==3): ", 2==3)
print("Operador != (2!=3): ", 2!=3)
print("Operador > (2>3): ", 2>3)
print("Operador < (2<3): ", 2<3)
print("Operador >= (2>=3): ", 2>=3)
print("Operador <= (2<=3): ", 2<=3)


print("")
nuevoTema("Variables")
entero= 1
flotante = 3.1416
cadena="Hola"
cadena_dos="Hola2"
a,b,c=10,3.1416,"Hola3"
print(entero, flotante, cadena, cadena_dos,a,b,c)


print("")
nuevoTema("Enteros")
w=100
x=989825123451352234
y=-256
z=0b0101
h=0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))


print("")
nuevoTema("Flotantes")
x=1.39999
print(x, type(x))
y=.900234
print(y, type(y))


print("")
nuevoTema("Complejos")
x= -56j
y= 12+56j
z= 2j
print(x, type(x))
print(y, type(y))
print(z, type(z))


print("")
nuevoTema("Booleanos")
lis= [0]
print(lis, "es ", bool(lis))
t=()
print(t, "es ", bool(t))
t="Hello"
print(t, "es ", bool(t))
t=99
print(t, "es ", bool(t))
t= 1+0j
print(t, "es ", bool(t))
t=None
print(t, "es ", bool(t))


print("")
nuevoTema("Listas")
a = [10, 20.5, "Python list"]
print(a)
print(a[1])
a[0]="Hola"
print(a[0])


print("")
nuevoTema("Tuplas")
t = (10, 20.5, "Tupla")
print(t)
print(t[1])
print(t[0:3])


print("")
nuevoTema("Conjuntos")
t={50,20,30,40,10,50}
print("Conjuntos: ", t, type(t))


print("")
nuevoTema("Diccionarios")
t={1:"valor1", "Valor2":2}
print(t, type (t))
print("t[Valor2]:", t["Valor2"])


print("")
nuevoTema("Cadenas")
s= "Esta es una cadena" #Tambien se pueden escribir con comillas simples
print(s)
s='''Esta es 
una cadena  '''
print(s)
cadena1="Hola"
cadena1= (cadena1+" ")*5
print(cadena1)
print(cadena1.capitalize())
#Cadenas


#if



