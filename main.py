#!/usr/bin/env python3

import logging
import signal
import sys
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")


def signal_handler(signum, _):
    logging.info(f"Received signal {signum}, shutting down gracefully...")
    sys.exit(0)


# Register signal handlers
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)  # Also handle Ctrl+C

i = 0
memory = []
while True:
    i += 1
    logging.info(f"Allocating {i * 4} MiB...")
    memory.append(bytearray(4 * 1024 * 1024))
    time.sleep(0.1)
