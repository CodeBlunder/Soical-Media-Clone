from pwdlib import PasswordHash
password_hash=PasswordHash.recommended()# This line is used to create a password hash object using the recommended hashing algorithm provided by the pwdlib library. This object will be used to hash and verify passwords in our application, ensuring that user passwords are stored securely in the database.


def hash_pass(password: str):
    return password_hash.hash(password)


def verify_pass(plain_password, hashed_password):
    return password_hash.verify(plain_password,hashed_password)

