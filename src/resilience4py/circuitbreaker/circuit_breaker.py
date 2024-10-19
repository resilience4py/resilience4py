from abc import ABC
from enum import Enum
from functools import wraps

class State(Enum):
    CLOSED = 0
    OPEN = 1
    HALF_OPEN = 2
    DISABLED = 3
    FORCED_OPEN = 4
    METRICS_ONLY = 5

class CircuitBreaker(ABC):
    def __init__(self):
        pass

    @staticmethod
    def decorate_function(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                raise e

