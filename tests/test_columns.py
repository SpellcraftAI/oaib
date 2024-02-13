from oaib import Batch


async def test_columns():
    n = 20
    batch = Batch(rpm=1000, tpm=10000, workers=5)

    for i in range(n):
        await batch.add(
            "chat.completions.create",
            metadata={"id": i},
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "say hello"}]
        )

    results = await batch.run()
    print(results)

    assert "id" in results.columns, "Should have id column"


async def test_index():
    n = 5
    batch = Batch(rpm=1000, tpm=10000, workers=5, index=["difficulty", "i"])
    difficulties = ["easy", "medium", "hard"]

    for difficulty in difficulties:
        for i in range(n):
            await batch.add(
                "chat.completions.create",
                metadata={"difficulty": difficulty, "i": i},
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"difficulty: {difficulty}\nwrite a math problem."}
                ]
            )

    results = await batch.run()
    print(results)

    total = n * len(difficulties)
    assert len(results) == total, "Callback should be called for each result"
