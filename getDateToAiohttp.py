import json
import  datetime
import  asyncio
import aiohttp

print("Запускаем процесс")
print("считываем файл из конфигураций")
nameFileToSite = "site.json"
siteData =None
with open(nameFileToSite, "r", encoding="utf-8") as f:
    siteData =  json.load(f)["webSite"]
siteData = [{**sd,"status":None, "dateLastCheck":None,"textError":None} for sd in siteData]

counter = 0
lock = asyncio.Lock()

#функция выполнения проверки, принимает элементы класса сайтов, по результатам прописывает в элемент класса время проверки, ошибку и проставляет статус
async def fetch(elm,session):
    global counter
    try:
        resp = session.get(elm["url"], timeout=5)
        elm["status"] = "Успех"
        elm["dateLastCheck"] = datetime.datetime.now()
        async with lock:
            counter += 1
            print(counter)
    except asyncio.TimeoutException:
        elm["status"] = "Ошибка"
        elm["textError"] = "Ошибка по таймауту"
        elm["dateLastCheck"] = datetime.datetime.now()
        async with lock:
            counter += 1
            print(counter)
    except aiohttp.RequestError as err:
        elm["status"] = "Ошибка клиента"
        elm["textError"] = str(err)
        elm["dateLastCheck"] = datetime.datetime.now()
        async with lock:
            counter += 1
            print(counter)
    except Exception as err:
        print(err)




#создаем массив задач и сессию
async def fetchAll(siteData):
        ses=  aiohttp.client()
        tasks = [fetch(elm,ses) for elm in siteData]
        return await asyncio.gather(*tasks)


#запускаем основной цикл
async def mainLoop():
    res = await fetchAll(siteData)


asyncio.run(mainLoop())

print(*siteData, sep="\n")
print("End")
