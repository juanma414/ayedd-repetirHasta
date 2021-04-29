max=0
contCheque=0
verif=str("inicio")
saldo=float(input("Buen día, ingrese el saldo en caja "))
cod=str(input("ingrese C para compra o V para venta "))
while cod!="F":
    while verif!="Correcto":
        cod=str(input("Código no válido, ingrese C o V "))
        if cod!="C":
            if cod!="V":
                verif="Incorrecto"
            else:
                verif="Correcto"
        else:
            verif="Correcto"
        
    if cod=="C":
        importe=float(input("Por favor ingrese el importe de la compra : "))
        if saldo-importe>=0:
            saldo=saldo-importe
        else:
            print("Emitir un cheque por el valor de ",importe-saldo)
            contCheque=contCheque+1
    else:
        importe=float(input("Por favor ingrese el importede la venta : "))
        saldo=saldo+importe
        if importe>max:
            max=importe
    cod=str(input("ingrese C para compra o V para venta "))
print("El saldo final de la caja es ",saldo)
print("La cantidad de cheques emitidos fueron ", contCheque)
print("El valor de la venta máxima es ",max)