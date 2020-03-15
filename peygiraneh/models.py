from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Employee(models.Model):
    # User = get_user_model()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    registeredDate = models.DateTimeField(auto_now=True)
    exit_time = JSONField(null=True, blank=True)
    arrival_time = JSONField(null=True, blank=True)

    # def __str__(self):
    #     return self.user.username

    # def __unicode__(self):
    #     return self.user.username


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Issue(models.Model):
    STATUS = (
        ('OPEN', 'OPEN'),
        ('DOING', 'DOING'),
        ('CLOSED', 'CLOSED'),
        ('CHECKING', 'CHECKING'),
        ('REVIEW', 'REVIEW'),
    )

    PRIORITY = (
        ('LOW', 'LOW'),
        ('NORMAL', 'NORMAL'),
        ('HIGH', 'HIGH'),
        ('VERY-HIGH', 'VERY-HIGH'),
        ('IMMEDIATE', 'IMMEDIATE')
    )
    responder = models.ForeignKey(Employee, related_name='issues', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    progress = models.IntegerField()
    time_spent = models.IntegerField()
    ideal_time = models.IntegerField()
    last_update = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now=True)
    deadline = models.DateField()
    description = models.CharField(max_length=100000)
    status = models.CharField(max_length=50, choices=STATUS)
    priority = models.CharField(max_length=50, choices=PRIORITY)
    issuer = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
