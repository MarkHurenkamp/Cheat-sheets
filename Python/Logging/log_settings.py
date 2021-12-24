"""
Log settings
------------
Uses the logging library to capture user-specified messages with the 
'log_message' function, as well as any uncaught exceptions, to the log file
(located in the 'Logs' folder, which will be created if it doesn't exist).
"""

import inspect
import logging
import sys
from datetime import datetime
from pathlib import Path
from types import TracebackType
from typing import Type

log_folder = "Logs"
Path(log_folder).mkdir(parents=True, exist_ok=True)

now = datetime.now()
date = now.strftime("%Y-%m-%d")
datetimefmt = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    filename=f"{log_folder}\{date}_log.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    datefmt=datetimefmt,
)


def log_message(message: str) -> None:
    """Add a message to the logging file and print it to stdout."""
    logging.info(message)
    print(f"{now.strftime(datetimefmt)}: {message}")


def log_exception(message: str) -> None:
    """Add a message to the logging file and print it to stdout."""
    func = inspect.currentframe().f_back.f_code
    func_args = inspect.currentframe().f_back.f_locals
    func_args.pop(next(reversed(func_args.keys())), None)
    msg = f"Exception caught in function '{func.co_name}' with arguments {func_args} at line {func.co_firstlineno}' of file {func.co_filename}:\n\t{message}"
    logging.debug(msg)
    print(f"{now.strftime(datetimefmt)}: {msg}")


def _log_excepthook(
    exc_type: Type[BaseException], exc_value: BaseException, tb: TracebackType
):
    """Adds an error message to logging for uncaught exceptions while still printing the error to stdout."""
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, tb)
        return

    logging.error("Uncaught exception:", exc_info=(exc_type, exc_value, tb))
    sys.__excepthook__(exc_type, exc_value, tb)


sys.excepthook = _log_excepthook
