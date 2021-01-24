import pika
import json
from util import LogTypes
from datetime import datetime
import os
import ssl
from dotenv import load_dotenv

load_dotenv()
def produce():
    credentials = pika.PlainCredentials(os.getenv("DB_USERNAME"), os.getenv("PASSWORD"))
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    config = {'host': 'b-6cdeb3fd-c4a0-432f-b393-287562fabdcb.mq.us-east-2.amazonaws.com', 'port': 5671,
              'exchange': 'system-integration', 'queue_name': 'logs'}
    param = pika.ConnectionParameters(host=config['host'],
                                      port=config['port'],
                                      credentials=credentials,
                                      virtual_host='/',
                                      ssl_options=pika.SSLOptions(context))
    connection = pika.BlockingConnection(param)
    channel = connection.channel()
    date = datetime.now().isoformat()
    payload = json.dumps({'type': str(LogTypes.CAR_RENTAL.value), 'content': {'car_id': 1, 'user_id': 4, 'reservation_id': 12, 'timestamp': date}})
    channel.basic_publish(exchange='system-integration',
                          routing_key='logs',
                          body=payload)


if __name__ == '__main__':
    produce()