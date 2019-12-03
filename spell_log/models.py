from django.db import models

# Create your models here.
class Spell(models.Model):
    SPELL_TYPES = (
        (0,"じゅもん"),
        (1,"とくぎ")
    )

    SPELL_CATEGORIES = (
        (0,"ダメージ"),
        (1,"かいふく"),
        (2,"その他")
    )

    name = models.CharField(max_length=200, unique=True)
    name_english = models.CharField(max_length=200, blank=True)

    spell_type = models.IntegerField(choices=SPELL_TYPES, default=0)
    spell_category = models.IntegerField(choices=SPELL_CATEGORIES, blank=True)

    description = models.TextField()
    description_english = models.TextField(blank=True)

    cost = models.IntegerField()

    user = models.ManyToManyField('Character', through='CharacterLearns')
    class_user = models.ManyToManyField('Class', through='ClassLearns')

    notes = models.TextField()

class Character(models.Model):
    name = models.CharField(max_length=200, unique=True)

    game = models.ForeignKey('Game', on_delete=models.CASCADE)

class CharacterLearns(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    spell = models.ForeignKey('Spell', on_delete=models.CASCADE)

    level = models.IntegerField(blank=True)

class Class(models.Model):
    name = models.CharField(max_length=200, unique=True)

    game = models.ForeignKey('Game', on_delete=models.CASCADE)

class ClassLearns(models.Model):
    character = models.ForeignKey('Class', on_delete=models.CASCADE)
    spell = models.ForeignKey('Spell', on_delete=models.CASCADE)

    level = models.IntegerField(blank=True)

class Game(models.Model):
    name = models.CharField(max_length=200, unique=True)