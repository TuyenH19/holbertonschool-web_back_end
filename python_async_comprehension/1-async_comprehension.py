#!/usr/bin/env python3
"""Async Comprehensions."""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronous coroutine that collects 10 random numbers
    over async_generator, then return 10 random numbers."""
    return [i async for i in async_generator()]
