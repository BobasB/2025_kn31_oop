import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main(p: int = 5) -> int:
    for i in range(1, p):
        logger.debug(f"Processing {i}")
    return 0

if __name__ == "__main__":
    main()