"""
This section contains the main code statuses and other result from GET API calls
"""


class ExpectedRequestsResult:
    STATUS_CODE_OK = 200
    NOT_FOUND = 404


class ExpectedCountUserList:
    PER_PAGE = 6
    TOTAL = 12
    TOTAL_PAGES = 2


class SupportData:
    url = "https://reqres.in/#support-heading"
    message = "To keep ReqRes free, contributions towards server costs are appreciated!"
