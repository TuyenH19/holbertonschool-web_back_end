#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async."""
import asyncio
from typing import List

# import wait_random
wait_random = __import__('0-basic_async_syntax').wait_random 


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that takes in 2 int arguments
    n and max_delay and return list of all delays
    in order without using sort()."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    done, _ = await asyncio.wait(tasks)
    return sorted([task.result() for task in done])
