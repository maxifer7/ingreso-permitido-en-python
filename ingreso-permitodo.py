# Paso 1: Solicitar al user que ingrese la edad del cliente

edad = int(input("Por favor, ingresa tu edad: "))


# Paso 2: Verificar si la edad ingresada cumple con el requisito para el ingreso

# permitido = True
# if edad >= 18:
#     permitido = True
# else:
#     permitido = False

permitido = True if edad >= 18 else False # Esto es lo mismo que lo de arriba pero ternario, más simple

# Paso 3: Mostrar al user si su cliente puede o no ingresar a la discoteca

if permitido:
    print("Puedes ingresar a la discoteca!!")
else:
    print("Lo sentimos mucho, no se puede ingresar a la discoteca siendo menor de edad.")