from typing import Annotated
from uuid import UUID

from dishka import FromComponent
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from src.subscription.application.all_followers import AllFollowers
from src.subscription.application.dto import FollowRequest, UnFollowRequest, AllFollowersRequest
from src.subscription.application.follow import Follow
from src.subscription.application.unfollow import UnFollow

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

@router.post('/unfollow')
async def unfollow_user(
    interactor: Annotated[UnFollow, FromComponent("subscription")],
    data: UnFollowRequest
) -> None:
    await interactor.execute(data)

@router.get('/all-followers')
async def get_all_followers(
    interactor: Annotated[AllFollowers, FromComponent("subscription")],
    data: AllFollowersRequest,
) -> list[UUID]:
    return await interactor.execute(data)
