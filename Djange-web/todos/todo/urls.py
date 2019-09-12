

import views
from django.conf.urls import patterns,url,include
from models import Todo

urlpatterns = patterns('',
                       (r'^$',views.todo_index),
                       (r'^add$',views.add_todo),
                       
                       (r'^(?P<object_id>\d+)$',update_object,
                        {'model':Todo,
                        'template_name':'templates/todo_form.html',
                        'post_save_redirect':'/todos/%(id)s',
                        }),

                        (r'^(?P<object_id>\d+)/delete$',
                         delete_object,
                         {'model':Todo,
                         'template_name':'template/todo_confirm_delete.html',
                         'post_delete_redirect':'..',}),)