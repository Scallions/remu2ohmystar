from remu2ohmystar import convert

DEBUG = True

from loguru import logger
import sys
logger.remove()
if DEBUG:
    logger.add(sys.stdout,level="DEBUG")
else:
    logger.add(sys.stdout,level="INFO")

remufp = "./data/remu.json"
outfp = "out.json"
userid = 6504500

convert(remufp,outfp,userid)