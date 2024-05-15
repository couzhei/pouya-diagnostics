from random import choice

from django.db import models
from django.forms import CharField

# Create your models here.


class JobType(models.TextChoices):
    PLANNING_EXPERT = "planning"
    INSPECTOR = "inspection"
    ENGINEER = "engineering"


class JobAuthority(models.TextChoices):
    ADMIN = "admin"
    M2 = "M2"
    M3 = "M3"
    NORMAL = "normal"


class User(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
    )
    family_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    # null=True signifies that the given column is
    # allowed to store a null value, while blank=True
    # means that Django Admin will allow the field to
    # have an empty string as a valid value. In short,
    # null=True is a database constraint, while
    # blank=True is a Django application constraint.
    phonenumber = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """
        We make these models human-readable, so whenever some query matches
        a User with some conditionals, we would see them with their full name
        """
        return self.name + " " + self.family_name


class Employee(User):

    personal_code = models.CharField(max_length=20)
    job_type = models.CharField(max_length=11, choices=JobType)
    job_authority = models.CharField(
        max_length=11, choices=JobAuthority, default=JobAuthority.NORMAL
    )
    job_experience = models.TextField(null=True, blank=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)


class Customer(User):
    pass
