def procesar_pago(monto, saldo):
    if monto <= 0:
        return "Monto invalido"

    if saldo >= monto:
        return "Pago aprobado"
    else:
        return "Saldo insuficiente"


# Funcion utilizada para las pruebas de calidad
# Control automatico mediante pre-commit


def calcular_descuento(precio):
    descuento = 10
    resultado = precio - descuento
    return resultado


def verificar_usuario(nombre):
    return nombre == "admin"
