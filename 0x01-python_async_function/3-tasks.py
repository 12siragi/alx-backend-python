#!/usr/bin/env python3
"""Returns an asyncio.Task for wait_random with a given delay."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
