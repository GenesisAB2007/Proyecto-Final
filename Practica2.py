examenes =int(input("Digite la cantidad de exámenes realizados: "))
if examenes >3:
    print ("Cantidad de exámenes inválido.")
else:
    num1 = int(input("Digite la nota obtenida del primer exámen: "))
    num2 = int(input("Digite la nota obtenida del segundo exámen: "))
    num3 = int(input("Digite la nota obtenida del tercer exámen: "))
    
    suma_notas = num1+num2+num3
    promedio = suma_notas/3
    
    print("Su nota final es: ", promedio)
    if promedio>=70:
        print ("El estudiante aprobó.")
    elif promedio<70 and promedio>=60:
        print ("El estudiante debe hacer ampliación.")
    elif promedio<60:
        print ("El estudiante reprobó.")