import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digit=True, use_special_chars=False):
    if length < 1:
        raise ValueError("Password length must be at least 1")
    # Build the pool of characters based on user choice
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digit:
        char_pool += string.digits
    if use_special_chars:
        char_pool += string.punctuation
    
    if not char_pool:
        raise ValueError("At least one character set must be enabled")
    
    # Generate password
    password = "".join(random.choices(char_pool, k=length))
    return password
print(generate_password(16, True, True, True, True))