"""Contain views of the application"""

from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


class BlogPostListView(ListAPIView):
    """View related to list of blog posts"""

    queryset = BlogPost.objects.order_by("-date_created")
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)


class BlogPostDetailView(RetrieveAPIView):
    """View related to the details of post"""

    queryset = BlogPost.objects.order_by("-date_created")
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)


class BlogPostFeaturedView(ListAPIView):
    "View related to the featured post"

    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)


class BlogPostCategoryView(APIView):
    """View related to the categorial list of posts"""

    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        """Function to fetch posts according to category"""
        data = self.request.data
        category = data["category"]
        queryset = BlogPost.objects.order_by("-date_created").filter(
            category__iexact=category
        )

        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)
