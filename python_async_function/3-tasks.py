#!/usr/bin/env python3
"""Function task_wait_random that takes an integer max_delay and returns a asyncio.Task."""
import asyncio
# Import module wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Asynchronous coroutine returns a asyncio.Task
    from an integer max_delay."""
    return asyncio.create_task(wait_random(max_delay))
