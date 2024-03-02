import os
import pytest
from oaib import Auto, Batch, AzureConfig

azure = AzureConfig()


async def test_azure():
    batch = Batch(workers=8, azure=azure, loglevel=2)

    n = 20
    for i in range(n):
        await batch.add(
            "chat.completions.create",
            model="Research",
            messages=[{"role": "user", "content": "say hello"}]
        )

    chats = await batch.run()
    assert len(chats) == n, f"Chat batch should return {n} results"
    print(chats)

    chat = chats.iloc[0].get("result")
    assert chat['choices'], "Should get valid chat completions"


async def test_azure_auto():
    with pytest.raises(ValueError, match="Auto does not support Azure"):
        auto_with_azure = Auto(azure=azure)
