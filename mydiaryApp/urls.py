from django.urls import path, include
from .views import helloAPI
from .views import randomCorpusAPI
from .views import totalCorpusAPI

urlpatterns = [
    path('hello/',helloAPI),#helloAPI의 url설정. http://49.50.173.73:8000/mydiary/hello/
    path('<int:id>/', randomCorpusAPI), # http://49.50.173.73:8000/mydiary/2/
    path('list/', totalCorpusAPI), #http://49.50.173.73:8000/mydiary/list/
]