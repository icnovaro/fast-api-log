from fastapi import FastAPI
from logging.config import dictConfig
import logging
from .config import LogConfig

app = FastAPI()

dictConfig(LogConfig().dict())
logger = logging.getLogger("mycoolapp")

@app.get("/")
def read_root():
    logger.info("SRE estuvo aquí")
    logger.error("Dummy Error")
    logger.debug("Dummy Debug")
    logger.warning("Dummy Warning")
    return {"Hello": "World"}


