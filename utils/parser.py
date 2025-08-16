import aiofiles

from utils.validator import validate

# Парсинг вебхуков из файла webhooks.txt(базового)
async def parse(webhook_file):
    webhooks = []

    try:
        async with aiofiles.open(webhook_file, mode='r') as file:
            async for line in file:
                webhook = line.strip()
                if webhook and await validate(webhook):
                    if webhook not in webhooks:
                        webhooks.append(webhook)

    except FileNotFoundError:
        return {
            "error": "File not found. Please check the file path."
        }
    
    except Exception as e:
        return {
            "error": f"An error occurred while reading the file: {e}"
        }

    return webhooks
