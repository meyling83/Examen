#funcion que calcula el area del rectangulo. 
#Por defecto el valor de la longitud de la altura es 3
def area(base,altura=3):
    return base * altura

if __name__=="__main__":
    base=float(input("Entre la longitud de la base"))
    altura=input("Entre la longitud de la altura")
    if altura=="":
        area=area(base)
    else:
        altura=float(altura)
        area=area(base,altura)
    print(f"El área del rectángulo es {area:.2f}")