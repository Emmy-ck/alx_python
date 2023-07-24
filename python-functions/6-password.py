def validate_password(password):
    if len(password) < 8:
        return False
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    
    for i in password:
        if i.isupper():
            has_uppercase = True
        elif i.islower():
            has_lowercase = True
        elif i.isdigit():
            has_digit = True
    if not (has_uppercase and has_lowercase and has_digit):
        return False
    
    if ' ' in password:
        return False
    
    return True