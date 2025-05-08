
# Chapter 1: Introduction to Scalable Web Applications

# Example Django models and queries for the introduction section

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.username
    