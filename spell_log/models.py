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
        (2,"その他"),
        (3,"Field")
    )

    name = models.CharField(max_length=200, unique=True)
    name_english = models.CharField(max_length=200, blank=True)

    spell_type = models.IntegerField(choices=SPELL_TYPES, default=0)
    spell_category = models.IntegerField(choices=SPELL_CATEGORIES, blank=True, default=2)

    description = models.TextField()
    description_english = models.TextField(blank=True)

    cost = models.IntegerField()

    user = models.ManyToManyField('Character', through='CharacterLearns', blank=True)
    class_user = models.ManyToManyField('Class', through='ClassLearns', blank=True)

    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=200, unique=True)

    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class CharacterLearns(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    spell = models.ForeignKey('Spell', on_delete=models.CASCADE)

    level = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.character)

class Class(models.Model):
    name = models.CharField(max_length=200, unique=True)

    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class ClassLearns(models.Model):
    character = models.ForeignKey('Class', on_delete=models.CASCADE)
    spell = models.ForeignKey('Spell', on_delete=models.CASCADE)

    level = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.character)

class Game(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return str(self.name)