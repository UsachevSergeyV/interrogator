import json
import  datetime
import  asyncio
import httpx
import os
os.environ['PYTHONASYNCIODEBUG'] = '1'
#import aiohttp

print("Запускаем процесс")
print("считываем файл из конфигураций")
nameFileToSite = "site.json"
siteData =None
with open(nameFileToSite, "r", encoding="utf-8") as f:
    siteData =  json.load(f)["webSite"]
#каждому оъекту добавляем новые свойства в виде статуса и времени последнего запроса
siteData = [{**sd,"status":None, "dateLastCheck":None,"textError":None} for sd in siteData]

counter = 0
lock = asyncio.Lock()

#функция выполнения проверки, принимает элементы класса сайтов, по результатам прописывает в элемент класса время проверки, ошибку и проставляет статус
async def fetch(elm):
  global counter
  async with httpx.AsyncClient() as session:
    try:
        resp = session.get(elm["url"], timeout=5)
        elm["status"] = "Успех"
        elm["dateLastCheck"] = datetime.datetime.now()
        async with lock:
            counter += 1
            print(counter)
    except httpx.TimeoutException:
        elm["status"] = "Ошибка"
        elm["textError"] = "Ошибка по таймауту"
        elm["dateLastCheck"] = datetime.datetime.now()
        async with lock:
            counter += 1
            print(counter)
    except httpx.RequestError as err:
        elm["status"] = "Ошибка клиента"
        elm["textError"] =str(err)
        elm["dateLastCheck"] = datetime.datetime.now()
        async with lock:
            counter += 1
            print(counter)
    except Exception as err:
        print(err)




#создаем массив задач и сессию
async def fetchAll(siteData):

        tasks = [fetch(elm) for elm in siteData]
        return await asyncio.gather(*tasks)


#запускаем основной цикл
async def mainLoop():
    res = await fetchAll(siteData)


asyncio.run(mainLoop())

print(*siteData, sep="\n")
print("End")
