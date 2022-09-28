#!/usr/bin/env python

# Python websocket server example
# https://websockets.readthedocs.io/en/stable/intro.html

import asyncio
from websocket import serve


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

try:
    asyncio.get_event_loop().run_until_complete(
        serve(hello, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("Server stopped")
