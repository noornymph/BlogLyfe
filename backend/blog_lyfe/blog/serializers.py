"""Serializers for the models of the application"""

from rest_framework import serializers

from .models import BlogPost


# Serializers define the API representation.
class BlogPostSerializer(serializers.ModelSerializer):
    """Serializer of the BlogPost model"""

    class Meta:
        """Metadata"""

        model = BlogPost
        fields = "__all__"
        lookup_field = "slug"
