from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    # category = models.Foreignkey('blog.Category', related_name='categories')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent = models.ForeignKey('self', blank=True, null=True)  # 'self' > 정의되기전 django에서 calss자신을 사용할때
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.parent:
            return "{} - {}".format(self.parent.name, self.name)
        else:
            return self.name


def approved_comments(self):
    return self.comments.filter(approved_comment=True)
