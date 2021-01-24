import pika
import json
from util import LogTypes
def produce():
    connection = pika.BlockingConnection()

    channel = connection.channel()

    payload = json.dumps({'type': str(LogTypes.CAR_RENTAL.value), 'content': {'car_id': 1, 'user_id': 4, 'reservation_id': 12}})
    channel.basic_publish(exchange='system-integration',
                          routing_key='logs',
                          body=payload)


if __name__ == '__main__':
    produce()