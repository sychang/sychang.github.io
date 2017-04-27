"""cve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/([0-9]+)/$', views.get_user, name="get_user"),
    url(r'^user/new/$', views.create_user, name="create_user"),
    url(r'^network/view/$', views.view_network, name="view_network"),
    url(r'^network/add$', views.add_to_network, name="add_to_network"),
    url(r'^network/remove$', views.remove_from_network, name="remove_from_network"),
    url(r'^tasks/$', views.list_tasks, name="list_tasks"),
    url(r'^task/([0-9+])/$', views.get_task, name="get_task"),
    url(r'^task/new/$', views.create_task, name="create_task"),
    url(r'^reviews/view$', views.view_reviews, name="view_reviews"),
    url(r'^network/post$', views.create_review, name="create_review"),
    url(r'^messages/all/$', views.all_messages, name="all_messages"),
    url(r'^messages/thread/([0-9])+/$', views.view_thread, name="view_thread"),
    url(r'^messages/compose/$', views.compose_message, name="compose_message"),
    url(r'^verify/generate$', views.generate_token, name="generate_token"),
    url(r'^verify/verify$', views.verify_token, name="verify_token"),
]
