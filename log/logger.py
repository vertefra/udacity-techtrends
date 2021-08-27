import logging
import sys

stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setLevel(logging.DEBUG)

stderror_handler = logging.StreamHandler(stream=sys.stderr)
stderror_handler.setLevel(logging.ERROR)

handlers = [stdout_handler, stderror_handler]

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:%(name)s - - [%(asctime)s] %(message)s",
    datefmt="%d-%b-%Y %H:%M:%S",
    handlers=handlers,
)
