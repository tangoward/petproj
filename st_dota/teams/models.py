from django.db import models

# Create your models here.


class Region_Name(models.Model):
    reg_name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.reg_name


class Team_Name(models.Model):
    name_team = models.CharField(max_length=250, unique=True)
    #logo = models.ImageField(upload_to='logos', blank=True)
    region_member = models.ForeignKey(Region_Name, related_name='regions', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name_team + ' - ' + str(self.region_member)


class Team_Member(models.Model):

    # Position values in drop down list
    POSITIONS = (
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
    )

    member_name = models.CharField(max_length=250)
    position = models.PositiveIntegerField(choices=POSITIONS)
    member_team = models.ForeignKey(Team_Name, related_name='teams', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.member_name + ' - ' + str(self.member_team) + ' - ' + str(self.position)
