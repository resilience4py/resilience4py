from resilience4py.circuitbreaker.circuit_breaker_config import CircuitBreakerConfig, SlidingWindowType
from resilience4py.metrics.FixedSizeSlidingWindowMetrics import FixedSizeSlidingWindowMetrics
from resilience4py.metrics.SlidingTimeWindowMetrics import SlidingTimeWindowMetrics
from resilience4py.metrics.metrics import Metrics


class CircuitBreakerMetrics(Metrics):
    def __init__(self,
                 sliding_window_size:int,
                 sliding_window_type:CircuitBreakerConfig.sliding_window_type,
                 circuit_breaker_config:CircuitBreakerConfig):
        self.sliding_window_size = sliding_window_size
        self.circuit_breaker_config = circuit_breaker_config
        self.failure_rate_threshold = circuit_breaker_config.failure_rate_threshold
        self.slow_call_rate_threshold = circuit_breaker_config.slow_call_rate_threshold
        self.slow_call_duration_threshold = circuit_breaker_config.slow_call_duration_threshold

        if sliding_window_type == SlidingWindowType.COUNT_BASED:
            self.metrics = FixedSizeSlidingWindowMetrics(sliding_window_size)
            self.minimumNumberOfCalls = min(circuit_breaker_config.minimum_number_of_calls,sliding_window_size)
        else:
            self.metrics = SlidingTimeWindowMetrics(sliding_window_size)
            self.minimumNumberOfCalls = circuit_breaker_config.minimum_number_of_calls





