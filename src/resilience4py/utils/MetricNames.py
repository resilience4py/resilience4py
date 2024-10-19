from dataclasses import dataclass

@dataclass(frozen=True)
class MetricNames:
    DEFAULT_PREFIX = "resilience4py.circuitbreaker"
    SUCCESSFUL = "successful"
    FAILED = "failed"
    SLOW = "slow"
    SLOW_SUCCESS = "slow_successful"
    SLOW_FAILED = "slow_failed"
    NOT_PERMITTED = "not_permitted"
    BUFFERED = "buffered"
    STATE = "state"
    FAILURE_RATE = "failure_rate"
    SLOW_CALL_RATE = "slow_call_rate"