from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define roles
ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
)

#receiver to auto-create profile on user creation
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

#receiver to save profile on user creation
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.userprofile.save()

class Author(models.Model):
    name = models.CharField()
    
    def __str__(self):
        return self.name    

class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    class Meta:
        permissions = [
                ("can_add_book", "Can add a book"),
                ("can_change_book", "Can change book details"),
                ("can_delete_book", "Can delete a book"),
                ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField()
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField()
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
