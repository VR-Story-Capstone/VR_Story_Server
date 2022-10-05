from django.db import models
from django.utils import timezone


# Create your models here.
class Sentence(models.Model):
    "sentence_type: integer, docs/sentence_list.txt explains this value"
    sentence_type = models.IntegerField()

    "subject(주어): the string which is subject(주어) of the sentence"
    subject = models.CharField(max_length=64, default="")

    "complement(보어): the string which is complement(보어) of the sentence"
    complement = models.CharField(max_length=64, default="")

    "object(목적어): the string which is object(목적어) of the sentence"
    object = models.CharField(max_length=64, default="")

    "modifier(수식어): the string which is modifier(수식어) of the sentence"
    modifier = models.CharField(max_length=64, default="")

    "predicate(서술어): the string which is predicate(서술어) of the sentence"
    predicate = models.CharField(max_length=64, default="")

    "created_at: time when create"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{},{},{},{},{},{}'.format(\
            self.sentence_type, self.subject, self.complement, \
                self.object, self.modifier, self.predicate, self.created_at)
