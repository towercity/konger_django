from django.contrib import admin
from .models import Spell, Character, Class, CharacterLearns, ClassLearns, Game

# Register your models here.
class UserInline(admin.TabularInline):
    model = CharacterLearns
    extra = 1

class ClassInline(admin.TabularInline):
    model = ClassLearns
    extra = 1

class SpellAdmin(admin.ModelAdmin):
    inlines = (UserInline,ClassInline,)

    list_display = ('name','spell_type','spell_category','description','cost',)
    list_filter = ('user','class_user')


admin.site.register(Spell, SpellAdmin)
admin.site.register(Character)
admin.site.register(Class)
admin.site.register(CharacterLearns)
admin.site.register(ClassLearns)
admin.site.register(Game)