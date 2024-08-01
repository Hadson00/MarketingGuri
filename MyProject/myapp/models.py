from django.db import models
from users.models import User
from django.db.models import Count

SECTION_CHOICES = {
    'empreendedorismo': 'EMPREENDEDORISMO',
    'startUp': 'STARTUP',
    'prototipo': 'PROTOTIPO',
    'pitch': 'PITCH',
    'mentoria': 'MENTORIA',
}

class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    section = models.CharField(max_length=16, choices=SECTION_CHOICES, default='empreendedorismo')

    def total_likes(self):
        return Like.objects.filter(card=self).count()

    @classmethod
    def most_liked(cls):
       return cls.objects.annotate(like_count=Count('like')).order_by('-like_count')[:10]

    def user_liked(self, user):
        return Like.objects.filter(card=self, user=user).exists()

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'card')