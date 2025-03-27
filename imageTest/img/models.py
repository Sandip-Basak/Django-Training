import os
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete

class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Picture(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pictures")  # ForeignKey to Product
    picture = models.ImageField(upload_to='images/')  

    def __str__(self):
        return f"Picture for {self.product.name}"

    def delete(self, *args, **kwargs):
        # Delete the image file from the media folder before deleting the database entry
        if self.picture:
            if os.path.isfile(self.picture.path):
                os.remove(self.picture.path)
        super().delete(*args, **kwargs)

# Signal to delete image file when a Picture instance is deleted
@receiver(pre_delete, sender=Picture)
def delete_picture_file(sender, instance, **kwargs):
    if instance.picture:
        if os.path.isfile(instance.picture.path):
            os.remove(instance.picture.path)
