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

# enhanced constrains
def generate_password_with_constrains(length = 16):
    if length < 4:
        raise ValueError("Password must be at least 4 to include all character types")
    
    # Ensure at least one of each type
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    special = random.choice(string.punctuation)
    digit = random.choice(string.digits)
    
    # remaining characters are random
    remaining_length = length - 4
    char_pool = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
    
    # additional constrains
    prohibited_chars = "0oli1"
    char_pool = ''.join(c for c in char_pool if c not in prohibited_chars)
    remaining_chars = random.choices(char_pool, k=remaining_length)
    
    # combinae and shuffle
    password = list(upper + lower + special + digit + "".join(remaining_chars))
    random.shuffle(password)
    return ''.join(password)

def is_valid_password(password, min_length=8, must_include_upper=True, must_include_lower=True, must_include_digit=True, must_include_special=True):
    if len(password) < min_length:
        return False, "Password is too short."

    if must_include_upper and not any(char.isupper() for char in password):
        return False, "Password must include at least one uppercase letter."

    if must_include_lower and not any(char.islower() for char in password):
        return False, "Password must include at least one lowercase letter."

    if must_include_digit and not any(char.isdigit() for char in password):
        return False, "Password must include at least one digit."

    if must_include_special and not any(char in string.punctuation for char in password):
        return False, "Password must include at least one special character."

    return True, "Password is valid."
