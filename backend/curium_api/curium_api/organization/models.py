from django.db import models
import uuid

class Organization(models.Model):
    org_id = models.UUIDField(
        primary_key=True, auto_created=True, default=uuid.uuid4, editable=False
    )
    org_name = models.CharField(max_length=255)
    org_description = models.TextField()
    org_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
