from django.db import models
# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class Worker(models.Model):
    name = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f'{self.name} : {self.email}'

class WorkOrder(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    deadline = models.DateTimeField(default=now)
    assigned_to = models.ManyToManyField(Worker, related_name='assignees', blank=True)

    class Meta:
        verbose_name_plural = 'Work Order'

    def __str__(self):
        return f'{self.title} : {self.deadline}'

# @receiver(m2m_changed, sender=WorkOrder.assigned_to.through)
# def assigned_to_changed(sender, **kwargs):
#     if kwargs['instance'].assigned_to.count() > 5:
#         raise ValidationError({'assigned_to': ["You can't assign more than five workers!"]})
