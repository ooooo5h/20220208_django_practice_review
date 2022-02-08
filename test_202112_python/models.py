from django.db import models

# Create your models here.
class LectureReview(models.Model):
    lecture = models.ForeignKey('Lectures', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    title = models.CharField(max_length=50)
    content = models.TextField()
    score = models.FloatField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lecture_review'


class LectureUser(models.Model):
    lecture = models.ForeignKey('Lectures', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecture_user'


class Lectures(models.Model):
    name = models.CharField(max_length=50)
    max_count = models.IntegerField()
    fee = models.IntegerField()
    campus = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lectures'


class Posts(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'posts'


class PostsReply(models.Model):
    post = models.ForeignKey(Posts, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'posts_reply'


class Users(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    birth_year = models.IntegerField()
    address = models.CharField(max_length=20)
    gender = models.CharField(max_length=2)
    height = models.FloatField()
    created_at = models.DateTimeField()
    friend = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'