import json,datetime, asyncio, aiohttp, requests, math,time
from urllib.parse import urlencode, urlunparse
print("Запускаем процесс")
#параметр блока который нужно получить
paramblocks = "blocks=info"
#параметр размера страницы
paramPageSize ="pagesize=1"
#базовый урл без параметров
baseURL = "budget.gov.ru/epbs/registry/ubpandnubp/data"
#построитель URL
def build_url(base_url, params=None):
    if params is None:
        params = {}
    query_string = urlencode(params)
    url = urlunparse(('https', base_url, '', '', query_string, ''))
    return url

#первый урл дляполучения размера , получааем только 1 организацию
firstUrl = build_url(baseURL, {"pagesize":1})

countPage =0

#кидаем первый запрос
response = requests.get(firstUrl)
if response.status_code == 200:
    firstData = response.json()
    countElemToEPBS=firstData["recordCount"]
    countPage =math.ceil(countElemToEPBS/1000)


lock = asyncio.Lock()


for page in range(1,countPage+1):
    currentUrl = build_url(baseURL, {"pagesize": 1000, "pageNum": page})
    response = requests.get(currentUrl)
    if response.status_code == 200:
        with open(f'logs/data_{page}.json', 'w',encoding='utf-8') as fileForSave:
            json.dump(response.json(), fileForSave)
    else:
        with open(f'logs/error_{page}.json', 'w',encoding='utf-8') as fileForSave:
            fileForSave.write(response.status_code)




