import base64

file = open('filein.txt', 'rb')

binary_data = file.read()
print(binary_data)

base64_encoded_data = base64.b64encode(binary_data)
print(base64_encoded_data)

base64_decoded_data = base64.b64decode(base64_encoded_data)
print(base64_decoded_data)

file.close()