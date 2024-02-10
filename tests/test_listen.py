from oaib import Batch
from oaib.utils import race

from asyncio import CancelledError
from asyncio import create_task, sleep, gather, wait


async def test_listen():
    batch = Batch(rpm=1000, tpm=10000, workers=16)

    async def run():
        batch.log("TEST | Running...")
        await sleep(10)
        batch.log("TEST | Done. Stopping.")
        await batch.stop()

    task = create_task(batch.listen())
    running = create_task(run())

    n = 5
    for i in range(n):
        await batch.add("chat.completions.create", model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"say hello! {i}"}])
        await sleep(1)

    await running
    print(batch.output)
    assert len(batch.output) == n, f"Should get {n} results"
