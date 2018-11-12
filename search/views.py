from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.views import View
from hello.models import Video
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


def search(request):
    #search_query = request.GET.get('q', '')

    #if search_query:
        #Videos = Video.objects.filter(Q(Video_name__icontains=search_query) | Q(Video_properties__icontains=search_query))
    #else:
        #Videos = Video.objects.all()

    Videos = Video.objects.all()
    paginator = Paginator('Videos', 3)

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
        'next_url': next_url
    }

    return render(request, 'search/search_rec.html', context=context)




# Create your views here.
