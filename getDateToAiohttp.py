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
n=1
siteData = [{**sd,"status":None, "dateLastCheck":None,"textError":None, "NPP":0,"statusCode":None} for sd in siteData]
for sd in siteData:
    sd["NPP"]=str(n)
    n=n+1

counter = 0
lock = asyncio.Lock()

#функция выполнения проверки, принимает элементы класса сайтов, по результатам прописывает в элемент класса время проверки, ошибку и проставляет статус
async def fetch(elm,session):
    global counter
    try:
        resp = await session.get(elm["url"], timeout=5)
        elm["status"] = "Успех"
        statusCode = resp.status
        elm["dateLastCheck"] = datetime.datetime.now()
        elm["statusCode"] =statusCode
        async with lock:
            counter += 1
            print(str(counter) +" "+ elm["NPP"])
    except asyncio.TimeoutError:
        elm["status"] = "Ошибка"
        elm["textError"] = "Ошибка по таймауту"
        elm["dateLastCheck"] = datetime.datetime.now()
        async with lock:
            counter += 1
            print(str(counter) +" "+ elm["NPP"])
    except aiohttp.ClientError  as err:
        elm["status"] = "Ошибка клиента"
        elm["textError"] = str(err)
        elm["dateLastCheck"] = datetime.datetime.now()
        async with lock:
            counter += 1
            print(str(counter) +" "+ elm["NPP"])





#создаем массив задач и сессию
async def fetchAll(siteData):
    async with aiohttp.ClientSession() as ses:
        tasks = [fetch(elm,ses) for elm in siteData]
        return await asyncio.gather(*tasks)


#запускаем основной цикл
async def mainLoop():
    res = await fetchAll(siteData)


while(True):
    asyncio.run(mainLoop())
    comand = input()
    if comand=="exit":
        break

#print(*siteData, sep="\n")
print("End")
