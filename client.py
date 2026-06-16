import asyncio

from config import HOST, PORT, ENCODING

async def main():
    """
    Connect to server and sent one message
    """

    readef, writer = await asyncio.open_connection(
        HOST,
        PORT
    )

    print("Connected to server")

    message = "Hello server!!"
    writer.write(
        message.encode(ENCODING)
    )

    writer.drain()
    print("Message sent")
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
#gyjyukgyulhul
