#!/usr/bin/env python3
"""Run time for four parallel comprehensions."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Asynchronous coroutine that will execute async_comprehension
    4 times in parallel using asyncio.gather, the return the running time."""
    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()
    total_time = end_time - start_time

    return total_time
