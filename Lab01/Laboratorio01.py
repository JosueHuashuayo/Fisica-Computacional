import math
# Funcion de la primera ecuacion, permite hallar cualquiera de los tres valores buscados 
def calcularMRU(variable, v=None, t=None, x=None):
    if (t == 0 or v == 0) :
        return None
    else:
        match variable:
            case 'x':
                return v * t
            case 'v':
                return x / t
            case 't':
                return x / v    
            case _:
                return None

# Funcion de la segunda ecuacion       
def calcularMRUV1(variable, Vi=None, a=None, t=None, x=None):
    if t == 0 :
        return None
    else:
        match variable:
            case 'x':
                return (Vi * t) + (a * t**2)/2
            case 'Vi':
                return (x/t) - (a*t)/2
            case 't':
                t1 = (-Vi + math.sqrt(Vi**2 + 4*a*x)) / (2*a)
                t2 = (-Vi - math.sqrt(Vi**2 + 4*a*x)) / (2*a)
                return (t1,t2)
            case 'a':
                return 2 * (x - Vi*t) / t**2
            case _:
                return None

# Funcion de la tercera ecuacion         
def calcularMRUV2(opc1, vi=None, a=None, t=None, vf=None):
    if (t == 0 or a == 0):
        return None
    else:
         match opc1:
            case "vi":
                return (vf - a*t)
            case "a":
                return (vf - vi)/t
            case "t":
                return (vf - vi)/a
            case "vf":
                return (vi + a*t)
            case _:
                return None
def main():
    while True:
        print("MENU: ")
        print("1: ∆x = v × ∆t")
        print("2: ∆x = Vi∆t + (α∆t^2)/2")
        print("3: Vf = Vi∆t + α∆t")
        print("4: Salir")
        
        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                print("∆x = v × ∆t")
                opc1 = input("Seleccione x(distancia), v(velocidad), t(tiempo) segun lo que desee hallar: ")
                match opc1:
                    case "x":
                        v = (float)(input("Ingrese velocidad: "))
                        t = (float)(input("Ingrese tiempo: "))
                        print("La distancia es: ", calcularMRU(opc1,v,t,None))
                    case "v":
                        x = (float)(input("Ingrese distancia: "))
                        t = (float)(input("Ingrese tiempo: "))
                        print("La distancia es: ", calcularMRU(opc1,None,t,x))
                    case "t":
                        x = (float)(input("Ingrese distancia: "))
                        v = (float)(input("Ingrese velocidad: "))
                        print("La distancia es: ", calcularMRU(opc1,v,None,x))
            case "2": 
                print("∆x = Vi∆t + (α∆t^2)/2")
                opc1 = input("Seleccione x(distancia), Vi(velocidad inicial), a aceleracion , t(tiempo) segun lo que desee hallar: ")
                match opc1:
                        case "x":
                            vi = (float)(input("Ingrese velocidad inicial: "))
                            a = (float)(input("Ingrese aceleracion: "))
                            t = (float)(input("Ingrese tiempo: "))
                            print("La distancia es: ", calcularMRUV1(opc1, vi, a, t, None))
                        case "Vi":
                            t = (float)(input("Ingrese tiempo: "))    
                            a = (float)(input("Ingrese aceleracion: "))
                            x = (float)(input("Ingrese distancia: "))
                            print("La velocidad inicial es: ", calcularMRUV1(opc1, None, a, t, x))
                        case "t":
                            vi = (float)(input("Ingrese velocidad inicial: "))
                            a = (float)(input("Ingrese aceleracion: "))
                            x = (float)(input("Ingrese distancia: "))
                            print("El tiempo es: ", calcularMRUV1(opc1, vi, a, None, x))
                        case "a":
                            vi = (float)(input("Ingrese velocidad inicial: "))
                            x = (float)(input("Ingrese distancia: "))
                            t = (float)(input("Ingrese tiempo: "))
                            print("La aceleracion es: ", calcularMRUV1(opc1, vi, None, t, x))
            case "3":
                print("Vf = Vi∆t + α∆t")
                opc1 = input("Seleccione vf(velocidad final), Vi(velocidad inicial), a(aceleración), t(tiempo) segun lo que desee hallar: ")
                match opc1:
                    case "vf":
                        vi = (float)(input("Ingrese velocidad inicial: "))
                        a = (float)(input("Ingrese aceleración: "))
                        t = (float)(input("Ingrese tiempo: "))
                        print("La velocidad final es: ", calcularMRUV2(opc1, vi, a, t, None))
                    case "Vi":
                        vf = (float)(input("Ingrese velocidad final: "))
                        a = (float)(input("Ingrese aceleración: "))
                        t = (float)(input("Ingrese tiempo: "))
                        print("La velocidad inicial es: ", calcularMRUV2(opc1, None, a, t, vf))
                    case "a":
                        vi = (float)(input("Ingrese velocidad inicial: "))
                        vf = (float)(input("Ingrese velocidad final: "))
                        t = (float)(input("Ingrese tiempo: "))
                        print("La aceleración es: ", calcularMRUV2(opc1, vi, None, t, vf))
                    case "t":
                        vi = (float)(input("Ingrese velocidad inicial: "))
                        vf = (float)(input("Ingrese velocidad final: "))
                        a = (float)(input("Ingrese aceleración: "))
                        print("El tiempo es: ", calcularMRUV2(opc1, vi, a, None, vf))
            case "4":
                break
            case _:
                print("Opcion no valida")

main()
        
                    
     
                    
     