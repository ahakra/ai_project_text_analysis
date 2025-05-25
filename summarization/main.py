import  asyncio
from api.utils.transformer_nats import run_nats
from api.utils.service_registry import run_service

async def main():
    await asyncio.gather(
        run_service(host="localhost", port=50051),
        run_nats()
    )

if __name__ == "__main__":
    asyncio.run(main())
