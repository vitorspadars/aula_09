from loguru import logger

logger.debug("um aviso para o desenvolvedor (ou eu mesmo) no futuro")
logger.info("informação do processo")
logger.warning("um aviso que algo vai parar de funcionar no futuro")
logger.error("aconteceu uma falha")
logger.critical("aconteceu um erro que aborta a aplicação")