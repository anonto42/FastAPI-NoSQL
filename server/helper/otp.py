import random

def generate_otp(length: int = 6):
    
    lower_bound = 10**(length - 1)
    upper_bound = 10**length - 1
    return random.randint(lower_bound, upper_bound)
