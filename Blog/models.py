from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(choices=[('admin' , 'Admin'),( 'user', 'User')])
    

    def __str__(self):
        return self.name

    def change_role(self,role_name):
        self.role = role_name
        self.save()


class Post(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    comment = models.ManyToManyField('Comments',related_name='comments',)

    def __str__(self):
        return self.name

    def corect_post(self):
        corect = str(input("Напиши новий текст поста"))
        self.content = corect
        self.save()



class Comments(models.Model):
    content = models.TextField()
    date = models.DateField()
    author = models.ForeignKey(User,related_name='user',on_delete=models.DO_NOTHING,)

    def __str__(self):
            return self.content
    