from .utils import setup
from oaib import Batch


async def test_batch():
    batch = Batch(rpm=100, tpm=1000, workers=5)

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

    chat = chats.iloc[0].get("result")
    assert chat['choices'], "Should get valid chat completions"

    embedding = embeddings.iloc[0].get("result")
    assert embedding['data'], "Should get valid embeddings"


async def test_callback():
    n = 20
    batch = Batch(rpm=1000, tpm=10000, workers=5)

    async def callback(result):
        nonlocal counter
        counter = counter + 1

    counter = 0
    for i in range(n):
        await batch.add("chat.completions.create", model="gpt-4", messages=[{"role": "user", "content": "say hello"}])

    results = await batch.run(callback=callback)
    assert counter == n, "Callback should be called for each result"

    counter = 0
    for i in range(n):
        await batch.add("embeddings.create", model="text-embedding-3-large", input="hello world")

    results = await batch.run(callback=callback)
    assert counter == n, "Callback should be called for each result"
