from custom_exception import CustomException
def error_handling(error: CustomException):
    """
    The function handles errors from CustomException class
    :param error class CustomException
    :return a message about the exception
    """
    try:
        raise error
    except CustomException as e:
        return f'{e.__class__} has been detected in {error.counter} time.\nThe reason: {e}'
