from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class RubricsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rubrics'

    def ready(self):
        # create new group for ability to create classes
        group, created = Group.objects.get_or_create(name='class_creators')
        # assign add_class permission to group so that we can use if statements
        permission = Permission.objects.get(codename='add_class')
        group.permissions.add(permission)