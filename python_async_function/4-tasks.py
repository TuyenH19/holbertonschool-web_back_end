#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n."""
import asyncio
from typing import List
from typing import Callable


# Import module wait_n
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Nearly identical to wait_n except task_wait_random is being called."""

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    done, _ = await asyncio.wait(tasks)
    return sorted([task.result() for task in done])
