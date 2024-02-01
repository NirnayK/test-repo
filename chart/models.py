from django.db import models

class School(models.Model):
    school_name = models.CharField(max_length=200)
    district_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    language = models.CharField(max_length=200)

    def __str__(self):
        string = "Name: " + self.school_name + " District: " + self.district_name + " Category: " + self.category + " Language: " + self.language
        return string

class Match(models.Model):
    winner = models.CharField(max_length=200)
    season = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        string ="Season: " + str(self.season) + " Date: " + str(self.date) + " Winner: " + self.winner
        return string


