from django.urls import path
from django.contrib.auth.views import LoginView
from .views import CustomLoginView
from .views import Home, ListEMP, EMPDetails,EmpCreate,updateEmp,deleteEmp,SearchEMP,FindEMP,FeedbackEMP

urlpatterns = [
    path('app/', Home.as_view(), name='home'),
    
    path('', CustomLoginView.as_view(), name='login'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('emp/', ListEMP.as_view(), name='list_emp'),
    path('emp/<int:idEMP>', EMPDetails.as_view(), name='emp_details'),
    path('emp/new/',EmpCreate.as_view(),name='emp_new'),
    path('emp/edit/<int:idEMP>',updateEmp.as_view(),name='emp_edit'),
    path('emp/delete/<int:idEMP>', deleteEmp .as_view(), name='emp_delete'),
    path('emp/search/', SearchEMP.as_view(), name='emp_search'),
    path('emp/search/<int:idEMP>/', FindEMP.as_view(), name='search_results'),
    path('emp/feedback/', FeedbackEMP.as_view(), name='emp_feedback'),
    



]
