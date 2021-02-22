import logging

from lilili import __title__

logging.basicConfig(
    filename=f"{__title__}.log",
    format="\t".join(
        (
            "%(asctime)s",
            "%(levelname)s",
            "%(name)s",
            "%(funcName)s",
            "%(lineno)d",
            "%(message)s",
        )
    ),
    level=logging.DEBUG,
)
