import json,datetime, asyncio, aiohttp, requests, math,time
import cProfile,pstats
import threading
import queue
import snakeviz

from urllib.parse import urlencode, urlunparse
print("Запускаем процесс "+str(datetime.datetime.now()))


#базовый урл без параметров
baseURL = "budget.gov.ru/epbs/registry/ubpandnubp/data"
#построитель URL
def build_url(base_url, params=None):
    if params is None:
        params = {}
    query_string = urlencode(params)
    url = urlunparse(('https', base_url, '', '', query_string, ''))
    return url

countPage =0

#кидаем первый запрос
response = requests.get(build_url(baseURL, {"pagesize":1}))
if response.status_code == 200:
    firstData = response.json()
    countElemToEPBS=firstData["recordCount"]
    countPage =math.ceil(countElemToEPBS/1000)

#очередь данных под запись
queue_data = queue.Queue()


#поток сохранения данных в файл
#в цикле мониторим наличие данных в очереди
def thrSaveToFile():
    while True:
        page, data = queue_data.get()
        if data is None:
            break
        print("Записываем файл по странице " + str(page))
        with open(f'logs/data{page}.json', 'w', encoding='utf-8') as fileForSave:
            json.dump(data.json(), fileForSave, ensure_ascii=False)
        queue_data.task_done()

def start_main():
    # проходим все страницы и сохраняем отдельные файлы по каждой странице
    # отдаем респонс в очередь данных
    for page in range(1,countPage+1):
        print("page "+str(page))
        response = requests.get(build_url(baseURL, {"pagesize": 1000, "pageNum": page}))
        print("2.Получили данные по странице "+str(page))
        if response.status_code == 200:
            queue_data.put((page,response))
        else:
           stop=1


save_thread = threading.Thread(target=thrSaveToFile)
save_thread.start()
cProfile.run('start_main()', 'profile_results.prof')
#start_main()

#ждем закрытия всех задач и закрываем поток
queue_data.join()
queue_data.put((None, None))
save_thread.join()


print("Завершаем процесс "+str(datetime.datetime.now()))