from oaib import Auto, Batch


async def test_long():
    batch = Auto()

    # Large batch - Auto (fast)
    n = 5_000
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

    # Large batch - Batch (slow)
    batch = Batch()
    for i in range(n):
        await batch.add(
            "chat.completions.create",
            model="gpt-3.5-turbo",
            max_tokens=4000,
            messages=[{"role": "user", "content": "say hello and goodbye " * m}]
        )
