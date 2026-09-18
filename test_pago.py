from pago import calcular_descuento, procesar_pago, verificar_usuario


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


def test_calcular_descuento():
    assert calcular_descuento(100) == 90


def test_verificar_usuario_admin():
    assert verificar_usuario("admin") is True


def test_verificar_usuario_no_admin():
    assert verificar_usuario("luciano") is False
