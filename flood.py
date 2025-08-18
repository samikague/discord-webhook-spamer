import aiohttp
import termcolor
import asyncio

from utils.webhook_info import get_webhook_info
from utils.validator import check

from config import RATE_LIMIT, DEFAULT_WAIT

async def webhook_flood(webhook: str, text: str) -> None:
    data = await get_webhook_info(webhook)

    async with aiohttp.ClientSession() as session:
        while True:
            # Промежуточная проверка на валидность
            valid = await check(webhook)

            if not valid:
                print(termcolor.colored(f"[{data['name']}] INVALID WEBHOOK", "red"))
                return
            
            async with session.post(webhook,
                                    json={
                                        "content": text,
                                    }) as response:
                
                if response.status == 204:
                    print(termcolor.colored(f'[{data["name"]}] SUCCESS', 'green'))
                    await asyncio.sleep(DEFAULT_WAIT)

                elif response.status == 429:
                    print(termcolor.colored(f"[{data["name"]}] RATE LIMIT - WAIT {RATE_LIMIT} SEC", "red"))
                    await asyncio.sleep(RATE_LIMIT)