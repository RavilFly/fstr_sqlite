from django.db import models

class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    class Meta:
        db_table = 'coords'

    def __str__(self):
        return f'Latitude: {self.latitude}, longitude: {self.longitude}, height: {self.height}'


class PerevalAdded(models.Model):
    STATUS_CHOICE = [
        ('new', 'Новый'),
        ('pending', 'На рассмотрении'),
        ('accepted', 'Принят'),
        ('rejected', 'Отклонен'),
    ]

    date_added = models.DateTimeField(auto_now_add=True)
    add_time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICE, default='new')
    beauty_title = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    other_titles = models.TextField(blank=True, null=True)
    connect = models.TextField(blank=True, null=True)
    winter = models.CharField(max_length=5, blank=True, null=True)
    spring = models.CharField(max_length=5, blank=True, null=True)
    summer = models.CharField(max_length=5, blank=True, null=True)
    autumn = models.CharField(max_length=5, blank=True, null=True)
    coords = models.ForeignKey('Coords', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)

    class Meta:
        db_table = 'pereval_added'

class PerevalAreas(models.Model):
    id_parent = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'pereval_areas'

# class SprActivitiesTypes(models.Model):
#     title = models.CharField(max_length=255)
#
#     class Meta:
#         db_table = 'spr_activities_types'

class Images(models.Model):
    title = models.CharField(max_length=255)
    pereval = models.ForeignKey(PerevalAdded, related_name="images", on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField()

    class Meta:
        db_table = 'images'


class Users(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    mid_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'users'

