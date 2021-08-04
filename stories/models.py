from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.expressions import F
from django.db.models.fields import Field
from django.urls import reverse_lazy
from ckeditor_uploader.fields import RichTextUploadingField
from slugify import slugify
import datetime

User = get_user_model()

# Create your models here.


class Tag(models.Model):
    """
    In this table we can store Tag info
    """
    title = models.CharField('Title', max_length=50)
    order = models.PositiveIntegerField('Order', default=1)
    is_published = models.BooleanField('Is Published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('Is_published')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ('created_at',)

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    In this table we can store Category info
    """

    title = models.CharField('Basliq', max_length=127)

    # moderation's
    order = models.PositiveIntegerField('Order', default=1)
    is_published = models.BooleanField('Is Published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('order', '-created_at')

    def __str__(self):
        return self.title


class Story(models.Model):

    """
    In this table we can store Story info
    """
    title = models.CharField('Basliq', max_length=127)
    description = RichTextUploadingField('Mezmun')
    image = models.ImageField('Sekil', upload_to='recipe_images')
    slug = models.SlugField('Slug', editable=False)
    is_published = models.BooleanField('Is_published', default=True)

    # relations
    tags = models.ManyToManyField(
        Tag, verbose_name='Tags', db_index=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Category',
                                 on_delete=models.CASCADE, db_index=True, related_name='stories')
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE, db_index=True,
                               related_name='stories', )

    # moderation's
    order = models.PositiveIntegerField('Order', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}-{datetime.datetime.now()}')
        return super(Story, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if self.slug:
            return reverse_lazy('stories:story_detail', kwargs={'slug': self.slug})
        return reverse_lazy('stories:story_detail', kwargs={'slug': 'sjkdnf'})

    @property
    def serialized_data(self):
        return {
            'title': self.title,
            'description': self.description,
            'slug': self.slug,
            'created_at': str(self.created_at),
        }


class Recipe(models.Model):
    """
    In this table we can store Recipe info
    """
    title = models.CharField('Basliq', max_length=127)
    slug = models.SlugField('Slug')
    short_description = models.CharField('Qisa Mezmun', max_length=255)
    image = models.ImageField('Sekil', upload_to='recipe_images')
    description = RichTextUploadingField('Mezmun')
    is_published = models.BooleanField('Is_published', default=True)
    is_approved = models.BooleanField('Approved', default=False)
    category = models.ForeignKey(Category, verbose_name='Category',
                                 on_delete=models.CASCADE, db_index=True, related_name='recipes')
    tags = models.ManyToManyField(
        Tag, verbose_name='Tags', db_index=True, blank=True, )
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE, db_index=True,
                               related_name='recipes', )

    # moderation's
    order = models.PositiveIntegerField('Order', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}-{datetime.datetime.now()}')
        return super(Recipe, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if self.slug:
            return reverse_lazy('stories:recipe_detail', kwargs={'slug': self.slug})
        return reverse_lazy('stories:recipe_detail', kwargs={'slug': 'sjkdnf'})

    @property
    def serialized_data(self):
        return {
            'title': self.title,
            'description': self.description,
            'short_description': self.short_description,
            'slug': self.slug,
            'created_at': str(self.created_at),
        }


class Comment(models.Model):
    """
    In this table we can store user Comment info
    """
    context = models.TextField('Reyiniz')

    recipe = models.ForeignKey(Recipe, verbose_name='Recipe', on_delete=models.CASCADE, db_index=True,
                               related_name='comment',)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True,
                               related_name='comment',)
    parent_comment = models.ForeignKey('self', verbose_name='Parent Comment', on_delete=models.CASCADE, db_index=True,
                                       related_name='sub_comments', blank=True, null=True,)
    

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.context


class Review(models.Model):
    """
    In this table we can store user Review info
    """
    context = models.TextField('Reyiniz')

    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True,
                               related_name='review',)
    parent_review = models.ForeignKey('self', verbose_name='Parent review', on_delete=models.CASCADE, db_index=True,
                                       related_name='sub_reviews', blank=True, null=True,)
    story = models.ForeignKey(Story, verbose_name='Story', on_delete=models.CASCADE, db_index=True,
                              related_name='review', null = True , blank=True)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.context

class Contact(models.Model):
    """
    In this table we can store user Contact info
    """
    name = models.CharField('Tam adi', max_length=127)
    email = models.EmailField('E-poct', max_length=63)
    subject = models.CharField('Movzu', max_length=255)
    message = models.TextField(
        'Mesaj', help_text='Bu qutuya mesajinizi daxil edin')

    # moderation's
    order = models.PositiveIntegerField('Order', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    """
    In this table we can store user Subscriber info
    """
    email = models.EmailField('E-poct', max_length=63, unique=True)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
