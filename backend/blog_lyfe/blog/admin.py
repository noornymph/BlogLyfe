"""Admin Panel of the application"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import BlogPost


# Apply summernote to all TextField in model.
class BlogPostAdmin(SummernoteModelAdmin):
    """Admin panel settings of blog post"""

    exclude = ("slug",)
    list_display = ("id", "title", "category", "date_created")
    search_field = ("title",)
    list_per_page = 25
    summernote_fields = ("content",)


admin.site.register(BlogPost, BlogPostAdmin)
