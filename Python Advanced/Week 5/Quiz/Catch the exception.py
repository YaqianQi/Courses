def exception_logger(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AssertionError:
            print('AssertionError')
        except ZeroDivisionError:
            print('ZeroDivisionError')
        except ArithmeticError:
            print('ArithmeticError')
    return inner