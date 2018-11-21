
class ExpectedError(RuntimeError):
    exit_code = 255

class InvalidInput(ExpectedError):
    exit_code = 2

class InvalidFile(ExpectedError):
    exit_code = 3

class AccessDenied(ExpectedError):
    exit_code = 4
