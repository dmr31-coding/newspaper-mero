from django.db import models

# Create your models here.

class TimeStampModel(models.Model):   # Do not create table for this model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # same kura diff. class ma chaiyeko le ya eutai class ma rakheko inherit garna ko lagi


    class Meta:
        abstract = True  # django le model dekhne bitikai table banauxa so sab model ko table banauxa vanera avoid garna ko lagi yo properties vako model haru ma so yo model chai inheritance ko lagi matra use garna lako ho special use ko lagi haina
    


class Category(TimeStampModel):
    name = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name

class Tag(TimeStampModel):
    name = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name



class Post(TimeStampModel):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("in_active", "Inactive"),

    ]
    title = models.CharField(max_length=250)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    published_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default= "active")
    views_count = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)


    def __str__(self):
        return self.title
    
    # Fat model and thin Views
    @property
    def latest_comments(self):
        comments = Comment.objects.filter(post=self).order_by("-created_at")
        return comments
    


class Contact(TimeStampModel):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.subject
    

class Newsletter(TimeStampModel):
    email = models.EmailField()

    def __str__(self):
        return self.email
    

class Comment(TimeStampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.comment[:50]