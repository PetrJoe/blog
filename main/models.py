from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, default=1, related_name="user_post", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
    	return self.title
    
    class Meta:
        ordering = ('-created_date',)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, null=True)
    date_added = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.comment


    def num_comments(self):
        return self.comment_set.all().count()
