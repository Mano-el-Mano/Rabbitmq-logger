from models.consumer import Consumer
from models.logger import Logger
from util import generate_mongo_uri
import os
from dotenv import load_dotenv
import pika
import ssl
load_dotenv()
credentials = pika.PlainCredentials(os.getenv("DB_USERNAME"), os.getenv("PASSWORD"))
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
config = {'host': 'b-6cdeb3fd-c4a0-432f-b393-287562fabdcb.mq.us-east-2.amazonaws.com', 'port': 5671, 'exchange': 'system-integration', 'queue_name': 'logs'}
mongo_uri = generate_mongo_uri(os.getenv("DB_NAME"), os.getenv("DB_USERNAME"), os.getenv("PASSWORD"))
logger = Logger(mongo_uri, os.getenv("DB_NAME"))

consumer = Consumer(config=config, logger=logger, credentials=credentials, context=context)
if __name__ == '__main__':
    print(os.getenv("DB_USERNAME"))
    print(mongo_uri)

    consumer.setup_fanout()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
