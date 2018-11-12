from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comments
from . import Form
from django.template.context_processors import csrf    #кодировщик
from django.contrib import auth
from django.core.paginator import Paginator
from django.db.models import Q

def hello(request):
    return HttpResponse("Hello World")

def helloT(request):
    names = ["Yuliya", "Bob", "Alesha", "Valera", "Tom"]
    return render(request, "index.html", {"name": "Yuliya", "lastname": "Bulbenka", "names": names})

def Home(request):
    return render(request, "Main_templates.html")

def ShowVideos(request):
    search_query = request.GET.get('q', '')
    if search_query:
        Videos = Video.objects.filter(Q(Video_name__icontains=search_query) | Q(Video_properties__icontains=search_query))
    else:
        Videos = Video.objects.all()

    paginator = Paginator(Videos, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
        'username': auth.get_user(request).username
    }

    return render(request, 'AllVideos.html', context=context)


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
