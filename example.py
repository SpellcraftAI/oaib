from asyncio import run
from oaib import Auto, Batch


async def example():
    # Use low rate limits for this example.
    batch = Auto(workers=8)

    # Creating a batch with 20 chat completions.
    for i in range(1000):
        await batch.add(
            "chat.completions.create",
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "say hello"}]
        )

    results = await batch.run()
    results.to_csv("test.csv")

run(example())
