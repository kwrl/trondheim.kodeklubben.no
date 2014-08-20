from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView

from class_based_auth_views.views import LoginView
from usermanagement.views import LogoutView
from usermanagement.forms import UserAuthenticationForm

from rest_framework import viewsets, routers

from newsfeed.views import NewsView
from courses.views import CourseView, FullCourseView
from usermanagement.forms import UserCreateForm
from usermanagement.views import UserCreateView

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'api_news',NewsView, base_name='news')
router.register(r'api_courses',CourseView, base_name='courses')
router.register(r'api_courses_full', FullCourseView, base_name='courses_full')
#router.register(r'users', UserView, base_name='users')
#router.register(r'users', LoginView, base_name='login')

urlpatterns = patterns('',
    #url(r'^', include(router.urls)),
    url(r'^$', include('frontpage.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'tinymce/', include('tinymce.urls')),
    url(r'^login/', LoginView.as_view(template_name="login_screen.html", form_class=UserAuthenticationForm), name="log_in"),
    url(r'^logout/', LogoutView.as_view(template_name="logout_screen.html"), name="log_out"),
    url(r'^register/', UserCreateView.as_view(),name="register"),
    url(r'^courses/', include('courses.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
