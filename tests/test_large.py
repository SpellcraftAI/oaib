import oaib


async def test_long():
    batch = oaib.Auto()

    n = 20
    m = 20
    for i in range(n):
        await batch.add(
            "chat.completions.create",
            model="gpt-3.5-turbo",
            max_tokens=4000,
            messages=[{"role": "user", "content": "say hello and goodbye " * m}]
        )

    chats = await batch.run()
    assert len(
        chats) == n, f"Chat batch should return {n} results, got {len(chats)}"

    chat = chats.iloc[0].get("result")
    assert chat['choices'], "Should get valid chat completions"

    chats
