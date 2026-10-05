# PRD - GreenFarm

## 1. Visão geral
O GreenFarm é um sistema de regras de negócio para uma mecânica de cultivo de um jogo. O sistema permite verificar se uma determinada cultura pode ser plantada pelo jogador considerando cultura, estação, nível do jogador, quantidade de água e área disponível.

O sistema não possui interface gráfica. Seu objetivo é representar as regras de cultivo e servir como Sistema Sob Teste (SUT) para a disciplina de Qualidade e Teste de Software.

## 2. Objetivo

Implementar regras determinísticas para:

* validar culturas;
* verificar compatibilidade entre cultura e estação;
* verificar nível mínimo do jogador;
* verificar quantidade de água;
* verificar área disponível;
* determinar a condição de crescimento da plantação.

## 3. Culturas

| Cultura | Estações permitidas | Nível mínimo | Água mínima | Água máxima | Área necessária |
| ------- | ------------------- | -----------: | ----------: | ----------: | --------------: |
| tomate  | primavera, verão    |            2 |          30 |          80 |               2 |
| cenoura | outono, inverno     |            1 |          20 |          70 |               1 |
| milho   | primavera, verão    |            3 |          40 |          90 |               3 |

## 4. Regras de negócio

### RN01 — Cultura válida

A cultura informada deve ser `tomate`, `cenoura` ou `milho`.

Caso contrário, o sistema deve lançar `ValueError`.

### RN02 — Estação válida

A estação deve ser uma das seguintes:

* primavera;
* verão;
* outono;
* inverno.

Caso contrário, o sistema deve lançar `ValueError`.

### RN03 — Compatibilidade de estação

A cultura somente poderá ser plantada em uma estação compatível.

* tomate: primavera ou verão;
* cenoura: outono ou inverno;
* milho: primavera ou verão.

Caso a estação seja incompatível, o plantio deve ser rejeitado.

### RN04 — Nível mínimo

O nível do jogador deve ser maior ou igual ao nível mínimo da cultura.

Caso contrário, o plantio deve ser rejeitado.

### RN05 — Quantidade de água

A quantidade de água deve estar dentro da faixa definida para a cultura, incluindo os limites.

Valores abaixo do mínimo ou acima do máximo devem impedir o plantio.

### RN06 — Área disponível

A área disponível deve ser maior ou igual à área necessária para a cultura.

Caso a área seja insuficiente, o plantio deve ser rejeitado.

### RN07 — Fertilizante

Quando todas as condições de plantio forem atendidas:

* sem fertilizante: rendimento `normal`;
* com fertilizante e nível do jogador igual ou superior ao nível mínimo + 2: rendimento `alto`;
* com fertilizante, mas nível abaixo desse limite: rendimento `normal`.

## 5. Entradas inválidas

O sistema deve rejeitar ou lançar exceção para:

* cultura inexistente;
* estação inexistente;
* nível negativo;
* quantidade de água negativa;
* área negativa;
* valores de tipos incompatíveis com os parâmetros esperados.

## 6. Resultado

O sistema deve informar de maneira determinística se o plantio é permitido e, quando permitido, qual é o rendimento esperado.

## 7. Restrições técnicas

* Python 3.12 ou superior;
* gerenciamento do projeto com `uv`;
* testes automatizados com `pytest`;
* cobertura com `pytest-cov`;
* cobertura de branches utilizando `--cov-branch`;
* testes seguindo o padrão Arrange, Act, Assert;
* utilização de testes parametrizados;
* aplicação de Equivalence Partitioning, Boundary Value Analysis e Error Guessing.
