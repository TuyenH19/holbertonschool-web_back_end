#!/usr/bin/env python3
"""Measure the runtime."""
import asyncio
from typing import List
from random import uniform
from functools import partial
import time

# Import module wait_n
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Asynchronous coroutine that measures the total execution time
    for wait_n(n, max_delay), and returns total_time / n."""

    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
