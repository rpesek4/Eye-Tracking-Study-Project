import re

def validate_password(password):
    pattern = r'^[a-zA-Z0-9]{8,12}$'

    if re.match(pattern, password):
        return True
    else:
        return False

test_passwords = [
    "password123",  
    "12345",         
    "validpassword", 
    "TooLongPassword123", 
    "short",         
    "12345678",      
    "password123!",  
    "valid123"
]

for password in test_passwords:
    is_valid = validate_password(password)
    print(f"Password: {password} - Valid: {is_valid}")
