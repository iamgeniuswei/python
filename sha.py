import hashlib

data = "123"
hash_md5 = hashlib.md5(data.encode("utf-8"))
print(hash_md5)
print(hash_md5.hexdigest())
