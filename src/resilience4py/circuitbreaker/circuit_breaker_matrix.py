from dataclasses import dataclass
from enum import Enum

class Result(Enum):
    BELOW_THRESHOLDS = 10
    FAILURE_RATE_ABOVE_THRESHOLDS = 20
    SLOW_CALL_RATE_ABOVE_THRESHOLDS = 30
    ABOVE_THRESHOLDS = 40
    BELOW_MINIMUM_CALLS_THRESHOLD = 50