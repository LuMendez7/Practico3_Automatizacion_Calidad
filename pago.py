def procesar_pago(monto, saldo):
    if monto <= 0:
        return "Monto invalido"

    if saldo >= monto:
        return "Pago aprobado"
    else:
        return "Saldo insuficiente"

# Funcion utilizada para las pruebas de calidad