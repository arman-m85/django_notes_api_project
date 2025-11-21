
from django.urls import path, include
from Users.views import create_note, create_user,delete_note, note_detail,update_note,veiw_user_notes
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('create_user/',create_user.as_view()),
    path("create_note/",create_note.as_view()),
    path("view_note/", veiw_user_notes.as_view()),
    path("update_note/<int:pk>/",update_note.as_view()),
    path("delete_note/<int:pk>/",delete_note.as_view()),
    path("note_detail/<int:pk>/",note_detail.as_view()),
    path('silk/', include('silk.urls', namespace='silk'))
    
]

