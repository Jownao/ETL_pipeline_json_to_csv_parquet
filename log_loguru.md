# Logging com Loguru

Este documento fornece uma introdução sobre como usar a biblioteca `loguru` para logging em Python. O `loguru` é uma biblioteca poderosa e fácil de usar para gerenciamento de logs.

## Instalação

Para instalar a biblioteca `loguru`, você pode usar o `pip`:

```bash
pip install loguru
```

## Configuração Básica

Aqui está um exemplo de como configurar o `loguru` para salvar logs em um arquivo e imprimir logs no console:

```python
from loguru import logger
import sys

# Configurar logger para salvar logs em um arquivo
logger.add(
    "meu_arquivo_de_logs.log",
    format="{time}|{level}|{message}|{file}",
    level="INFO"
)

# Configurar logger para imprimir logs no console
logger.add(
    sink=sys.stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

# Exemplo de uso do logger
logger.debug("Isso é um debug message")
logger.info("Isso é um info message")
logger.warning("Isso é um warning message")
logger.error("Isso é um error message")
logger.critical("Isso é um critical message")
```

## Parâmetros do Logger

### Arquivo de Logs

```python
logger.add("meu_arquivo_de_logs.log", ...)
```
Este parâmetro especifica o caminho do arquivo onde os logs serão salvos.

### Formato

```python
format="{time}|{level}|{message}|{file}"
```
O parâmetro `format` define o formato dos logs que serão escritos no arquivo. No exemplo, o formato inclui:
- `{time}`: Timestamp do log.
- `{level}`: Nível do log (por exemplo, INFO, ERROR).
- `{message}`: Mensagem do log.
- `{file}`: Nome do arquivo onde o log foi gerado.

### Nível

```python
level="INFO"
```
O parâmetro `level` define o nível mínimo de severidade dos logs que serão registrados. No caso, o nível é `INFO`, o que significa que apenas logs com nível `INFO` ou superior (como `WARNING`, `ERROR`, `CRITICAL`) serão salvos. Logs de níveis inferiores (como `DEBUG`) serão ignorados.

### Sink

```python
sink=sys.stderr
```
O parâmetro `sink` especifica para onde os logs devem ser direcionados. No exemplo, `stderr` é usado como o sink, que é a saída de erro padrão do sistema (geralmente o console).

## Exemplo Completo

Aqui está um exemplo completo combinando todas as configurações mencionadas:

```python
from loguru import logger
import sys

# Configurar logger para salvar logs em um arquivo
logger.add(
    "meu_arquivo_de_logs.log",
    format="{time}|{level}|{message}|{file}",
    level="INFO"
)

# Configurar logger para imprimir logs no console
logger.add(
    sink=sys.stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

# Exemplo de uso do logger
logger.debug("Isso é um debug message")
logger.info("Isso é um info message")
logger.warning("Isso é um warning message")
logger.error("Isso é um error message")
logger.critical("Isso é um critical message")
```

## Referências

- [Documentação oficial do Loguru](https://loguru.readthedocs.io/en/stable/)
- [Repositório do Loguru no GitHub](https://github.com/Delgan/loguru)

Este README fornece uma introdução básica ao `loguru` e deve ajudá-lo a começar a usar a biblioteca para logging em seus projetos Python.

