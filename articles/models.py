from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True) # 생성시에 자동으로 추가가 되겠다 라는 뜻임


