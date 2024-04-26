#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async."""

import asyncio
import typing

# import wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Asynchronous coroutine that takes in 2 int arguments
    n and max_delay and return list of all delays
    in order without using sort()."""
    delay_n = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])

    return sorted(delay_n)
