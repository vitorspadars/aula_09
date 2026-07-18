from loguru import logger
from sys import stderr

logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO"
            )

# logger.add(
#                 "meu_arquivo_de_logs.log",
#                 format = "{time} {level} {message} {file}",
#                 level="INFO"
#             )

logger.add(
                "meu_log_critical.log",
                format = "{time} {level} {message} {file}",
                level='CRITICAL')

def soma (x,y):
    try:
        soma = x + y
        logger.info(f"você digitou valores corretos {soma}")
        return soma
    except:
        logger.critical("você tem que digitar valores corretos")


soma(2,5)
soma(4,6)
soma(4,"3")