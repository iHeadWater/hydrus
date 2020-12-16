import logging


def get_hydro_logger(log_level_param):
    logger = logging.getLogger(__name__)
    # StreamHandler
    stream_handler = logging.StreamHandler()  # console stream output
    stream_handler.setLevel(level=log_level_param)
    logger.addHandler(stream_handler)
    return logger


log_level = logging.INFO
hydro_logger = get_hydro_logger(log_level)