
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from Users.permission import IsOwner
from Users.models import Note, user
from Users.serializers import NoteSerializer, user_serializers
from rest_framework.response import Response
from rest_framework import status
from Users.Pagination import NotePagination
# Create your views here.

def home(request):
    return HttpResponse("Welcome to Personal_Notes.com")
    
class create_user(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = user_serializers
    queryset = user.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class create_note(generics.CreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class veiw_user_notes(generics.ListAPIView):
    permission_classes = [IsOwner,IsAuthenticated]
    serializer_class = NoteSerializer
    pagination_class = NotePagination
    queryset = Note.objects.select_related("owner").all()
    
    def get_queryset(self):
        
        user = self.request.user
        qs = super().get_queryset()
        return qs.filter(owner=user)

class update_note(generics.UpdateAPIView):
    permission_classes = [IsOwner,IsAuthenticated]
    serializer_class = NoteSerializer
    queryset=Note.objects.select_related("owner").all()


class delete_note(generics.DestroyAPIView):
    permission_classes = [IsOwner,IsAuthenticated]
    serializer_class = NoteSerializer
    queryset=queryset = Note.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message":"Order deleted successfully"
        },
        status=status.HTTP_200_OK)


class note_detail(generics.RetrieveAPIView):
    permission_classes = [IsOwner,IsAuthenticated]
    serializer_class = NoteSerializer
    queryset=Note.objects.select_related("owner").all()


