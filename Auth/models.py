from datetime import date
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

class UserManager(BaseUserManager):
    def _create_user(
                    self, email, username,
                    password,
                    is_staff, is_superuser,
    ):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set.')
        email = self.normalize_email(email)
        user = self.model(
                          email=email, username=username, is_active=True,
                          date_joined=now, last_login=now,

                          is_staff=is_staff, is_superuser=is_superuser,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None):
        return self._create_user(email, username, password, False, False)

    def create_superuser(self, email, username, password):
        return self._create_user(email, username, password, True, True)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(('username'), max_length=15, primary_key=True)
    email = models.EmailField(('email address'), max_length=254, unique=True)
    is_staff = models.BooleanField(('staff status'), default=False)
    is_active = models.BooleanField(('active'), default=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        return str(self.username)

    @models.permalink
    def get_absolute_url(self):
        return "/accounts/profile/%s" % username

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def get_by_natural_key(self, username):
        return self.get(username__iexact=username)

class Profile(models.Model):
    from character.models import Character
    user = models.OneToOneField('User', blank=True, primary_key=True, on_delete=models.CASCADE)
    characters = models.ManyToManyField(Character, blank=True)
    description = models.TextField(('profile description'), max_length=500,
                                        blank=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    gender = models.CharField(('gender'), max_length=1, null=True,
                                        choices=GENDER_CHOICES, blank=True)
    profile_picture = models.ImageField(upload_to='profile-pictures/%Y/%m/%d',
                                        blank=True)
    dob = models.DateField(('birthday'), blank=True, null=True)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    def __unicode__(self):
        return str(self.user)

    def calculate_age(self):
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
