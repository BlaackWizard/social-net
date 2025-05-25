from typing import Annotated, List
from uuid import UUID

from dishka import FromComponent
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from social_net.subscription.application.all_followers import AllFollowers
from social_net.subscription.application.dto import FollowRequest, UnFollowRequest, AllFollowersRequest
from social_net.subscription.application.follow import Follow
from social_net.subscription.application.unfollow import UnFollow

router = APIRouter(
    prefix='/subscriptions',
    tags=['Подписка'],
    route_class=DishkaRoute,
)


@router.post("/follow") # type: ignore[misc]
async def follow_user(

    interactor: Annotated[Follow, FromComponent("subscription")],
    data: FollowRequest,
) -> None:
    await interactor.execute(data)

@router.post('/unfollow') # type: ignore[misc]
async def unfollow_user(
    interactor: Annotated[UnFollow, FromComponent("subscription")],
    data: UnFollowRequest
) -> None:
    await interactor.execute(data)

@router.get('/all-followers', response_model=List[UUID]) # type: ignore[misc]
async def get_all_followers(
    interactor: Annotated[AllFollowers, FromComponent("subscription")],
    data: AllFollowersRequest,
) -> List[UUID]:
    return list(await interactor.execute(data))
