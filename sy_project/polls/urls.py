from django.urls import path

from . import views

# 아래와같이 urls.py 에 namespace를 할당해줌으로써 탬플릿태그 {% url %} 을 사용할때 어떤 앱의 뷰에서 url을 생성할지 알 수 있다.
app_name = 'polls' 

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]