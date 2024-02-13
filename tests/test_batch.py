from oaib import Batch


async def test_batch():
    n = 10
    batch = Batch(rpm=60, tpm=1000, workers=5)

    for i in range(n):
        await batch.add("chat.completions.create", model="gpt-3.5-turbo", messages=[{"role": "user", "content": "say hello"}])

    chats = await batch.run()
    assert len(chats) == n, f"Chat batch should return {n} results"
    print(chats)

    for i in range(n):
        await batch.add("embeddings.create", model="text-embedding-3-large", input="hello world")

    embeddings = await batch.run()
    assert len(embeddings) == n, f"Embeddings batch should return {n} results"
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
        await batch.add("chat.completions.create", model="gpt-3.5-turbo", messages=[{"role": "user", "content": "say hello"}])

    results = await batch.run(callback=callback)
    assert counter == n, "Callback should be called for each result"

    counter = 0
    for i in range(n):
        await batch.add("embeddings.create", model="text-embedding-3-large", input="hello world")

    results = await batch.run(callback=callback)
    assert counter == n, "Callback should be called for each result"
