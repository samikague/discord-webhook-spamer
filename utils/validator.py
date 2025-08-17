import aiohttp

# Проверка доступности вебхука
async def check(webhook: str) -> bool:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(webhook) as response:
                if response.status == 200:
                    return True
                else:
                    return False
                
        except aiohttp.ClientError:
            return False
    
# Валидация ссылки на вебхук
async def validate(webhook) -> bool:
    if not webhook.startswith("https://discord.com/api/webhooks/"):
        return False
    
    if await check(webhook):
        return True
    else:
        return False