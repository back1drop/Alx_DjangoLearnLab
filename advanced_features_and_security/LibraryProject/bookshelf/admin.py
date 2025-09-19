from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")

# Optional: Auto-create groups & assign permissions
def setup_groups():
    content_type = ContentType.objects.get_for_model(Book)

    # Define groups and their permissions
    groups_permissions = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perms in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for codename in perms:
            permission = Permission.objects.get(
                codename=codename, content_type=content_type
            )
            group.permissions.add(permission)

# Call setup_groups when server starts (optional, can also do via admin UI)
try:
    setup_groups()
except:
    # Avoid migration errors before DB is ready
    pass
