from .utils import setup
from oaib import Auto


async def test_auto():
    batch = Auto(workers=8)

    for i in range(20):
        await batch.add("chat.completions.create", model="gpt-4", messages=[{"role": "user", "content": "say hello"}])

    chats = await batch.run()
    assert len(chats), "Chat batch should return results"
    print(chats)

    for i in range(20):
        await batch.add("embeddings.create", model="text-embedding-3-large", input="hello world")

    embeddings = await batch.run()
    assert len(embeddings), "Embeddings batch should return results"
    print(embeddings)

    embedding = embeddings.iloc[0].get("result")
    assert embedding['data'], "Should get valid embeddings"

    chat = chats.iloc[0].get("result")
    assert chat['choices'], "Should get valid chat completions"
