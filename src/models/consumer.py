import pika
import sys
sys.path.append('../')
from src.util import LogTypes
from src.models.logger import Logger
import json


class Consumer:
    def __init__(self, config, logger: Logger, credentials: pika.PlainCredentials, context):
        self.config = config
        self.queue_name = config.get('queue_name')
        self.exchange = config.get('exchange')
        self.logger = logger
        print(credentials)
        self.credentials = credentials
        self.context=context
        self.connection = self.create_connection()

    def create_connection(self):
        print(self.config)
        print(f' with {self.credentials} ')
        param = pika.ConnectionParameters(host=self.config['host'],
                                          port=self.config['port'],
                                          credentials=self.credentials,
                                          virtual_host='/',
                                          ssl_options=pika.SSLOptions(self.context))
        return pika.BlockingConnection(param)

    def on_message_callback(self, channel, method, properties, body):
        binding_key = method.routing_key
        print(f"received message for - + binding_key {binding_key}")
        parsed_body = json.loads(body)
        _type = parsed_body['type']
        if _type not in [str(_type.value) for _type in LogTypes]:
            result = self.logger.insert_error_log(_type)
            #raise Exception(f"Unkown type specified {_type}")
            print(f"Unkown type specified {_type}")
        result = self.logger.insert_log(parsed_body)
        return result

    def setup_topic(self):
        channel = self.connection.channel()
        channel.exchange_declare(exchange=self.config['exchange'],
                                 exchange_type='topic', durable=True)
        # This method creates or checks a queue
        channel.queue_declare(queue=self.queue_name, durable=True)
        # Binds the queue to the specified exchange
        channel.queue_bind(exchange=self.config['exchange'], queue=self.queue_name, routing_key=self.exchange)
        channel.basic_consume(queue=self.queue_name,
                              on_message_callback=self.on_message_callback)
        print(f'waiting for data press CTRL + C to exit')
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()

    def setup_fanout(self):
        channel = self.connection.channel()
        channel.exchange_declare(exchange=self.config['exchange'],
                                     exchange_type='fanout', durable=True)

        channel.exchange_declare(exchange=self.config['exchange'],
                             exchange_type='fanout', durable=True)
        # This method creates or checks a queue
        result = channel.queue_declare(queue='', exclusive=True)

        queue_name = result.method.queue
        print(queue_name)
        print(self.exchange)
        channel.queue_bind(exchange=self.exchange, queue=queue_name)
        # Binds the queue to the specified exchange
        channel.basic_consume(queue=queue_name,
                          on_message_callback=self.on_message_callback, auto_ack=True)
        print("afte consume")
        print(f'waiting for data press CTRL + C to exit')
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
