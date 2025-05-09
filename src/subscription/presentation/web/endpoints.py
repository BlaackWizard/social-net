from typing import Annotated

from dishka import FromComponent
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from src.subscription.application.follow import Follow, FollowRequest

router = APIRouter(
    prefix='/subscriptions',
    tags=['Подписка'],
    route_class=DishkaRoute,
)


@router.post("/follow")
async def follow_user(
    interactor: Annotated[Follow, FromComponent("subscription")],
    data: FollowRequest,
) -> None:
    await interactor.execute(data)
