calificacion = input("Introduce tu calificación del AZ-900: ")
calificacion= int(calificacion)
if calificacion < 700 :
    print("Veees, por no estudiar")
elif calificacion > 1000 :
    print("MIENTES!!! No se puede sacar más de mil")
else :
    print("Felicidades, pasa por tu certificado")


edad = input("Introduce tu edad: ")
edad= int(edad)
if edad >= 18 and edad <= 100 :
    print("Bienvenid@ al mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros")

