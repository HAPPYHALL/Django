from django.shortcuts import render, redirect
from .models import TweetModel,TweetComment  # 글쓰기 모델 -> 가장 윗부분에 적어주세요!
from django.contrib.auth.decorators import login_required #게시글 삭제시, 로그인 한 사용자만 접근이 가능하게 하는 login_required 기능


# Create your views here.
def home(request):
    user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인이 되어있는지)
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')


def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # 사용자가 인증을 받았는지 (로그인이 되어있는지)
        if user:  # 로그인 한 사용자라면
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html', {'tweet': all_tweet})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/sign-in')

    elif request.method == 'POST':  # 요청 방식이 POST 일때
        user = request.user  # 현재 로그인 한 사용자를 불러오기
        my_tweet = TweetModel()  # 글쓰기 모델 가져오기
        my_tweet.author = user  # 모델에 사용자 저장
        my_tweet.content = request.POST.get('my-content', '')  # 모델에 글 저장
        my_tweet.save()
        return redirect('/tweet')


@login_required     #게시글 삭제시, 로그인 한 사용자만 접근이 가능하게 하는 login_required 기능. 함수의 인자에 request 외에 id 가 추가되었습니다!
def delete_tweet(request, id):                                     #  이 id는 게시글 고유의 id로써 게시글을 구분 하는 데에 사용 할 변수에요!
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')




#detail_tweet / write_comment / delete_comment 작성

@login_required
def detail_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
    return render(request,'tweet/tweet_detail.html',{'tweet':my_tweet,'comment':tweet_comment})


@login_required
def write_comment(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment","")
        current_tweet = TweetModel.objects.get(id=id)

        TC = TweetComment()
        TC.comment = comment
        TC.author = request.user
        TC.tweet = current_tweet
        TC.save()

        return redirect('/tweet/'+str(id))


@login_required
def delete_comment(request, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect('/tweet/'+str(current_tweet))