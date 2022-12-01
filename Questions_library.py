from random import choice
from string import ascii_uppercase


def generate_question(task_difficulty):
    lengths = {1:3,2:4,3:6,4:8}
    
    n = lengths[task_difficulty]

    string_val = "".join(choice(ascii_uppercase) for i in range(n))
    
    return string_val