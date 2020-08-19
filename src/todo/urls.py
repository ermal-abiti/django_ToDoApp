from django.urls import path
from .views import toDoApp, deleteToDo, aboutPage

urlpatterns = [
    path('', toDoApp, name='indexPage'),
    path('todos/<int:id>/delete', deleteToDo, name="deleteToDo_url"),
    path('about/', aboutPage, name="aboutPage_url")
]