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

# Learner model
# inherits from User model
# enum choices for occupation
# occupation as CharField
# social_link as URLField
class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    # Occupation Char field with defined enumeration choices
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    # Social link URL field
    social_link = models.URLField(max_length=200)
    
    # Create a toString method for object string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
                "Last name: " + self.last_name + ", " \
                "Date of Birth: " + str(self.dob) + ", " + \
                "Occupation: " + self.occupation + ", " + \
                "Social Link: " + self.social_link
   

# Course model
# many to many with Instructor model
# name, description as CharField
# instructors as ManyToManyField
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    # Many-To-Many relationship with Instructor
    instructors = models.ManyToManyField(Instructor)
    
    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description

# Lesson model
# one to many with Course model
# title as CharField
# course as ForeignKey
# content as TextField
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()

