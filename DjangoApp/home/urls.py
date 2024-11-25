from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('signout',views.signout, name="signout"),
    path('profile',views.profile, name="profile"),
    path('employee/delete/<int:id>', views.deleteEmployee, name="deleteEmployee"),
    path('employee/add', views.addEmployee, name="addEmployee"),
    path('employee/update/<int:id>',views.employeeUpdate, name="employeeUpdate")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
