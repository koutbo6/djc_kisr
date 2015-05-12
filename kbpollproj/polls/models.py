from django.db import models

# Create your models here.
# Create your models here.
class Poll(models.Model):
    # CharField holds a string
    # The first parameter is verbose_name
    # max_length is number of characters allowed
    name = models.CharField("poll name", max_length=64)
    
    # TextField holds a variable length field
    # usually used for large string based documents
    # use it for descriptions and when you do not
    # need to search the field
    question = models.TextField("product description",blank=True)

class Response(models.Model):
    # This established a one to many relationship between
    # Product (one) and Rating (Many)
    # other relations are OneToOne and ManyToMany
    poll = models.ForeignKey(Product, verbose_name="reviewed product")
    # Float value that is 0.0 by default
    # null parameter means that we can store None value in DB
    # the null parameter is usefull in textbased fields
    # because empty list is always stored
    score = models.FloatField(default=0.0, blank=True, null=True) #null is useless in text fields
    comment = models.TextField("product description",blank=True)
    # Store DimeTime in which review was created
    # auto_now_add means that the current datetime
    # is inserted when the object is first created
    # When auto_now_add is True then default and blank
    # are overridden to now and True
    created_at = models.DateTimeField("reviewed at", auto_now_add=True)
    # auto_now means update the field to now
    # everytime it is saved
    updated_at = models.DateTimeField("last updated", auto_now_add=True, auto_now=True)
