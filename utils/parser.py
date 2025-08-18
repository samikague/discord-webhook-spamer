import aiofiles
import re

from utils.validator import validate

# Парсинг вебхуков из переданного файла
async def parse(webhook_file: str) -> list:
    webhooks = []
    pattern = re.compile(r"https?://(?:discord|discordapp)\.com/api/webhooks/\d{17,19}/[a-zA-Z0-9_-]+", re.IGNORECASE)

    try:
        async with aiofiles.open(webhook_file, mode='r') as file:
            content = await file.read()
            webhooks = pattern.findall(content)

    except FileNotFoundError:
        return {
            "error": "File not found. Please check the file path."
        }
    
    except Exception as e:
        return {
            "error": f"An error occurred while reading the file: {e}"
        }

    return webhooks
