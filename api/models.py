from django.db import models
import random
import string

# Length of room code
CODE_LENGTH = 6

# Generate a unique code
def generate_unique_code():
    while True:
        # Create a random string of letters
        code = ''.join(random.choices(string.ascii_uppercase, k=CODE_LENGTH))
        
        # If there is already a room with that code, generate a new one
        if Room.objects.filter(code=code).count() == 0:
            return code

def generate_random_name(): 
    return ''

# Room model
class Room(models.Model):
    code = models.CharField(max_length=CODE_LENGTH, default=generate_unique_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class User(models.Model):
    user = models.CharField(max_length=50, unique=True)
    user_name = models.CharField(max_length=50, default=generate_random_name, null=True)
    room_code = models.CharField(max_length=CODE_LENGTH, null=True)