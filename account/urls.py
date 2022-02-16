from django.urls import path
from .views import ListProjects, ProjectDetail, CreateProject, ProjectUpdate, ProjectDelete

urlpatterns = [
    path('', ListProjects.as_view(), name='listproject'),
    path('createproject/', CreateProject.as_view(), name='createproject'),
    path('projectdetail/<int:pk>/', ProjectDetail.as_view(), name='projectdetail'),
    path('projectupdate/<int:pk>/', ProjectUpdate.as_view(), name='projectupdate'),
    path('projectdelete/<int:pk>/', ProjectDelete.as_view(), name='projectdelete'),
]
