from dishka import Provider, Scope, provide

from src.subscription.adapters.db.config_loader import SubDBConfig


class SubscriptionConfigProvider(Provider):
    component = "subscription"
    scope = Scope.APP

    @provide
    def db(self) -> SubDBConfig:
        db_config = SubDBConfig.from_env()
        return db_config
