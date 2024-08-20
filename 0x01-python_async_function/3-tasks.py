#!/usr/bin/env python3
"""Function  takes an integer and returns  asyncio.Task."""
import time
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """
    Takes max_delay as an argument and returns .
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
