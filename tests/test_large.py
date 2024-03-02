from oaib import Auto, Batch, AzureConfig

azure = AzureConfig()


async def test_large_auto():
    batch = Auto()

    # Large batch - Auto (fast)
    n = 1_000
    m = 10
    for i in range(n):
        await batch.add(
            "chat.completions.create",
            model="gpt-3.5-turbo",
            max_tokens=4000,
            messages=[{"role": "user", "content": "say hello and goodbye " * m}]
        )

    chats = await batch.run()
    assert len(chats), f"Chat batch should return results"

    chat = chats.iloc[0].get("result")
    assert chat['choices'], "Should get valid chat completions"


async def test_large_batch():
    batch = Batch(azure=azure)

    # Large batch - Batch (slow)
    n = 5_000
    m = 10

    for i in range(n):
        await batch.add(
            "chat.completions.create",
            model="gpt-3.5-turbo",
            max_tokens=4000,
            messages=[{"role": "user", "content": "say hello and goodbye " * m}]
        )
