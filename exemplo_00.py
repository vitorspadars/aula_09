from loguru import logger

logger.add("meu_log.log")

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