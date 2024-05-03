from django.db import models

class UserClientModel(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    username = models.CharField(unique=True, max_length=150)
    last_login = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'UsuarioExample'
