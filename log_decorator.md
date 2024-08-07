# Decoradores em Python

Este documento fornece uma introdução sobre como usar decoradores em Python. Decoradores são uma poderosa funcionalidade da linguagem que permitem modificar o comportamento de funções ou métodos de forma declarativa.

## O que são Decoradores?

Decoradores em Python são funções que recebem outra função como argumento e retornam uma nova função modificada. Eles são comumente usados para adicionar funcionalidades extras a funções existentes sem modificar seu código diretamente.

* Exemplos práticos de decorators  
    * [Tenacity Decorator](https://github.com/Jownao/bootcamps_study/blob/main/01_bootcamp_python/009aula/decorator_tenacity.py)
    * [Singleton Decorator](https://github.com/Jownao/bootcamps_study/blob/main/01_bootcamp_python/009aula/decorator_singleton.py)

## Exemplo Básico de Decorador

Aqui está um exemplo simples de um decorador que adiciona logging a uma função:

```python
import functools
from loguru import logger

# Definindo um decorador
def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função: {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Função {func.__name__} concluída")
        return result
    return wrapper

# Aplicando o decorador a uma função
@log_function
def minha_funcao(x, y):
    return x + y

# Exemplo de uso da função decorada
resultado = minha_funcao(3, 5)
print(f"Resultado da função: {resultado}")
```

Neste exemplo:
- `log_function` é um decorador que registra mensagens de log antes e depois da execução da função decorada.
- `@log_function` aplica o decorador `log_function` à função `minha_funcao`.

## Como Funciona um Decorador?

- Um decorador é uma função que envolve outra função.
- Ele pode executar código antes e depois da chamada da função original.
- Ele pode modificar os argumentos passados para a função original.
- Pode também modificar o valor de retorno da função original.

## Benefícios dos Decoradores

- **Reutilização de código**: Permitem adicionar funcionalidades a múltiplas funções sem duplicação de código.
- **Separação de preocupações**: Permite separar a lógica principal da função de funcionalidades adicionais (como logging, validação, etc.).
- **Legibilidade**: Facilita a leitura do código ao manter a lógica principal da função clara e direta.

## Considerações Finais

Decoradores são uma ferramenta poderosa em Python para melhorar a modularidade, reusabilidade e legibilidade do código. Eles são amplamente utilizados em frameworks web, logging, caching, e muito mais.

