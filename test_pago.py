from pago import procesar_pago


def test_pago_aprobado():
    # Arrange
    monto = 500
    saldo = 1000

    # Act
    resultado = procesar_pago(monto, saldo)

    # Assert
    assert resultado == "Pago aprobado"


def test_saldo_insuficiente():
    # Arrange
    monto = 1500
    saldo = 1000

    # Act
    resultado = procesar_pago(monto, saldo)

    # Assert
    assert resultado == "Saldo insuficiente"


def test_monto_invalido():
    # Arrange
    monto = 0
    saldo = 1000

    # Act
    resultado = procesar_pago(monto, saldo)

    # Assert
    assert resultado == "Monto invalido"
