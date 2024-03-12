
from django.urls import path
from mytodo import views



urlpatterns = [
   path("",views.homepage,name="home"),
   path("alltodos",views.myalltodo, name="todos"),
   path("save-todo",views.savethistodo),
   path("done-todo/<int:id>",views.donetodo),

]
