from .models import Category
from modeltranslation.translator import TranslationOptions, register


@register(Category)
class CategoryTranslationOption(TranslationOptions):
    fields = ('name',)
