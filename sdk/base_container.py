from email.policy import default
from decouple import config
from dependency_injector import containers, providers

from sdk.db.pg_client import PgClient
from sdk.services.cache_service import CacheService
from sdk.services.coingecko_service import CoingeckoService
from sdk.services.etherscan_service import EtherscanService
from sdk.services.redis_client import RedisClient
from sdk.services.rest_client import RestClient
from sdk.services.web3_service import Web3Service
from sdk.services.client_service import ClientService


class BaseContainer(containers.DeclarativeContainer):
    POSTGRES_URI = config("POSTGRES_URI", default=None)
    ETHERSCAN_API_KEY = config("ETHERSCAN_API_KEY", default=None)
    ETHERSCAN_BASE_URL = config("ETHERSCAN_BASE_URL", default=None)
    REDIS_URI = config("REDIS_URI", default="redis://localhost")
    PORT = config("PORT", default=3001, cast=int)
    WEB3_PROVIDER_URL = config("WEB3_PROVIDER_URL", default=None)
    EK_PLUGIN_ID = config("EK_PLUGIN_ID", default=None)
    
    redis_client = providers.Singleton(
        RedisClient,
        uri=REDIS_URI
    )

    rest_client = providers.Singleton(
        RestClient,
    )

    pg_client = providers.Singleton(
        PgClient,
        uri=POSTGRES_URI,
    )

    coingecko_service = providers.Singleton(
        CoingeckoService,
        rest_client=rest_client
    )

    etherscan_service = providers.Singleton(
        EtherscanService,
        api_key=ETHERSCAN_API_KEY,
        base_url=ETHERSCAN_BASE_URL,
        rest_client=rest_client
    )

    cache_service = providers.Singleton(
        CacheService,
        redis_client=redis_client,
    )

    web3_service = providers.Singleton(
        Web3Service,
        provider_url=WEB3_PROVIDER_URL,
    )

    client_service = providers.Singleton(
        ClientService,
        port=PORT,
        plugin_id=EK_PLUGIN_ID
    )