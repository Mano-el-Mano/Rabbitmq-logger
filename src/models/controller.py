import logging


class CallbackController:

    def __init__(self, keys: list, log_config: dict):
        self.keys = keys
        logging.basicConfig(
            filename=log_config['filename'],
            filemode='a',
            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
            datefmt='%H:%M:%S',
            level=logging.INFO)
        self.__cache = list()

    @property
    def cache(self):
        return self.__cache

    @cache.setter
    def cache(self, value):
        self.cache.append(value)


    def handle(self, key: str, body: dict):
        print(f' {key}key')
        if key not in self.keys:
            return False

        if key == 'loans':
            self.handle_loans(body),
        elif key =='autumn_offers':
            self.handle_autumn_offers(body)
