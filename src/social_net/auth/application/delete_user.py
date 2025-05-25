from social_net.auth.application.common.id_provider import IdProvider
from social_net.auth.application.common.uow import UoW
from social_net.auth.application.dto.user import UserRegisterResponse


class DeleteUser:
    def __init__(
        self,
        uow: UoW,
        id_provider: IdProvider,
    ):
        self.uow = uow
        self.idp = id_provider

    async def execute(self) -> UserRegisterResponse:
        user = await self.idp.get_user()

        await self.uow.delete(user)
        await self.uow.commit()

        return UserRegisterResponse(
            message="Аккаунт удален.",
        )
