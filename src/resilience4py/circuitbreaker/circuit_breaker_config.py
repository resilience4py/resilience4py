from dataclasses import dataclass
from enum import Enum

class SlidingWindowType(Enum):
    TIME_BASED = 10
    COUNT_BASED = 20

@dataclass
class CircuitBreakerConfig:
    failure_rate_threshold:int
    permitted_number_of_calls_in_half_open_state:int
    sliding_window_size:int
    sliding_window_type:SlidingWindowType
    minimum_number_of_calls:int
    writable_stack_trace_enabled:bool
    automatic_transition_from_half_open_to_open_enabled:bool
    slow_call_rate_threshold:float
    slow_call_duration_threshold:int
