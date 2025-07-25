from django.contrib import admin
from .models import Project, ProjectImage

# Inline for project images
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

# Single ProjectAdmin combining both features
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ['title', 'created_at']
    search_fields = ['title']

# Optional: Register ProjectImage separately (for viewing/editing individually)
@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'image']
