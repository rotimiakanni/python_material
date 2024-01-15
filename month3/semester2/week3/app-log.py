# Logging is an essential part of application development and maintenance.
# It involves recording information about an application's runtime behavior to a more persistent medium.
# This information can be used to monitor the application's health, to diagnose problems, and to detect attacks.
# The Python standard library includes a logging module that provides a flexible
# framework for recording messages from your application.

# The logging module provides a Logger class that you can use to record messages.
# The Logger class has methods for recording messages at different levels of severity.
# The levels, in increasing order of severity, are DEBUG, INFO, WARNING, ERROR, and CRITICAL.


# Example: logging to a file
import logging

# logging.basicConfig(filename="log.txt", level=logging.DEBUG)

# logging.debug("This message will be recorded.")
# logging.info("This message will be recorded.")
# logging.warning("This message will be recorded.")
# logging.error("This message will be recorded.")
# logging.critical("This message will be recorded.")


# # Example: logging to the console

# logging.basicConfig(level=logging.DEBUG)

# logging.debug("This message will be shown on the console.")
# logging.info("This message will be shown on the console.")


# Example: logging to a file with a custom format
# logging.basicConfig(
#     filename="log.txt",
#     level=logging.DEBUG,
#     format="%(asctime)s %(levelname)s %(message)s",
# )

# logging.debug("This message will be recorded.")
# logging.info("This message will be recorded.")


# Example: logging to the console with a custom format
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s %(levelname)s %(message)s",
# )

# logging.debug("This message will be shown on the console.")
# logging.info("This message will be shown on the console.")


# Example: Logging to external location: Sentry
# Sentry is a service that you can use to monitor the health of your application.
# It provides a web interface that you can use to view information about your application's runtime behavior.
# Sentry also provides a Python package that you can use to record messages from your application.
# You can install the Sentry package with pip install 'sentry-sdk[fastapi]'.
# You can use the Sentry package to record messages from your application.
# The Sentry package takes a dsn keyword argument that you can use to specify the URL of your Sentry project.
# You can find the URL of your Sentry project on the Sentry website.
# The Sentry package also takes an integrations keyword argument that you can use to specify the integrations that you want to use.
# The integrations keyword argument should be a list of strings.
# The Sentry package also takes a release keyword argument that you can use to specify the version of your application.

# Example: logging to Sentry
import sentry_sdk  # pip install 'sentry-sdk[fastapi]'

sentry_sdk.init(
    dsn="https://37b1516ab27b4a07871c70e89c838299@eeeeqe.ingest.sentry.io/9903930",
    traces_sample_rate=1.0,  # Sample rate of 1.0 records all traces
)

logging.basicConfig(
    level=logging.DEBUG,  # Everything will be logged
    format="%(asctime)s %(levelname)s %(message)s",
)

logging.debug("This message will be recorded.")
logging.info("This message will be recorded.")
logging.warning("This message will be recorded.")
logging.error("This message will be recorded.")
logging.critical("This message will be recorded.")
