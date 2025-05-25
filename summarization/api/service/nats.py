import asyncio
import nats
from nats.errors import ConnectionClosedError, TimeoutError, NoServersError



class NatsClient:
    def __init__(self, url: str = "nats://localhost:4222"):
        self.url = url
        self.nc = None

    async def connect(self):
        try:
            print(f"Attempting to connect to NATS at {self.url}...")
            self.nc = await nats.connect(self.url)
            print("Connected to NATS!")
        except (ConnectionClosedError, TimeoutError, NoServersError) as e:
            print(f"Initial connection failed: {e}")
            raise

    async def close(self):
        if self.nc and self.nc.is_connected:
            await self.nc.drain()
            await self.nc.close()
            print("Disconnected from NATS.")

    async def publish(self, subject: str, message: str):
        if self.nc and self.nc.is_connected:
            await self.nc.publish(subject, message.encode())
        else:
            raise ConnectionClosedError("Not connected to NATS.")

    async def subscribe(self, subject: str, cb):
        if self.nc and self.nc.is_connected:
            await self.nc.subscribe(subject, cb=cb)
        else:
            raise ConnectionClosedError("Not connected to NATS.")