import asyncio

async def simple_async_function():
    print("Начало выполнения")
    await asyncio.sleep(1)  # Ожидаем 1 секунду
    print("Конец выполнения")
    await asyncio.sleep(1)  # Ожидаем 1 секунду
    print("Конец выполнения")

# Запуск асинхронной функции
asyncio.run(simple_async_function())


import httpx
import asyncio

async def fetch(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.text

async def main():
    content = await fetch('https://www.example.com')
    print(content)

asyncio.run(main())