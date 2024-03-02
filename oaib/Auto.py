from asyncio import Event

from .Batch import Batch
from .utils import EXAMPLE, get_limits
# from .config import config


class Auto(Batch):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.azure:
            raise ValueError(
                "Auto does not support Azure or custom APIs. Manually set your TPM and RPM with Batch."
            )

        if "rpm" in kwargs or "tpm" in kwargs:
            raise ValueError(
                "Auto does not allow you to manually set your RPM or TPM. They will be set automatically using the limits provided by OpenAI's response headers."
            )

        self.__limits_loaded = Event()
        self.__model = None

    async def _process(self, *args, **kwargs):
        # If rate limits have not been loaded from response headers yet, do so.
        if self._headers is not None and not self.__limits_loaded.is_set():
            self.rpm, self.tpm = get_limits(self._headers)
            self.log(f"LIMITS FROM OPENAI | {self.rpm} RPM | {self.tpm} TPM")
            self.__limits_loaded.set()

        return await super()._process(*args, **kwargs)

    async def add(self, *args, **kwargs):
        model = kwargs.get("model")

        # Ensure all items in the Auto queue are the same type.
        if self.__model is None:
            self.__model = model

        elif model != self.__model:
            raise ValueError(
                f"Auto does not allow you to mix models.\nThis is a {self.__model} queue, but you are trying to add a {model} job.\nFill the queue with only one model at a time, and then `await batch.run()` to process them.\n{EXAMPLE}"
            )

        return await super().add(*args, **kwargs)

    async def _cleanup(self):
        self._headers = None

        self.__limits_loaded.clear()
        self.__model = None

        return await super()._cleanup()
