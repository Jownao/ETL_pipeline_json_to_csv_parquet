from loguru import logger
from sys import stderr
from functools import wraps
import pandas as pd

logger.remove()

logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(
    "meu_arquivo_de_logs.log",
    format="{time}|{level}|{message}|{file}",
    level="INFO"
)

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}'")
        if args or kwargs:
            logger.info(f"Argumentos: {[(type(arg).__name__, arg.shape if isinstance(arg, pd.DataFrame) else arg) for arg in args]} "
                        f"{[(k, (type(v).__name__, v.shape) if isinstance(v, pd.DataFrame) else v) for k, v in kwargs.items()]}")
        try:
            result = func(*args, **kwargs)
            if isinstance(result, pd.DataFrame):
                logger.info(f"Função '{func.__name__}' retornou um DataFrame com dimensões {result.shape}")
            elif result is not None:
                logger.info(f"Função '{func.__name__}' retornou {result}")

            # Adiciona mensagem de sucesso
            logger.info(f"Função '{func.__name__}' executada com sucesso")
            
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            #raise
    return wrapper
