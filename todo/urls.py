from django.urls import path
from . import views
from todo.views import addTodo,delete,edit

app_name = "todo"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/update', views.update, name='update'),
    path('addTodo/',views.addTodo),
    path('<int:id>/delete', views.delete, name='delete'),
]