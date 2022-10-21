from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """ Helps django work with our custom user model"""

    def create_user(self, email, password=None, **kwargs):
        """Creates a new user profile object"""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password) # this will encrypt the password 
        user.save(using = self.db)

        return user

    def create_superuser(self, email, password, **kwargs):
        """Creates and saves a new superuser with given details"""

        user = self.create_user(email, password, **kwargs)

        user.is_superuser = True
        user.is_staff = True

        user.save(using = self.db)

        return user
