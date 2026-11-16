import argparse
import logging
from importlib.metadata import entry_points

from . import AbstractDisplay, __version__

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

    text = "Hello world!"

    display_eps = entry_points(group=AbstractDisplay.ENTRY_POINT_GROUP)

    logger.debug(f"{display_eps=}")

    if display_eps:
        for display_ep in display_eps:
            try:
                logger.info(f"Loading display plugin {display_ep.name}.")
                display_class = display_ep.load()
                display_instance = display_class()
                logger.info(
                    f"Display plugin {display_ep.name} version {display_instance.version} loaded."
                )
                display_instance.display(text)
            except Exception as e:
                logger.error(f"Display plugin {display_ep.name} exception: {e}.")
    else:
        logger.warning("No display plugins found.")
