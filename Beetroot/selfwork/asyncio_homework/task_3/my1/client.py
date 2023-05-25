import asyncio as a

async def tcp_echo_client(message):
    reader, writer = await a.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

async def main():
    await a.gather(
        tcp_echo_client('Hello Server!'),
        tcp_echo_client('How are you?'),
        tcp_echo_client('Have a good day!'),
        tcp_echo_client('Goodbye!'),
    )

a.run(main())

