# tweet/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('tweet/', views.tweet, name='tweet'),  # 127.0.0.1:8000/tweet 과 views.py 폴더의 tweet 함수 연결
    path('tweet/delete/<int:id>', views.delete_tweet, name='delete-tweet'),
            # 게시글을 삭제 할 tweet앱의 views.py의 delete_tweet 함수를 만들었고, 저 함수를 url과 연결시켜 주었슴.
            # tweet/delete/<int:id> 는, tweet/delete/123 과 같이 맨 뒷자리에 숫자가 온다는 얘기이고, 이 숫자는 id에 담겨져 delete_tweet에 전달이 됩니다.
            # 이 id를 views.py의 delete_tweet(request,id) 에서 매개변수로 받아 사용을 할 수 있는 것 입니다.
    path('tweet/<int:id>', views.detail_tweet, name='detail-tweet'),
    path('tweet/comment/<int:id>', views.write_comment, name='write-comment'),
    path('tweet/comment/delete/<int:id>', views.delete_comment, name='delete-comment'),

]
