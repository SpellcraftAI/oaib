from os import environ
from types import SimpleNamespace


class AzureConfig(SimpleNamespace):
    def __init__(
        self,
        azure_endpoint: str or None = environ.get("AZURE_OPENAI_ENDPOINT"),
        api_version: str or None = environ.get("AZURE_OPENAI_VERSION"),
        api_key: str or None = environ.get("AZURE_OPENAI_KEY"),
    ):
        super().__init__(
            azure_endpoint=azure_endpoint,
            api_version=api_version,
            api_key=api_key
        )
