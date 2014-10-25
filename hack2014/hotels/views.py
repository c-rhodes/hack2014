import requests
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def Hotels(request):
    context = RequestContext(request)
    context_dict = {} 

    lat = '53.476621'
    long = '-2.253648'
    url = 'https://sandbox.api.tlrg.io/v1/mobile/search/location/' + lat + ',' + long + '/'
    headers = {'API-Key': 'JufM0RVUtJT9ZU8HDAmOg4mGThA78qPn'}

    r = requests.get(url, headers=headers)

    if not r.ok:
        context_dict['error'] = 'Whoops'
    else:
        search_results = r.json()
        context_dict['hotels'] = search_results['results']

    return render_to_response('hotels/hotels.html', context_dict, context)
