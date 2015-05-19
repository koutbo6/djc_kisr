from django.db import models

# Create your models here.


class Poll(models.Model):
    # CharField holds a string
    # The first parameter is verbose_name
    # max_length is number of characters allowed
    name = models.CharField("poll name", max_length=64)

    # category to distinguish poll types
    category = models.CharField("poll category", max_length=64)

    # TextField holds a variable length field
    # usually used for large string based documents
    # use it for descriptions and when you do not
    # need to search the field
    # notice how we didn't include the verbose_name
    # Django has reasonable defaults for converting
    # the field name into a human readable form
    question = models.TextField(blank=True)

    def __str__(self):
        return "{}: {}".format(self.name, self.category)

    def choice_count(self):
        return self.choice_set.count()


class Choice(models.Model):
    # This established a one to many relationship between
    # (one) Poll has (Many) Choice
    # other relations are OneToOne and ManyToMany
    poll = models.ForeignKey(Poll, verbose_name="poll question")

    # The answers to be shown for polls
    label = models.CharField("answer choice", max_length=200)

    # Store DimeTime to keep track of our polls
    # auto_now_add means that the current datetime
    # is inserted when the object is first created
    # When auto_now_add is True then default and blank
    # are overridden to now and True
    # verbose_name will be "Created At"
    # auto_now_add means set date/time on first save only
    created_at = models.DateTimeField(auto_now_add=True)

    # keep track of last change made to poll
    # auto_now means update the field to now
    # everytime it is saved
    # verbose_name will be "last updated"
    # auto_now means update date/time on save
    updated_at = models.DateTimeField(
        "last updated", auto_now=True)


class Response(models.Model):
    # every response will have a single choice made
    # or none
    # remember that response will be related to Poll
    # through Choice
    choice = models.ForeignKey(Choice, null=True, blank=True)

    # null parameter means that we can store None value in DB
    # For text based fields, we never set null to True
    # because Django will always store and empty string ""
    # null only makes finding empty fields more difficult
    # as we will need to search for "" and None
    comment = models.TextField(blank=True)

    # Just like poll, we need to know time of response
    submitted_at = models.DateTimeField(auto_now_add=True)

    def poll_name(self):
        return self.choice.poll.name

    def choice_label(self):
        return self.choice.label
