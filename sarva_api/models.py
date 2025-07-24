from django.db import models

# Create your models here.
class WheelSpecificationForm(models.Model):
    form_number = models.CharField(max_length=50, unique=True)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()
    fields = models.JSONField()
    status = models.CharField(max_length=20, default='Saved')  # used in POST response
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.form_number