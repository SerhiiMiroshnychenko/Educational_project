# Start with a jpeg file
jpg_file = open('foto.jpeg', 'rb')
jpg_data = jpg_file.read()
jpg_file.close()

# And the zip file to embed in the jpeg
zip_file = open('special.rar', 'rb')  # Path to ZIP file
zip_data = zip_file.read()
zip_file.close()

# # Combine the files_for_task3
out_file = open('special_foto.jpg', 'wb')  # Output file
out_file.write(jpg_data)
out_file.write(zip_data)
out_file.close()