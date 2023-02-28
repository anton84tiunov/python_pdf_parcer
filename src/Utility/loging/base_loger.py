import logging
import logging.handlers

# filemode='w'

def init_loger(name):
    """функция для инициализации loger для ведения лог файлов"""
    logger = logging.getLogger(name)
    FORMAT = 'asctime: %(asctime)s, name: %(name)s, levelname: %(levelname)s, message: %(message)s\n ------------------------------\n'
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    # fn = logging.handlers.RotatingFileHandler(filename='app_logs/pdf_editor.log')
    fn = logging.FileHandler(filename='app_logs/pdf_editor.log')
    fn.setFormatter(logging.Formatter(FORMAT))
    fn.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    logger.addHandler(fn)
    logger.debug("logger init")























