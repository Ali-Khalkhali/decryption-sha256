from csv import reader
from hashlib import sha256
hash_password_to_password = {}
for password in range(1,10000):
    hashing_number = sha256(b'%i'% password).hexdigest()
    hash_password_to_password[hashing_number] = password
with open('E:\\DOWNLOADS\\2.csv') as f:
    passwords_singer =reader(f)
    for row in passwords_singer:
        name_users = row[0]
        for key in row[1:]:
            print(name_users,':',hash_password_to_password[key])
