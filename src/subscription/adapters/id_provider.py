import aiohttp
from uuid import UUID
from fastapi import Request
from aiohttp import ClientError

from src.subscription.application.common.id_provider import IdProvider
from src.subscription.application.exceptions.subscription import AccessTokenOccurredError

class AuthClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")  # на всякий случай

    async def get_user_id(self, cookies: dict) -> UUID:
        url = f"{self.base_url}/auth/me"
        try:
            async with aiohttp.ClientSession(cookies=cookies) as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise AccessTokenOccurredError(f"Status code: {response.status}")
                    data = await response.json()
                    try:
                        return UUID(data["uid"])
                    except (KeyError, ValueError):
                        raise AccessTokenOccurredError("Invalid or missing 'uid'")
        except ClientError as e:
            raise AccessTokenOccurredError(f"{e}")

class HTTPRequestIdProvider(IdProvider):
    def __init__(self, request: Request, auth_client: AuthClient):
        self.request = request
        self.auth_client = auth_client

    async def get_follower_user_uuid(self):
        cookies = self.request.cookies
        return await self.auth_client.get_user_id(cookies)

