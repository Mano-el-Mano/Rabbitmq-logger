import enum


def generate_mongo_uri(db_name: str, username: str, password: str):
    return f'mongodb+srv://{username}:{password}@car-review-cluster.szjxc.mongodb.net/{db_name}?retryWrites=true&w=majority'


class LogTypes(enum.Enum):
    CAR_RENTAL = "CAR_RENTAL"
    PROXY_SERVER = "PROXY_SERVER",
    CAR_REVIEW = "CAR_REVIEW"
