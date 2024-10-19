from resilience4py.circuitbreaker.circuit_breaker import CircuitBreaker
from resilience4py.circuitbreaker.circuit_breaker_config import CircuitBreakerConfig


class CircuitBreakerStateMachine(CircuitBreaker):
    def __init__(self, name:str, config:CircuitBreakerConfig):
        self.name = name
        self.config = config