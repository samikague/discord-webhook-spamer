import asyncio

from utils.parser import parse
from flood import webhook_flood

async def main():
    file = input("Enter the webhooks file path(press enter for default file): ")
    text = input("Enter the message to flood: ")

    if file == "":
        file = "webhooks.txt"

    webhooks = await parse(file)

    # Проверяем если парсер вернул ошибку
    if isinstance(webhooks, dict) and 'error' in webhooks:
        print(webhooks["error"])
        return
    
    if not webhooks:
        print("No valid webhooks found.")
        return
    else:
        tasks = []
        for webhook in webhooks:
            task = asyncio.create_task(webhook_flood(webhook, text))
            tasks.append(task)

        if not tasks:
            print("No valid webhooks found after filtering.")
            return
            
        await asyncio.gather(*tasks)

asyncio.run(main())