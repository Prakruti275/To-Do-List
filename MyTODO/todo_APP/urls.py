from django.contrib import admin
from django.urls import path,include
from todo_APP import views

urlpatterns = [
    path('',views.todo_list,name="todo_list"),
    path('create/',views.create_todo,name="create_todo"),
    path('complete/<int:todo_id>/',views.complete_todo,name="complete_todo"),
    path('delete/<int:todo_id>/',views.delete_todo,name="delete_todo"),
    path('admin/', admin.site.urls),
    path('', views.todo_list, name='todo_list')
 

]
