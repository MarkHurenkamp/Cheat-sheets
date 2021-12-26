import os

os.chdir("Python/Logging")
# log_settings changes sys.excepthook to log_settings.log_exceptions, so
# importing log_settings is sufficient to capture uncaught exceptions to the
# log file, meanwhile they are also (still) printed to stdout
import log_settings


# adds 'Starting new program!' with timestamp to the log file
log_settings.log_message("Starting new program!")


def divide(num1: int, num2: int) -> float:
    log_settings.log_message(f"Attempting to divide {num1} by {num2}")
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        # Caught exceptions can be added as a log message:
        log_settings.log_exception(e)


# Normal behaviour:
print(divide(10, 3))

# Caught error:
print(divide(10, 0))

# Uncaught error:
print(divide(10 / "x"))
