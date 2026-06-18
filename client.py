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

    username = input("Enter your username: ")
    writer.write(
        username.encode(ENCODING)
    )

    await writer.drain()   ##!!!!!

    #Send multyply messages

    while True:
        message = input("> ") #запрошення до ведення діалогу

        if message == 'exit':
            break

        writer .write(message.encode(ENCODING))

        await writer.drain()

    writer.close()

    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())

