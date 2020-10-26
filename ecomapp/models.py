from django.db import models

# Create your models here.


class Setting(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False')
    )
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = models.TextField()
    phone = models.IntegerField()
    fax = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True, null=True)
    smptserver = models.CharField(max_length=100)
    smpt_password = models.CharField(blank=True, null=True, max_length=50)
    smptport = models.CharField(blank=True, max_length=100)
    icon = models.ImageField(blank=True,null=True, upload_to='icon/')
    instagram = models.CharField(blank=True, max_length=100)
    facebook = models.CharField(blank=True, max_length=100)
    address = models.TextField()
    contact = models.TextField()
    reference = models.TextField()
    status = models.CharField(max_length=50, choices=status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    status = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed')
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField( blank=True)
    status = models.CharField(max_length=40, choices=status, default='New')
    ip = models.CharField(max_length=100, blank=True)
    note = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name