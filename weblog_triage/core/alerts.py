from enum import Enum


class AlertReason(Enum):
    PUT = "A request using a PUT HTTP method was found"
    DELETE = "A request using a DELETE HTTP method was found"
    UNCOMMON = "A request using an UNCOMMON HTTP method was found"
    FREQ_IP = "This IP is a low frequency request"


class AlertType(Enum):
    FREQUENCY = "This investigation approach is focused on triaging low frequency requests that might be suspicious"
    IOCs = "This investigation approach is focused on triaging requests that contain a match with an Indicator of Compromise (IoC)"
    Pattern = "This investigation approach is focused on looking for popular attack patterns such as XSS, SQLi, etc"


class Alert():
    def __init__(self, type, reason, raw_request):
        self.type = type
        self.reason = reason
        self.raw_request = raw_request
        self.more_info = ""

    def add_more_info(self, more_info):
        self.more_info = more_info
