from django.db import models

# Create your models here.

class BookActiveManager(models.Manager):
        def get_queryset(self):
            return super(BookActiveManager, self).get_queryset().filter(is_deleted=0)

class BookInactiveManager(models.Manager):
        def get_queryset(self):
            return super(BookInactiveManager, self).get_queryset().filter(is_deleted=1)


class Book(models.Model):
    name = models.CharField(max_length = 150)
    author = models.CharField(max_length = 150)
    price = models.IntegerField()
    pub = models.CharField(max_length=250,default= 'Tata McGraw Hill')
    is_deleted = models.IntegerField(default=0)
    active_objects = BookActiveManager()
    inactive_objects = BookInactiveManager()
    objects = models.Manager()

    def __str__(self):
        return self.name 

    class Meta:
        db_table = 'book'