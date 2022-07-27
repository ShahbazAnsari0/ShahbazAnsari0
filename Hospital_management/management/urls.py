app_name = 'management'
from django.conf.urls import url
from django.conf.urls.static import static
from .import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
url(r'^login/',views.login,name="login"),
url(r'^signup/',views.signup,name="signup"),
url(r'^maps/',views.maps,name="maps"),
url(r'^visitor/',views.visitor,name="visitor"),
url(r'^appointment/',views.appointment,name="appointment"),
url(r'^organ/',views.organ,name="organ"),
url(r'^infrastructure/',views.infrastructure,name="infrastructure"),
url(r'^contact/',views.contact,name="contact"),
url(r'^confirmation/',views.confirmation,name="confirmation"),
url(r'^achievement/',views.achievement,name="achievement"),
url(r'^overview/',views.overview,name="overview"),
url(r'^logout/',views.logout,name="logout"),
url(r'^profile/',views.profile,name="profile"),
url(r'^home/',views.home,name="home"),
url(r'^slide/',views.slide,name="slide"),

]
