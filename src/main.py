from models.consumer import Consumer
from models.logger import Logger
from util import generate_mongo_uri
import os
from dotenv import load_dotenv

load_dotenv()

config = {'host': 'localhost', 'port': 5672, 'exchange': 'system-integration', 'queue_name': 'logs'}
mongo_uri = generate_mongo_uri(os.getenv("DB_NAME"), os.getenv("DB_USERNAME"), os.getenv("PASSWORD"))
logger = Logger(mongo_uri, os.getenv("DB_NAME"))
consumer = Consumer(config=config, logger=logger)

if __name__ == '__main__':
    print(os.getenv("DB_USERNAME"))
    print(mongo_uri)
    consumer.setup_fanout()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
