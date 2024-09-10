import hashlib

data = 'Hello, world!'
hash_object = hashlib.sha256(data.encode())
print(hash_object.hexdigest())