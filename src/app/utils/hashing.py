from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def verify_password(password, hashed_password):
    return password_hash.verify(password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)