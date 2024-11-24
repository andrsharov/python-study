import base64
input_str = input()
b = bytes(input_str, 'utf-8')
encoded = base64.urlsafe_b64encode(b)
output = encoded.decode('utf-8')
print(output)