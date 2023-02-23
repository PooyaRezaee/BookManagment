import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model 

class Book(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='covers/',null=True,blank=True)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)
    discount = models.PositiveIntegerField()

    class Meta:
        permissions = [
        ('detial_see', 'Can read Detial all books'),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:detail', args=[str(self.id)])

    def all_reviews(self):
        return self.reviews.all()

class Review(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews')
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    likes = models.ManyToManyField(get_user_model(),related_name='review_like')

    def __str__(self):
        return self.review
    
    def count_like(self):
        return self.likes.count()