from django.db import models

# Create your models here.

class Contest(models.Model): 
    """
    This will be used to store the giveaway information for giveaways that have been entered
    or were attempted to have been entered.
    """
    giveaway_id = models.IntegerField()
    book_name = models.CharField(max_length=260)
    author = models.CharField(max_length=260)
    geo_entered = models.CharField(max_length=2, default='US')
    entered_date = models.DateTimeField("date entered")
    giveaway_ends_data = models.DateTimeField("giveaway end date")
    entered = models.BooleanField(default=False)
    format = models.CharField(max_length=20, default="print")