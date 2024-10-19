from resilience4py.circuitbreaker.circuit_breaker import CircuitBreaker


class CircuitBreakerUtil:
    @staticmethod
    def is_call_permitted(circuit_breaker:CircuitBreaker):
        return circuit_breaker.state == State.CLOSED or circuit_breaker.state == State.HALF_OPEN or circuit_breaker.state == State.DISABLED or circuit_breaker.state == State.METRICS_ONLY




