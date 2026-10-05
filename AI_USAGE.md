# AI Usage GreenFarm

## 1. Ferramentas utilizadas

Foram utilizadas ferramentas de Inteligência Artificial como apoio ao desenvolvimento do projeto:

* ChatGPT, da OpenAI;
* GitHub Copilot.

## 2. Como a IA foi utilizada

As ferramentas de IA foram utilizadas como apoio durante diferentes etapas do desenvolvimento, incluindo:

* elaboração e revisão das regras de negócio;
* identificação de partições de equivalência;
* identificação de valores de fronteira para aplicação de BVA;
* sugestão de cenários de Error Guessing;
* sugestão e revisão de casos de teste;
* auxílio na identificação de entradas inválidas;
* explicação e investigação de erros encontrados durante a execução do Pytest;
* revisão da cobertura de código e branches.

O GitHub Copilot também foi utilizado como assistente de programação durante a implementação e edição dos arquivos do projeto, para correção de identação e erros.

## 3. Auditoria

As sugestões geradas pelas ferramentas de IA não foram consideradas automaticamente corretas.

O código produzido ou sugerido foi revisado comparando seu comportamento com as regras definidas no `PRD.md`, que é a fonte de verdade do projeto.

A validação foi realizada por meio da execução da suíte de testes automatizados utilizando Pytest.

Resultado final:

* 109 testes executados;
* 109 testes aprovados;
* 0 testes falhos.

Também foi utilizada a cobertura de branches com `pytest-cov`:

```text
uv run pytest --cov=app --cov-branch --cov-report=term-missing
```

Resultado:

* cobertura de linhas: 100%;
* cobertura de branches: 100%.

## 4. Governança

O arquivo `AGENTS.md` define as regras de contexto utilizadas no projeto e estabelece que:

* o `PRD.md` é a fonte de verdade das regras de negócio;
* a IA não deve inventar ou alterar regras de negócio sem autorização;
* testes existentes não devem ser removidos para fazer a suíte passar;
* mudanças devem ser validadas por testes automatizados;
* 100% de cobertura de linhas não é considerada suficiente sem a verificação dos branches.

## 5. Responsabilidade e revisão

A utilização das ferramentas de IA teve caráter de assistência ao desenvolvimento.

As sugestões foram analisadas, adaptadas quando necessário e validadas pelo autor do projeto.

A implementação final, as decisões sobre as regras de negócio, os testes e a validação dos resultados são de responsabilidade do autor.

A auditoria final foi realizada por meio da comparação com o `PRD.md`, execução dos 109 testes e análise da cobertura de linhas e branches.
