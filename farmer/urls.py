
from django.urls import path
from farmer import views
urlpatterns = [
     path('', views.login_or_register, name='login_or_register'),
    path('register',views.user_register ,name="register"),
    path('login',views.user_login,name="login"),
    path('user_dashboard',views.user_dashboard,name="user_dashboard"),
    path('user_product_add',views.user_product_add,name="user_product_add"),
    path('User_Product_details',views.User_Product_details,name="User_Product_details"),
    path('User_meeting',views.User_meeting,name="User_meeting"),
    # path('service',views.service,name="service"),
    path('logout',views.user_logout,name="logout"),
    path('update/<id>/',views.user_update,name="update"),
    path('agent-register',views.agent_register,name="agent_register"),
    path('agent-login',views.agent_login,name="agent_login"),
    path('agent-state',views.agent_state,name="agent_state"),
    path('agent_result',views.agent_table,name="agent_result"),
    path('update-user/<id>/',views.agent_update,name="update-user"),
    path('farmer_form/', views.farmer_form, name='farmer_form'),
    path('agent_logout',views.agent_logout,name="agent_logout"),
]
