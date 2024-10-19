from abc import ABC, abstractmethod

class Snapshot(ABC):
    @abstractmethod
    def get_average_duration(self):
        pass

    @abstractmethod
    def get_total_duration(self):
        pass

    @abstractmethod
    def get_total_number_of_slow_calls(self):
        pass

    @abstractmethod
    def get_number_of_slow_successful_calls(self):
        pass

    @abstractmethod
    def get_number_of_slow_failed_calls(self):
        pass

    @abstractmethod
    def get_slow_call_rate(self):
        pass

    @abstractmethod
    def get_number_of_successful_calls(self):
        pass

    @abstractmethod
    def get_number_of_failed_calls(self):
        pass

    @abstractmethod
    def get_total_number_of_calls(self):
        pass

    @abstractmethod
    def get_failure_rate(self):
        pass