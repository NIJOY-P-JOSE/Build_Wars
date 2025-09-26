from django.db import models

class Participant(models.Model):
    # 'Number' is handled automatically by Django's 'id' field, which is a unique, auto-incrementing number for each participant.

    # Mandatory fields
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, verbose_name="From") # 'From' field
    phone_number = models.CharField(max_length=15)

    # Automatically set timestamp
    registration_time = models.DateTimeField(auto_now_add=True)

    # Score can be added later, so it can be empty initially
    score = models.IntegerField(null=True, blank=True, default=None)

    # Two extra optional text fields for additional info
    extra_info_1 = models.TextField(blank=True, null=True)
    extra_info_2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"#{self.id} - {self.name} from {self.location}"

    class Meta:
        # This ensures the rank list is always ordered correctly:
        # 1. Participants with a score are ranked highest.
        # 2. Scores are ranked from highest to lowest.
        # 3. If scores are tied, the person who registered earlier gets the higher rank.
        ordering = [models.F('score').desc(nulls_last=True), 'registration_time']

