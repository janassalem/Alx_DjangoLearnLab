from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import CustomUser  # Adjust based on your app name

class Command(BaseCommand):
    help = 'Create user groups and assign permissions.'

    def handle(self, *args, **kwargs):
        # Create groups
        editors_group, created = Group.objects.get_or_create(name='Editors')
        viewers_group, created = Group.objects.get_or_create(name='Viewers')
        admins_group, created = Group.objects.get_or_create(name='Admins')

        # Get permissions
        content_type = ContentType.objects.get_for_model(CustomUser)
        can_view = Permission.objects.get(codename='can_view', content_type=content_type)
        can_create = Permission.objects.get(codename='can_create', content_type=content_type)
        can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
        can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

        # Assign permissions to groups
        editors_group.permissions.add(can_view, can_create, can_edit)
        viewers_group.permissions.add(can_view)
        admins_group.permissions.add(can_view, can_create, can_edit, can_delete)

        self.stdout.write(self.style.SUCCESS('Successfully created groups and assigned permissions'))
