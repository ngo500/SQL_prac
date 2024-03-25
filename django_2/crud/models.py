from django.db import models
from django.utils.timezone import now

# User model
# first_name, last_name as CharField
# dob as DateField
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    dob = models.DateField(null=True)
    
    # Create a toString method for object string representation
    def __str__(self):
        return self.first_name + " " + self.last_name

# Instructor model
# inherits from User model (one to one)
# full_time as BooleanField
# total_learners as IntegerField
class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()
    
    # Create a toString method for object string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
               "Last name: " + self.last_name + ", " + \
               "Is full time: " + str(self.full_time) + ", " + \
               "Total Learners: " + str(self.total_learners)
        
