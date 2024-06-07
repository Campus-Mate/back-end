from django.db import models

class IDRecord(models.Model):
    id_value = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_value
