from django.db import models

from django.contrib.auth.models import User



# Create your models here.

class AcademicResource(models.Model):
    CATEGORY_CHOICES = [

        ('lecture_notes', 'Lecture Notes'),
        ('past_papers', 'Past Papers'),
        ('textbooks', 'Textbooks'),
        ('math', 'Math'),
        ('science', 'Science'),
        ('engineering', 'Engineering'),
        ('humanities', 'Humanities'),
        ('business', 'Business'),
        ('other', 'Other')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    school = models.CharField(max_length=100,null=True,blank=True)

    # added functionality of uploading documents
    rating = models.FloatField(default=0)
    num_ratings = models.IntegerField(default=0)
    document = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.title

    def average_rating(self):
        if self.num_ratings == 0:
            return 0
        else:
            return self.rating / self.num_ratings


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(AcademicResource, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(AcademicResource, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



