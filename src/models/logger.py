from pymongo import MongoClient


class Log:
    def __init__(self, type, timestamp, message):
        self.type = type
        self.timestamp = timestamp
        self.message = message


class Logger:

    def __init__(self, connection_str: str, db_name: str):
        self.client = MongoClient(connection_str)
        self.db = self.client[db_name]

    def insert_log(self, content: dict):
        logs = self.db.logs
        result = logs.insert_one(content)
        print(result)
        return result

    def insert_error_log(self, _type):
        logs = self.db.logs
        log = {
            'message': f'Unknown type specified {_type}',
            'type': 'ERROR'
        }
        result = logs.insert_one(log)
        return result