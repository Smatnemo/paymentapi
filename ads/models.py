from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

from taggit.managers import TaggableManager

# Create your models here.
class Ad(models.Model):
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 1 character")]
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    # https://django-taggit.readthedocs.io/en/latest/api.html#TaggableManager
    tags = TaggableManager(blank=True)

    # Picture
    picture = models.BinaryField(null=True, blank=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, blank=True,
            help_text='The MIMEType of the file')

    # Favorites
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Fav",
                    related_name='favorite_ads')
                    # Calling Ad.favorite_ads returns a list of users that like the ad instance

    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment', related_name='comments_owned')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(
        validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")]
        )

    # An ad has a one-to-many relationship with Comment
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    # A User has a one-to-many relationship with Comment
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        if len(self.text) < 15 : return self.text
        return self.text[:11] + ' ...'

class Fav(models.Model):
    # Fav has a many to one relationship with Ad
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    # Fav has a many to one relationship with User
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        # only one entry with the same combination can be entered
        unique_together = ('ad', 'user')

    def __str__(self):
        return '%s likes %s'%(self.user.username, self.ad.title[:10])