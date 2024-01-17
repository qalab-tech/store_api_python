from loguru import logger

logger.add('logs/application.log', format='{time:DD-MM-YY HH:mm:ss} - {level} - {message}', level='INFO', rotation='1 week', compression='zip')