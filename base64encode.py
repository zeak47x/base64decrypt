import base64

# Your base64 encoded string
enc_string = "SGVsbG8gd29ybGQh"

# Step 1: Convert the base64 string to bytes
encoded_bytes = enc_string.encode('utf-8')

# Step 2: Base64 decode the bytes
decoded_bytes = base64.b64decode(encoded_bytes)

# Step 3: Convert the decoded bytes back to a string using UTF-8 encoding
dec_string = decoded_bytes.decode('utf-8')

print(dec_string)
