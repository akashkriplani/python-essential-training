# Custom Exception
class CustomException(Exception):
  pass

def causeError():
  raise CustomException('You called the causeError function!')

print(causeError())

# Adding attributes

class HttpException(Exception):
  statusCode = None
  message = None

  def __init__(self):
    super().__init__(f'Status code: {self.statusCode} and message is: {self.message}')

class NotFound(HttpException):
  statusCode = 404
  message = 'Resource not found'

class ServerError(HttpException):
  statusCode = 500
  message = 'Internal server error'

def raiseServerError():
  raise ServerError()

print(raiseServerError())