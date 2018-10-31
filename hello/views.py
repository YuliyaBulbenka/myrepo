from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comments
from . import Form
from django.template.context_processors import csrf    #кодировщик
from django.contrib import auth


def hello(request):
    return HttpResponse("Hello World")

def helloT(request):
    names = ["Yuliya", "Bob", "Alesha", "Valera", "Tom"]
    return render(request, "index.html", {"name": "Yuliya", "lastname": "Bulbenka", "names": names})


def ShowVideos(request):
    content = []

    for vid in Video.objects.all():
        oneVid = [vid]
        oneVid.append(Comments.objects.filter(Comments_Video_id = vid.id))
        content.append(oneVid)
    return render(request, "AllVideos.html", {"content": content, "username": auth.get_user(request).username})

def ShowVideo(request, video_id):
    comment_form = Form.CommentForm
    args = {}
    args.update(csrf(request))
    args["video"] = Video.objects.get(id = video_id)
    args["Comments"] = Comments.objects.filter(Comments_Video_id = video_id)
    args["Form"] = comment_form
    args["username"] = auth.get_user(request).username
    return render(request, "OneVideo.html", args)


def AddLike(request, video_id):
    if video_id not in request.COOKIES:
        video = Video.objects.get(id=video_id)
        video.Video_likos += 1
        video.save()
        response = redirect("/AllVideos/get/" + str(video_id) + "/")
        response.set_cookie(video_id, "test")
        return response
    return redirect("/AllVideos/get/" + str(video_id) + "/")



def ajax(request):
    if request.GET:
        idvideo = request.GET['addlike']
        video = Video.objects.get(id=idvideo)
        video.Video_likos += 1
        video.save()
    return HttpResponse(video.Video_likos)


def AddCom(request, video_id):
    if request.POST:
        forma = Form.CommentForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit = False)
            comment.Comments_Video = Video.objects.get(id=video_id)
            forma.save()
    return redirect("/AllVideos/get/" + str(video_id) + "/")




# Create your views here.
