#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async."""
import asyncio
from typing import List
from random import uniform
from functools import partial

# import wait_random
# from 0-basic_async_syntax import wait_random 
async def wait_random(max_delay: int) -> float:
    """Asynchronous coroutine that waits for a random delay
    between 0 and max_delay seconds (inclusive)."""

    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that takes in 2 int arguments
    n and max_delay and return list of all delays
    in order without using sort()."""

    tasks = [wait_random(max_delay) for _ in range(n)]
    done, _ = await asyncio.wait(tasks)
    return sorted([task.result() for task in done])
