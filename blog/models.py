from django.db import models
# from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=50)
    data = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_posted']




    


