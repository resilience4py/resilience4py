from abc import ABC, abstractmethod

from src.resilience4py.metrics.metrics import Outcome

class AbstractAggregation(ABC):

    def __init__(self):
        self.number_of_slow_failed_calls = 0
        self.number_of_slow_calls = 0
        self.number_of_failed_calls = 0
        self.total_duration_in_millis = 0
        self.number_of_calls = 0

    @abstractmethod
    def record(self, duration:int, outcome:Outcome)->None:
        self.number_of_calls+=1
        self.total_duration_in_millis+=duration
        match outcome:
            case(Outcome.ERROR):
                self.number_of_failed_calls+=1
            case(Outcome.SLOW_ERROR):
                self.number_of_slow_calls+=1
                self.number_of_failed_calls+=1
                self.number_of_slow_failed_calls+=1
            case(Outcome.SLOW_SUCCESS):
                self.number_of_slow_calls+=1
            case _:
                raise ValueError(f'Undefined outcome value {outcome}')
