import asyncio as a

async def tcp_echo_client():
    while True:
        message = input('Enter your message: ')
        if message == 'exit':
            print('Close the connection')
            break
        message = f'<< {message} >> from Client One'

        reader, writer = await a.open_connection(
            '127.0.0.1', 8888)

        print(f'Send: {message!r}')
        writer.write(message.encode())
        await writer.drain()

        data = await reader.read(100)
        print(f'Received: {data.decode()!r}')

        writer.close()
        await writer.wait_closed()



a.run(tcp_echo_client())
