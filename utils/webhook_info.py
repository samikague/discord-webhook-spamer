import aiohttp

async def get_webhook_info(webhook: str) -> dict:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(webhook) as response:
                if response.status == 200:
                    data = await response.json()
                    return {
                        "name": data.get("name"),
                        "id": data.get("id"),
                        "token": data.get("token")
                    }
                
                else:
                    return {"error": f"Failed to retrieve webhook info: {response.status}"}
                
        except aiohttp.ClientError as e:
            return {"error": f"Client error: {str(e)}"}