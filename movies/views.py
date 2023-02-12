from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie
from .serializers import MovieSerializer
from joda_movies_api.permissions import IsUserOrReadOnly


class MovieList(APIView):
    serializer_class = MovieSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True, context= {'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class Movie_Get_Details(APIView):
    permission_classes = [IsUserOrReadOnly]
    serializer_class = MovieSerializer

    def get_object(self, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            self.check_object_permissions(self.request, movie)
            return movie
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = MovieSerializer(
            post, context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(
            movie, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

    
