# GreenFarm

Sistema de regras de negócio para uma mecânica de cultivo de um jogo, desenvolvido para a disciplina de Qualidade e Teste de Software (QTS).

O projeto implementa regras determinísticas para verificar condições de plantio e calcular o rendimento de culturas.

## Tecnologias

* Python 3.14
* uv
* Pytest
* pytest-cov

## Estrutura

```text
at1-qts/
├── app/
│   ├── __init__.py
│   └── fazenda.py
├── tests/
│   └── test_fazenda.py
├── AGENTS.md
├── AI_USAGE.md
├── PRD.md
├── README.md
├── main.py
├── pyproject.toml
└── uv.lock
```

## Instalação

É necessário ter Python 3.12 ou superior e o `uv` instalado.

Para instalar as dependências do projeto:

```bash
uv sync
```

## Executar os testes

Para executar a suíte completa:

```bash
uv run pytest -v
```

A suíte contém 109 cenários de teste.

## Cobertura de código

Para executar os testes com cobertura de linhas e branches:

```bash
uv run pytest --cov=app --cov-branch --cov-report=term-missing
```

Resultado esperado:

```text
100% de cobertura de linhas
100% de cobertura de branches
```

## Técnicas de teste utilizadas

A suíte utiliza:

* Arrange, Act, Assert (AAA);
* `@pytest.mark.parametrize`;
* Particionamento de Equivalência (EP);
* Análise do Valor Limite (BVA);
* Error Guessing;
* cobertura de código e branches com `pytest-cov`.

## Governança de IA

O arquivo `AGENTS.md` define as regras de contexto e as restrições para utilização de IA no projeto.

O arquivo `AI_USAGE.md` documenta como a IA foi utilizada e como as sugestões foram auditadas.

## Especificação

As regras de negócio do sistema estão documentadas no arquivo `PRD.md`.
