import time
import functools
from loguru import logger

def log_step(func):

    @functools.wraps(func)
    def wrapper(*args, **kwagrs):
        func_name = func.__name__
        logger.info(f"▶️ Start {func_name}")

        start_time = time.time()
        try:
            result = func(*args, **kwagrs)
            elapsed = time.time() - start_time

            logger.info(f"✅ Finish: {func_name} | Time {elapsed:.2f}s")
            return result
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"❌ Error in {func_name} after {elapsed:.2f}s: {e}")
            raise

    return wrapper