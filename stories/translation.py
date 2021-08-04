from modeltranslation.translator import translator, TranslationOptions
from stories.models import (
    Tag,
    Category
)

class TagTranslationOptions(TranslationOptions):
    fields = ('title', )


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Tag, TagTranslationOptions)
translator.register(Category, CategoryTranslationOptions)