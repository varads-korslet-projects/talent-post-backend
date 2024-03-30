from django.db import models
from django.contrib.auth.models import User

# User Model
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_display_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

# Team Model
class Team(models.Model):
    team_code = models.CharField(max_length=20, unique=True)
    registration_id = models.CharField(max_length=50, unique=True)
    team_name = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)
    rank = models.IntegerField(default=0)

# Team Members Model
class TeamMembers(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
