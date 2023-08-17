import time

def causeError():
  try:
    return 1/0
  except Exception as e:
    return e
  finally:
    print('This will always print')

print(causeError())

def causeError():
  start = time.time()
  try:
    time.sleep(0.5)
    return 1/0
  except Exception as e:
    return e
  finally:
    print(f'Function took {time.time() - start} seconds to execute')

print(causeError())

# Catching exceptions by type
def causeError():
  try:
    time.sleep(0.5)
    return 1/0
  except TypeError:
    print('There was a type error')
  except ZeroDivisionError:
    print('There was a zero division error')
  except Exception:
    print('There was some sort of error')

print(causeError())

# Custom decorators
def handleException(func):
  def wrapper(*args):
    try:
      func(*args)
    except TypeError:
      print('There was a type error')
    except ZeroDivisionError:
      print('There was a zero division error')
    except Exception:
      print('There was some sort of error')
  return wrapper

@handleException
def causeError():
  return 1/0

# Raising exception
@handleException
def raiseError(n):
  if n == 0:
    raise Exception()
  print(n)

print(raiseError(0))
