# Regras de contexto GreenFarm

## Objetivo

Este projeto é um trabalho acadêmico da disciplina Qualidade e Teste de Software. O objetivo é desenvolver e testar um sistema determinístico de regras de negócio para uma fazenda de um jogo.

## Fonte de verdade

O arquivo `PRD.md` é a fonte de verdade das regras de negócio.

As regras implementadas em `app/` devem estar de acordo com o PRD.

## Uso de IA

A IA pode auxiliar em:

* elaboração e revisão de testes;
* identificação de partições de equivalência;
* identificação de valores de fronteira;
* identificação de entradas para Error Guessing;
* revisão de cobertura de código;
* sugestões de melhoria na organização dos testes;
* explicação de erros encontrados durante a execução.

## Restrições

A IA não deve:

* inventar regras de negócio que não estejam no PRD;
* alterar regras do PRD sem autorização;
* remover testes existentes;
* adicionar dependências sem necessidade;
* modificar o comportamento da aplicação apenas para fazer os testes passarem;
* considerar 100% de cobertura de linhas como suficiente quando houver branches não testados.

## Testes

Os testes devem:

* utilizar pytest;
* seguir Arrange, Act, Assert;
* utilizar `@pytest.mark.parametrize` quando houver cenários semelhantes;
* utilizar técnicas de Equivalence Partitioning;
* utilizar Boundary Value Analysis;
* utilizar Error Guessing;
* verificar resultados e exceções esperadas;
* buscar 100% de cobertura de linhas e branches das regras de negócio.

## Auditoria

Todo código gerado ou sugerido por IA deve ser revisado comparando-se com o `PRD.md` e validado pela execução da suíte de testes e pela análise de cobertura.
