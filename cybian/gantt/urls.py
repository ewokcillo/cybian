from django.conf.urls import url, patterns

urlpatterns = patterns('gantt.views',
        url('$', 'gantt', name='gantt')
)
