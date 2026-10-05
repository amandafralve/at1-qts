from typing import Final

CULTURAS: Final[dict[str, dict[str, object]]] = {
    "tomate": {
        "estacoes": ("primavera", "verao"),
        "nivel_minimo": 2,
        "agua_minima": 30,
        "agua_maxima": 80,
        "area": 2,
    },
    "cenoura": {
        "estacoes": ("outono", "inverno"),
        "nivel_minimo": 1,
        "agua_minima": 20,
        "agua_maxima": 70,
        "area": 1,
    },
    "milho": {
        "estacoes": ("primavera", "verao"),
        "nivel_minimo": 3,
        "agua_minima": 40,
        "agua_maxima": 90,
        "area": 3,
    },
}

ESTACOES_VALIDAS: Final[tuple[str, ...]] = (
    "primavera",
    "verao",
    "outono",
    "inverno",
)


def validar_cultura(cultura: str) -> None:
    """Verifica se a cultura existe no sistema."""
    if not isinstance(cultura, str):
        raise TypeError("A cultura deve ser uma string.")

    if cultura not in CULTURAS:
        raise ValueError(f"Cultura inválida: {cultura}")


def validar_estacao(estacao: str) -> None:
    """Verifica se a estação informada é válida."""
    if not isinstance(estacao, str):
        raise TypeError("A estação deve ser uma string.")

    if estacao not in ESTACOES_VALIDAS:
        raise ValueError(f"Estação inválida: {estacao}")


def verificar_plantio(
    cultura: str,
    estacao: str,
    nivel: int,
    agua: int,
    area: float,
) -> bool:
    """Verifica se uma cultura pode ser plantada nas condições informadas."""
    validar_cultura(cultura)
    validar_estacao(estacao)

    if isinstance(nivel, bool) or not isinstance(nivel, int):
        raise TypeError("O nível deve ser um número inteiro.")

    if isinstance(agua, bool) or not isinstance(agua, (int, float)):
        raise TypeError("A quantidade de água deve ser numérica.")

    if isinstance(area, bool) or not isinstance(area, (int, float)):
        raise TypeError("A área deve ser numérica.")

    if nivel < 0:
        raise ValueError("O nível não pode ser negativo.")

    if agua < 0:
        raise ValueError("A quantidade de água não pode ser negativa.")

    if area < 0:
        raise ValueError("A área não pode ser negativa.")

    dados = CULTURAS[cultura]
    estacoes = dados["estacoes"]
    nivel_minimo = dados["nivel_minimo"]
    agua_minima = dados["agua_minima"]
    agua_maxima = dados["agua_maxima"]
    area_necessaria = dados["area"]

    if estacao not in estacoes:
        return False

    if nivel < nivel_minimo:
        return False

    if agua < agua_minima or agua > agua_maxima:
        return False

    if area < area_necessaria:
        return False

    return True


def calcular_rendimento(
    cultura: str,
    nivel: int,
    fertilizante: bool,
) -> str:
    """Calcula o rendimento da plantação."""
    validar_cultura(cultura)

    if isinstance(nivel, bool) or not isinstance(nivel, int):
        raise TypeError("O nível deve ser um número inteiro.")

    if nivel < 0:
        raise ValueError("O nível não pode ser negativo.")

    if not isinstance(fertilizante, bool):
        raise TypeError("Fertilizante deve ser True ou False.")

    nivel_minimo = CULTURAS[cultura]["nivel_minimo"]

    if not fertilizante:
        return "normal"

    if nivel >= nivel_minimo + 2:
        return "alto"

    return "normal"

