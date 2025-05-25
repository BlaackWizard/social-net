from dishka import Provider, Scope, provide

from social_net.subscription.adapters.db.config_loader import SubDBConfig


class SubscriptionConfigProvider(Provider): # type: ignore[misc]
    component = "subscription"
    scope = Scope.APP

    @provide # type: ignore[misc]
    def db(self) -> SubDBConfig:
        db_config = SubDBConfig.from_env()
        return db_config
