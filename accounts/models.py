from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    ''' user model '''
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    full_name = models.CharField(unique=True, max_length=100)
    otp = models.CharField(max_length=100, null=True, blank=True)
    refresh_token = models.CharField(max_length=1000, null=True, blank=True)

    USERNAME_FIELD = 'email'  # email is the username field
    REQUIRED_FIELDS = ['username']  # email field make required email=username
    """
    1. USERNAME_FIELD = 'email' means:
        Users will login with their email instead of a username
        Example: user@example.com + password (not username + password)

    2. REQUIRED_FIELDS = ['username'] means:
        When creating a superuser (admin) with python manage.py createsuperuser:  # noqa
        It will ask for email (because it's the login field)
        Then ask for username (because we listed it as required)
        Then ask for password

    What's happening in your code:
        Your model automatically creates a username from the email if empty
        (e.g., user@example.com → username = "user")
        But still needs the username field for admin commands
    """
    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        email_username, full_name = self.email.split("@")
        if self.full_name == "" or self.full_name is None:
            self.full_name == email_username
        if self.username == "" or self.username is None:
            self.username = email_username
        super(User, self).save(*args, **kwargs)


class Profile(models.Model):
    ''' profile model '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(
        upload_to="user_folder",
        default="default-user.jpg",
        null=True,
        blank=True
    )
    full_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.full_name:
            return str(self.full_name)
        else:
            return str(self.user.full_name)

    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name is None:
            self.full_name == self.user.username
        super(Profile, self).save(*args, **kwargs)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
