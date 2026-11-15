import argparse
import logging

from . import __version__

logger = logging.getLogger(__name__)


def main() -> int | None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action="store_true")
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    logger.debug(f"{args=}")

    if args.version:
        print(__version__)
        return

    print("Hello world!")
