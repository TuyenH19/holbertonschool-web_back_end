#!/usr/bin/env python3
"""Async generator."""
import asyncio
import random


async def async_generator():
    """Asynchronous coroutine that yields a random number
    between 0 and 10, after waiting 1 second,  repeat 10 times."""
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random number btw 0 and 10
