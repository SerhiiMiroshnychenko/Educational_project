import io

binary_stream = io.BytesIO()
print(type(binary_stream))
binary_stream.write('Hello, world!\n'.encode('ascii'))
binary_stream.write('Hello, world!\n'.encode('utf-8'))
binary_stream.seek(0)
stream_data = binary_stream.read()
print(type(stream_data))
print(stream_data)
mutable_buffer = binary_stream.getbuffer()
print(type(mutable_buffer))
print(mutable_buffer)
mutable_buffer[7:12] = 0xFF
print(mutable_buffer)
print(mutable_buffer[0])
binary_stream.seek(0)
print(binary_stream.read())
