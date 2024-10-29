#!/usr/bin/env python3
"""
Module with a function that takes an integer and returns an asyncio.Task
"""
import asyncio
from typing import Optional

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """
    Creates an asyncio Task that waits for a random delay.

    Args:
        max_delay (int): The maximum delay (in seconds) for the task.

    Returns:
        asyncio.Task: A Task that runs wait_random with max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))

