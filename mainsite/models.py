from django.db import models


class Blog(models.Model):

    image = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=350, null=False, blank=False)
    tag = models.CharField(max_length=50)
    blog_post = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title


class BlogComments(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=350)
    email = models.EmailField(max_length=254, null=True, blank=True)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):

    image = models.ImageField(upload_to='courses')
    title = models.CharField(max_length=350, null=False, blank=False)
    tag = models.CharField(max_length=50)
    couser_description = models.TextField()
    Objectives = models.TextField()
    level = models.CharField(max_length=50)
    Eligibility = models.TextField()

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title


class lessons(models.Model):
    slug = models.SlugField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=350)
    postion = models.IntegerField()
    video = models.FileField(upload_to="lessons")

    def __str__(self):
        return self.title

    
    @property
    def videoUrl(self):
        try:
            url = self.video.url
        except:
            url = ''
        return url

class coursefeedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=350)
    comment = models.TextField()

    def __str__(self):
        return self.name
    
    
class lessonfeedback(models.Model):
    lesson = models.ForeignKey(lessons, on_delete=models.CASCADE)
    name = models.CharField(max_length=350)
    comment = models.TextField()

    def __str__(self):
        return self.name