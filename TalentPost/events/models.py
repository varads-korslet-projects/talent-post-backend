from django.db import models
from users.models import UserModel

class Category(models.Model):
    category_name = models.CharField(max_length=255)

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_photo = models.ImageField(upload_to='Images/event_covers/')
    thumbnail = models.ImageField(upload_to='Images/event_thumbnails/')
    event_video = models.FileField(upload_to='Videos/event_videos', null=True, blank=True)

class Organizer(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    organizer_name = models.CharField(max_length=255)
    organizer_info = models.TextField()
    organizer_display_image = models.ImageField(upload_to='Images/organizer_images/')

class Sponsor(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sponsor_name = models.CharField(max_length=255)
    sponsor_description = models.TextField()
    sponsor_display_image = models.ImageField(upload_to='Images/sponsor_images/')

class OrganizingTeam(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    userid = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ('organizer', 'Organizer'),
        ('screening', 'Screening'),
        ('judging', 'Judging'),
        # Add more roles as needed
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class Stage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ONLINE_OFFLINE_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )
    online_offline = models.CharField(max_length=10, choices=ONLINE_OFFLINE_CHOICES)
    venue = models.CharField(max_length=255)

class Prize(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rank = models.IntegerField()
    prize_amount = models.DecimalField(max_digits=10, decimal_places=2)
