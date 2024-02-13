from oaib import Auto


async def test_auto():
    batch = Auto(workers=8)

    n = 20
    for i in range(n):
        await batch.add("chat.completions.create", model="gpt-3.5-turbo", messages=[{"role": "user", "content": "say hello"}])

    chats = await batch.run()
    assert len(chats) == n, f"Chat batch should return {n} results"
    print(chats)

    for i in range(n):
        await batch.add("embeddings.create", model="text-embedding-3-large", input="hello world")

    embeddings = await batch.run()
    assert len(embeddings) == n, "Embeddings batch should return {n} results"
    print(embeddings)

    embedding = embeddings.iloc[0].get("result")
    assert embedding['data'], "Should get valid embeddings"

    chat = chats.iloc[0].get("result")
    assert chat['choices'], "Should get valid chat completions"
