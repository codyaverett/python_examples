"""
Native vs Generator Based Coroutines: Interoperability
There’s no functional differences between the Native and Generator based coroutines except the differences in the syntax. It is not permitted to mix the syntaxes. So we can not use await inside a generator based coroutine or yield/yield from inside a native coroutine.

Despite the differences, we can interoperate between those. We just need to add @types.coroutine decorator to old generator based ones. Then we can use one from inside the other type. That is we can await from generator based coroutines inside a native coroutine and yield from native coroutines when we are inside generator based coroutines.:
"""

import asyncio
import datetime
import random
import types

# Allows use of await in other asyncio functions


@types.coroutine
def my_sleep_func():
    yield from asyncio.sleep(random.randint(0, 5))


async def display_date(num, loop, ):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await my_sleep_func()


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()
