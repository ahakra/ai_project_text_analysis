import asyncio

from api.service.nats import NatsClient
from api.configuration.service_constants import  SERVICE_REGISTER_INFO
from api.service.transformer import summarize_text

async def message_handler(msg):
    subject = msg.subject
    data = msg.data.decode()
    #print(summarize_text(data))
    print(f"Received a message on '{subject}': {data}")
    await msg.respond(data)


async def run_nats():
    client = NatsClient()
    nats_subject = SERVICE_REGISTER_INFO["metadata"]["NATS"]
    while True:
        try:
            await client.connect()
            break
        except Exception as e:
            print(f"Retrying NATS connection in 5 seconds...")
            await asyncio.sleep(5)

    await client.subscribe(nats_subject, cb=message_handler)

    # Keeping connection alive
    try:
        while True:
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        await client.close()

