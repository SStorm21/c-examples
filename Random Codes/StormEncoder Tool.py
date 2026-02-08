import marshal, zlib, base64

my_code = "print(\"WORKING!\")"
comp = (my_code,)  # Remove unnecessary elements

def encrypt():
  data = marshal.dumps(comp)
  compressed = zlib.compress(data)
  encoded = base64.b64encode(compressed)
  return encoded

def decrypt(encoded_data):
  decoded = base64.b64decode(encoded_data)
  decompressed = zlib.decompress(decoded)
  unmarshalled = marshal.loads(decompressed)
  return unmarshalled[0]  # Get the first element (code string)

# Encrypt the code
encrypted_code = encrypt()

# Decrypt and execute the code (use with caution for untrusted sources)
code_to_exec = decrypt(encrypted_code)
exec(code_to_exec)

# Print the encrypted code (optional)
print(encrypted_code.decode())
