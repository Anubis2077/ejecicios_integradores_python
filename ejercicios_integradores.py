#trabajo de ejercicios integradores
# set_alumno(self, Gerardo Morito):
    #if alumno != Gerardo Morito
        #raise ValueError ("alguien usurpo mis ejercicios")
    # if alumno == Gerardo Morito
        #print ("su trabajo es para un 10")
#jajaj



def calcular_mcd(a, b):
    """Se empieza dividiendo a entre b. Si el resto es cero, entonces b es el MCD de a y b, 
    y se devuelve b. Si el residuo no es cero, se hace a igual a b y b igual al resto.
    Luego se vuelve al paso 1. Este proceso continúa hasta que se encuentra un residuo cero, 
    lo que significa que se ha encontrado el MCD de los dos números
    """
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

a = 15
b = 18
mcd = calcular_mcd(a,b)
print("el maximo comun divisor de", a ,"y", b ,"es:", mcd)

#2.Escribir una función que calcule el mínimo común múltiplo entre dos números

def calcular_mcm(a, b):
    """Para calcular el mínimo común denominador (MCD) de dos números, se pueden seguir los siguientes pasos:
        Calcular el Máximo Común Divisor (MCD) de los dos números.
        Multiplicar los dos números. 
        Dividir el producto de los dos números por el MCD calculado en el paso 1."""
    mcd = calcular_mcd(a,b)
    return a * b //(mcd)

a=12
b=18
mcm = calcular_mcm(a,b)
print("el minimo comun denominador de", a, "y", b, "es:", mcm)

#3.Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
# cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def contar_palabras(cadena):
    palabras = cadena.lower().split()
        #recibe una palabra y la convierte todo a minuscula y luego las divide en letras
    
    frecuencia = {}
        #crea un diccionario vacio
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
            #hace una iteracion dentro de un bucle for en el cual por cada palabra que se repita agrega +=1 en el dict

        else:
            frecuencia[palabra] = 1
            #si no hay repeticion el valor es solamente 1

    return frecuencia
    #devuelve el diccionario

cadena = input("ingrese su texto:")
frecuencias = contar_palabras(cadena)
print(frecuencias) 

#4.Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
# palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
# que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def palabra_mas_repetida(frecuencias):
    palabra_mas_repetida = None
    #variable vacia
    frecuencia_mas_alta = 0
    #variable vacia
    for palabra, frec in frecuencias.items():
        #iteracion de palabra y frecuencia en frecuencias.items()
        if frec > frecuencia_mas_alta:
            palabra_mas_repetida = palabra
            frecuencia_mas_alta = frec
            #si la frecuencia es mayor que la frecuencia mas alta que de momento es 0 la palabra mas repetida es palabra
            #y la frecuencia mas repetida es frecuencia

    return (palabra_mas_repetida, frecuencia_mas_alta)

cadena = input("Ingrese una cadena de caracteres: ")
frecuencias = contar_palabras(cadena)
palabra, frecuencia = palabra_mas_repetida(frecuencias)
print(f'La palabra más repetida es "{palabra}" con una frecuencia de {frecuencia}.')
#ingresa una cadena, def contar palabras, luego establece el valor de palabra y fecuencia con la def palabra_mas_repetida
# luego imprime una interpolacion de las variables palabra con "" y frecuencia como int


#5.Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
# cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
# del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
# ejercicio tanto de manera iterativa como recursiva.

#funcion iterativa:
def get_int():
    """la def get_init() inicia un ciclo infinito hasta que se ingrese un valor valido, por eso delante
    del input se pone int para intentar convertir el valor a numero entero, 
    en value error captura el error y lo imprime"""
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            return num
        except ValueError:
            print("fijate bien que no es un número entero.")


#funcion recursiva:
def get_int():
    # esta funcion hace lo mismo que la anterior, solamente que no lo ejecuta dentro de un bucle infinito
    #sino que intenta convertir la entrada del usuario a int, si es exitosa retorna el valor num
    #sino ex exitosa imprime el value error y luego llama recursivamente a la def get_init()
    try:
        num = int(input("Ingrese un número entero: "))
        return num
    except ValueError:
        print("fijate bien que no es un número entero.")
        return get_int()
    

#6.Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construya los siguientes métodos para la clase:
# - Un constructor, donde los datos pueden estar vacíos. x
# -Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# -mostrar(): Muestra los datos de la persona.
# -Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:

    def __init__(self, nombre="", edad=0, dni=0):
        """constructor donde los datos estan vacios"""
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    #aqui empiezan los setters y getters para cada uno de los atributos
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena de texto")
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        if edad <= 0:
            raise ValueError("La edad debe ser un número positivo mayor a cero")
        self.edad = edad
    
    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        if not dni.isdigit() or len(dni) != 8:
            raise ValueError("El DNI debe ser un número entero de 8 dígitos sin puntos")
        self.dni = dni
    #aca terminan
    
    #funcion mostrar los datos de la persona
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")
    
    # funcion que devuelve un valor booleano sobre si es mayor de edad o no
    def es_mayor_de_edad(self):
        return self.edad >= 18
    

#7.Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
#titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad 
# es opcional. Crear los siguientes métodos para la clase:
# -Un constructor, donde los datos pueden estar vacíos.
# -Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
# directamente, sólo ingresando o retirando dinero.
# -mostrar(): Muestra los datos de la cuenta.
# -ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, 
# no se hará nada.
# -retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos


class Cuenta:
    
    def __init__(self, titular="", cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    
    def get_titular(self):
        return self.titular
    
    #setter del titular, compueba que el nombre sea un string y que no tenga espacios ni que este vacio
    def set_titular(self, titular):
        if not isinstance(titular, str):
            raise ValueError("El nombre debe ser una cadena de texto")
        elif len(titular.strip()) == 0:
            raise ValueError("el nombre no puede estar vacio")

        self.titular = titular

    #funcion para ingresar dinero
    def ingresar_dinero(self,cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad 
    
    #funcion para retirar dinero, permite al usuario hacer retiros mayores a 0 y que la cuenta quede con saldo
    #negativo dando un aviso al usuario que la cuenta esta en numeros rojos, se hace modificando un atributo privado
    # por el cual se puede acceder solamente a traves de las def retirar_dinero e ingresar_dinero
    def retirar_dinero(self, cantidad):
        if cantidad >= 0:
            raise ValueError ("la cantidad a retirar debe ser mayor a 0")
        self.__cantidad -= cantidad
        if self.__cantidad <= 0:
            print("la cuenta esta en numeros rojos")
        
    #getter de cantidad
    def get_cantidad(self):
        return self.__cantidad
    
    #funcion mostrar 
    def mostrar(self):
        print("Titular:", self.titular)
        print("Cantidad:", self.__cantidad)
           
#8.Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
# tanto por ciento. Crear los siguientes métodos para la clase:
#- Un constructor.
#- Los setters y getters para el nuevo atributo.
#-En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
# mayor de edad pero menor de 25 años y falso en caso contrario.
#-Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#-El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta
        
# clase cuenta_joven, la consigna dice que solo debo heredar Cuenta pero herede persona para poder saber si el
# individuo es mayor de edad a traves de la def get_edad, sino iba a estar dificil        
class cuenta_joven(Cuenta, Persona):
    #constructor con los datos vacion y una bonificacion de un 10%
    def __init__(self, titular="", cantidad=0, bonificacion=0.10):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    

    def set_bonificacion(self,bonificacion):
        if bonificacion <0:
            raise ValueError("la bonificacion debe ser mayor a 0")
        self.__bonificacion = bonificacion
    

    def get_bonificacion(self):
        return self.__bonificacion
    
    #def para definir si el titular es valido a traves del getter get_edad
    def es_titular_valido(self):
        return 18 <=  self.get_edad() <25
    

    #retirar dinero, la misma se hace de forma que si el titular no es valido, no lo deja retirar, se fija que la cantidad
    #a retirar sea mayor a 0 y para acceder al metodo retirar dinero de la cuenta padre hace una validacion para ver
    # si el titular es valido accede al metodo y retira y se ve reflejado en la cantidad, sino no hace nada
    def retirar_dinero(self, cantidad):
        if not self.es_titular_valido:
            raise ValueError("el titular no es valido para realizar la operacion")
        if cantidad < 0:
            raise ValueError ("La cantidad debe ser mayor a 0")
        super().retirar_dinero(cantidad) if self.es_titular_valido() else None

    #mostrar: muestra al titular, cantidad y bonificacion
    def mostrar(self):
        print("Cuenta Joven")
        print("Titular:", self.get_titular())
        print("Cantidad:", self.get_cantidad())
        print("Bonificación:", self.get_bonificacion())
     
        



