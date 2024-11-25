from django.db import models
import uuid

def image(instance, filename):
    extension = filename.split('.')[-1]  # Get file extension
    unique_filename = f"{uuid.uuid4().hex}.{extension}"
    return f"employee_photos/{unique_filename}"


# Create your models here.
class Employee(models.Model):
    eid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.DecimalField(max_digits=2, decimal_places=0)
    jobDescription=models.TextField()
    profile_photo=models.FileField(upload_to=image,default="default_user.png")

    def __str__(self):
        return f"EID:{self.eid}"

