# 2-measure_runtime.py
#!/usr/bin/env python3
import time
import asyncio

from asyncio_tasks import wait_n  # Updated import statement

def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n as a float."""
    start_time = time.time()  # Record start time
    asyncio.run(wait_n(n, max_delay))  # Execute wait_n with asyncio.run
    end_time = time.time()  # Record end time

    total_time = end_time - start_time  # Calculate the elapsed time
    return total_time / n  # Return the average time per call

