from django.urls import path
from .views import ListProjects, ProjectDetail, CreateProject, ProjectUpdate, ProjectDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', ListProjects.as_view(), name='projectlist'),
    path('createproject/', CreateProject.as_view(), name='createproject'),
    path('projectdetail/<int:pk>/', ProjectDetail.as_view(), name='projectdetail'),
    path('projectupdate/<int:pk>/', ProjectUpdate.as_view(), name='projectupdate'),
    path('projectdelete/<int:pk>/', ProjectDelete.as_view(), name='projectdelete'),
]
