#!/usr/bin/env python3
"""Function that takes an integer and returns an asyncio.Task."""
import asyncio
from typing import Task

# Import the wait_random coroutine from 0-basic_async_syntax
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int = 0) -> Task:
    """
    Takes max_delay as an argument and returns an asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
