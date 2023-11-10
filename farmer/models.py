from django.db import models
# from django.contrib.auth.models import AbstractUser,Group,Permission,_
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Use a unique related_name
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Use a unique related_name
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )


    def __str__(self):
        return self.email
    

class UserInformation(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE,related_name="UserInformation")
    uname = models.CharField(max_length=100)
    uplace = models.CharField(max_length=100)
    ublock = models.CharField(max_length=100)
    udate = models.DateField()
    product_name = models.CharField(max_length=100)
    product_weight = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.uname)
   

class ResponseLog(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Farmer_details(models.Model):
    # user=models.OneToOneField(User,null=True,on_delete=models.CASCADE,related_name="Farmer_details")
    your_name=models.CharField(max_length=100,null=True)
    father_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    mail_id = models.EmailField()
    aadhaar_number = models.CharField(max_length=12)
    pan_card_number = models.CharField(max_length=10)
    land_area = models.DecimalField(max_digits=10, decimal_places=2)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=15)
    bank_name = models.CharField(max_length=100)
    loan_details = models.TextField()
    first_time_investment_size = models.DecimalField(max_digits=10, decimal_places=2)
    job_card_number = models.CharField(max_length=20)
    farmer_name1 = models.CharField(max_length=100)
    mobile_number1 = models.CharField(max_length=15)
    land1 = models.CharField(max_length=10)
    another_farmer_name = models.CharField(max_length=100)
    mobile_number2 = models.CharField(max_length=15)
    land_area2 = models.CharField(max_length=10)

    def __str__(self):
        return self.your_name  # Display farmer's name in admin panel

#custom user models


