"""
This section contains the main code statuses and other result from API methods
"""


class ExpectedRequestsResult:
    STATUS_CODE_OK = 200
    NOT_FOUND = 404
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400


class ExpectedCountUserList:
    PER_PAGE = 6
    TOTAL = 12
    TOTAL_PAGES = 2


class SupportData:
    url = "https://reqres.in/#support-heading"
    message = "To keep ReqRes free, contributions towards server costs are appreciated!"


class CreateUser:
    create = ["name", "job", "id", "createdAt"]
    update = ["name", "job", "updatedAt"]
    check_update = ["name", "job"]


class RegisterUser:
    register = ["token", "id"]
    error_message = ["Note: Only defined users succeed registration",
                     "Missing password",
                     "Missing email or username"]


class Email:
    email = ['george.bluth@reqres.in', 'janet.weaver@reqres.in',
             'emma.wong@reqres.in', 'eve.holt@reqres.in',
             'charles.morris@reqres.in', 'tracey.ramos@reqres.in',
             'michael.lawson@reqres.in', 'lindsay.ferguson@reqres.in',
             'tobias.funke@reqres.in', 'byron.fields@reqres.in',
             'george.edwards@reqres.in', 'rachel.howell@reqres.in'
             ]
