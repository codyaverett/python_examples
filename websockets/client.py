#!/usr/bin/env python

import asyncio
from websockets import connect


async def hello(uri):
    async with connect(uri) as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()


def init():
    try:
        asyncio.run(hello("ws://localhost:8765"))
    except KeyboardInterrupt:
        print("Exiting")


if __name__ == "__main__":
    init()
