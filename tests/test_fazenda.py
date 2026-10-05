import pytest

from app.fazenda import (
    calcular_rendimento,
    validar_cultura,
    validar_estacao,
    verificar_plantio,
)


# ============================================================
# VALIDAÇÃO DE CULTURA
# EP - Partições de Equivalência
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "cultura",
    ["tomate", "cenoura", "milho"],
)
def test_cultura_valida(cultura):
    # Arrange
    cultura_informada = cultura

    # Act
    resultado = validar_cultura(cultura_informada)

    # Assert
    assert resultado is None


@pytest.mark.unit
@pytest.mark.parametrize(
    "cultura",
    ["batata", "arroz", "abobora", ""],
)
def test_cultura_invalida(cultura):
    # Arrange
    cultura_informada = cultura

    # Act / Assert
    with pytest.raises(ValueError):
        validar_cultura(cultura_informada)


# ============================================================
# ERROR GUESSING - CULTURA
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "cultura",
    [None, 123, True, [], {}],
)
def test_cultura_com_tipo_invalido(cultura):
    # Arrange
    cultura_informada = cultura

    # Act / Assert
    with pytest.raises(TypeError):
        validar_cultura(cultura_informada)


# ============================================================
# VALIDAÇÃO DE ESTAÇÃO
# EP - Partições de Equivalência
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "estacao",
    ["primavera", "verao", "outono", "inverno"],
)
def test_estacao_valida(estacao):
    # Arrange
    estacao_informada = estacao

    # Act
    resultado = validar_estacao(estacao_informada)

    # Assert
    assert resultado is None


@pytest.mark.unit
@pytest.mark.parametrize(
    "estacao",
    ["chuva", "seca", "monsoon", ""],
)
def test_estacao_invalida(estacao):
    # Arrange
    estacao_informada = estacao

    # Act / Assert
    with pytest.raises(ValueError):
        validar_estacao(estacao_informada)


# ============================================================
# ERROR GUESSING - ESTAÇÃO
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "estacao",
    [None, 123, True, [], {}],
)
def test_estacao_com_tipo_invalido(estacao):
    # Arrange
    estacao_informada = estacao

    # Act / Assert
    with pytest.raises(TypeError):
        validar_estacao(estacao_informada)


# ============================================================
# VERIFICAÇÃO DE PLANTIO
# EP - Partições de Equivalência
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "cultura, estacao, nivel, agua, area",
    [
        ("tomate", "primavera", 2, 50, 2),
        ("tomate", "verao", 4, 60, 3),
        ("cenoura", "outono", 1, 40, 1),
        ("cenoura", "inverno", 3, 50, 2),
        ("milho", "primavera", 3, 60, 3),
        ("milho", "verao", 5, 80, 4),
    ],
)
def test_plantio_valido(cultura, estacao, nivel, agua, area):
    # Arrange
    dados = (cultura, estacao, nivel, agua, area)

    # Act
    resultado = verificar_plantio(*dados)

    # Assert
    assert resultado is True


# ============================================================
# BVA - LIMITE INFERIOR DA ÁGUA
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "cultura, estacao, agua, esperado",
    [
        ("tomate", "primavera", 29, False),
        ("tomate", "primavera", 30, True),
        ("tomate", "primavera", 31, True),
        ("cenoura", "outono", 19, False),
        ("cenoura", "outono", 20, True),
        ("cenoura", "outono", 21, True),
        ("milho", "primavera", 39, False),
        ("milho", "primavera", 40, True),
        ("milho", "primavera", 41, True),
    ],
)
def test_limite_inferior_da_agua(cultura, estacao, agua, esperado):
    # Arrange
    nivel = 10
    area = 10

    # Act
    resultado = verificar_plantio(
        cultura,
        estacao,
        nivel,
        agua,
        area,
    )

    # Assert
    assert resultado is esperado


# ============================================================
# BVA - LIMITE SUPERIOR DA ÁGUA
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "cultura, estacao, agua, esperado",
    [
        ("tomate", "primavera", 79, True),
        ("tomate", "primavera", 80, True),
        ("tomate", "primavera", 81, False),
        ("cenoura", "outono", 69, True),
        ("cenoura", "outono", 70, True),
        ("cenoura", "outono", 71, False),
        ("milho", "primavera", 89, True),
        ("milho", "primavera", 90, True),
        ("milho", "primavera", 91, False),
    ],
)
def test_limite_superior_da_agua(cultura, estacao, agua, esperado):
    # Arrange
    nivel = 10
    area = 10

    # Act
    resultado = verificar_plantio(
        cultura,
        estacao,
        nivel,
        agua,
        area,
    )

    # Assert
    assert resultado is esperado


# ============================================================
# BVA - NÍVEL MÍNIMO
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "cultura, nivel, esperado",
    [
        ("tomate", 1, False),
        ("tomate", 2, True),
        ("tomate", 3, True),
        ("cenoura", 0, False),
        ("cenoura", 1, True),
        ("cenoura", 2, True),
        ("milho", 2, False),
        ("milho", 3, True),
        ("milho", 4, True),
    ],
)
def test_nivel_minimo(cultura, nivel, esperado):
    # Arrange
    dados = {
        "tomate": ("primavera", 50, 2),
        "cenoura": ("outono", 40, 1),
        "milho": ("primavera", 60, 3),
    }
    estacao, agua, area = dados[cultura]

    # Act
    resultado = verificar_plantio(
        cultura,
        estacao,
        nivel,
        agua,
        area,
    )

    # Assert
    assert resultado is esperado


# ============================================================
# BVA - ÁREA NECESSÁRIA
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "cultura, area, esperado",
    [
        ("tomate", 1.9, False),
        ("tomate", 2, True),
        ("tomate", 2.1, True),
        ("cenoura", 0.9, False),
        ("cenoura", 1, True),
        ("cenoura", 1.1, True),
        ("milho", 2.9, False),
        ("milho", 3, True),
        ("milho", 3.1, True),
    ],
)
def test_area_necessaria(cultura, area, esperado):
    # Arrange
    dados = {
        "tomate": ("primavera", 50, 2),
        "cenoura": ("outono", 40, 1),
        "milho": ("primavera", 60, 3),
    }
    estacao, agua, nivel = dados[cultura]

    # Act
    resultado = verificar_plantio(
        cultura,
        estacao,
        nivel,
        agua,
        area,
    )

    # Assert
    assert resultado is esperado


# ============================================================
# REGRAS DE ESTAÇÃO
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "cultura, estacao",
    [
        ("tomate", "inverno"),
        ("tomate", "outono"),
        ("cenoura", "primavera"),
        ("cenoura", "verao"),
        ("milho", "outono"),
        ("milho", "inverno"),
    ],
)
def test_cultura_em_estacao_incompativel(cultura, estacao):
    # Arrange
    nivel = 10
    agua = 50
    area = 10

    # Act
    resultado = verificar_plantio(
        cultura,
        estacao,
        nivel,
        agua,
        area,
    )

    # Assert
    assert resultado is False


# ============================================================
# ERROR GUESSING - PLANTIO
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "nivel",
    [-1, -10],
)
def test_nivel_negativo(nivel):
    # Arrange
    dados = ("tomate", "primavera", nivel, 50, 2)

    # Act / Assert
    with pytest.raises(ValueError):
        verificar_plantio(*dados)


@pytest.mark.unit
@pytest.mark.parametrize(
    "agua",
    [-1, -10],
)
def test_agua_negativa(agua):
    # Arrange
    dados = ("tomate", "primavera", 2, agua, 2)

    # Act / Assert
    with pytest.raises(ValueError):
        verificar_plantio(*dados)


@pytest.mark.unit
@pytest.mark.parametrize(
    "area",
    [-1, -10],
)
def test_area_negativa(area):
    # Arrange
    dados = ("tomate", "primavera", 2, 50, area)

    # Act / Assert
    with pytest.raises(ValueError):
        verificar_plantio(*dados)


@pytest.mark.unit
@pytest.mark.parametrize(
    "nivel",
    [None, "2", 2.5, True],
)
def test_nivel_com_tipo_invalido(nivel):
    # Arrange
    dados = ("tomate", "primavera", nivel, 50, 2)

    # Act / Assert
    with pytest.raises(TypeError):
        verificar_plantio(*dados)


@pytest.mark.unit
@pytest.mark.parametrize(
    "agua",
    [None, "50", [], {}],
)
def test_agua_com_tipo_invalido(agua):
    # Arrange
    dados = ("tomate", "primavera", 2, agua, 2)

    # Act / Assert
    with pytest.raises(TypeError):
        verificar_plantio(*dados)


@pytest.mark.unit
@pytest.mark.parametrize(
    "area",
    [None, "2", [], {}],
)
def test_area_com_tipo_invalido(area):
    # Arrange
    dados = ("tomate", "primavera", 2, 50, area)

    # Act / Assert
    with pytest.raises(TypeError):
        verificar_plantio(*dados)


# ============================================================
# RENDIMENTO
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "cultura, nivel, fertilizante, esperado",
    [
        ("tomate", 2, False, "normal"),
        ("tomate", 2, True, "normal"),
        ("tomate", 4, True, "alto"),
        ("cenoura", 1, False, "normal"),
        ("cenoura", 3, True, "alto"),
        ("milho", 3, True, "normal"),
        ("milho", 5, True, "alto"),
    ],
)
def test_calcular_rendimento(cultura, nivel, fertilizante, esperado):
    # Arrange
    dados = (cultura, nivel, fertilizante)

    # Act
    resultado = calcular_rendimento(*dados)

    # Assert
    assert resultado == esperado


# ============================================================
# ERROR GUESSING - RENDIMENTO
# ============================================================


@pytest.mark.unit
@pytest.mark.parametrize(
    "nivel",
    [-1, -5],
)
def test_rendimento_com_nivel_negativo(nivel):
    # Arrange
    dados = ("tomate", nivel, True)

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_rendimento(*dados)


@pytest.mark.unit
@pytest.mark.parametrize(
    "nivel",
    [None, "2", 2.5, True],
)
def test_rendimento_com_nivel_invalido(nivel):
    # Arrange
    dados = ("tomate", nivel, True)

    # Act / Assert
    with pytest.raises(TypeError):
        calcular_rendimento(*dados)


@pytest.mark.unit
@pytest.mark.parametrize(
    "fertilizante",
    [None, "sim", 1, 0, []],
)
def test_rendimento_com_fertilizante_invalido(fertilizante):
    # Arrange
    dados = ("tomate", 4, fertilizante)

    # Act / Assert
    with pytest.raises(TypeError):
        calcular_rendimento(*dados)


