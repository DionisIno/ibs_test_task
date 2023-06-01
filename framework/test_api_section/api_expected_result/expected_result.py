"""
This section contains the main code statuses and other result from API methods
"""


class ExpectedRequestsResult:
    STATUS_CODE_OK = 200
    NOT_FOUND = 404
    CREATED = 201


class ExpectedCountUserList:
    PER_PAGE = 6
    TOTAL = 12
    TOTAL_PAGES = 2


class SupportData:
    url = "https://reqres.in/#support-heading"
    message = "To keep ReqRes free, contributions towards server costs are appreciated!"


class CreateUser:
    create = ["name", "job", "id", "createdAt"]
