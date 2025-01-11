from enum import Enum


class LogLevelModel(str, Enum):
    """
    A class used to model log level in pydantic

    ...

    Attributes
    ----------
    Methods
    -------
    """

    critical = "CRITICAL"
    error = "ERROR"
    warning = "WARNING"
    info = "INFO"
    debug = "DEBUG"
