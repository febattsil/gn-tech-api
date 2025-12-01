import json
import datetime
from django.shortcuts import render
from urllib.request import urlopen
from urllib.parse import urlencode

# Create your views here.
def index(request):

    if 'cidade' in request.POST:
        cidade = request.POST['cidade']
    else:
        cidade = 'Florianopolis'

    appid = '1af4f300eb9de42f3c51227897a6e713'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':cidade, 'appid': appid, 'units': 'metric'}
    query_string = urlencode(PARAMS)

    full_url = f"{URL}?{query_string}"

    with urlopen(full_url) as response:
        res = response.read()
    
    data = json.loads(res)

    descricao = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']
    dia = datetime.date.today()

    return render(request, 'gnweather/index.html', 
                  {'descricao': descricao, 'icon': icon, 'temp': temp, 'dia': dia, 'cidade': cidade})

