from django.db import models

class Newsfeed(models.Model):
    newsid = models.AutoField(primary_key=True)
    theirid = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    itemlink = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    imagelink = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=25, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return "{} - {}".format(self.title, self.source)
    class Meta:
        managed = False
        db_table = 'newsfeed'
