import logging


def logger():

    import logging

    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename="debug.log", level=logging.DEBUG,
                        format=LOG_FORMAT, filemode='w')
    logger = logging.getLogger()
    logger.debug('hi')
