import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Postblog.settings")

django.setup()

from Blog.models import *


# User.objects.create(
#     name = "Alex",
#     email = "alex@example.com",
#     role = "user")
# User.objects.create(
#     name = "Sofa",
#     email = "sofa@example.com",
#     role = "user")

# User.objects.create(
#     name = "Iosip",
#     email = "iosip@example.com",
#     role = "user")


user1 = User.objects.get(id = 1)
user2 = User.objects.get(id = 2)
user3 = User.objects.get(id = 3)



# Comments.objects.create(
#     content = 'Накінецьто я дождаввся , скільки ждав , ждав але всьотакі єєєєє',
#     date = "2026-10-30",
#     author = user1,
#     )
comments1 = Comments.objects.get(id = 1)

# Post.objects.create(
#     name = 'Лопнула Аі бульбашка',
#     # name = models.CharField(max_length=200),
#     content ='комерційна аі бульбошка накінецьто лопнула ',
#     # content = models.TextField(),
#     date = '2026-10-29',
#     # date = models.DateField(),
#     )
post1 = Post.objects.get(id = 1 )
# post1.comment.add(comments1)
post1.corect_post("Зміна для приклада")