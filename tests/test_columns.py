from oaib import Batch, AzureConfig

azure = AzureConfig()


async def test_columns():
    n = 20
    batch = Batch(rpm=1000, tpm=10000, workers=5, azure=azure)

    for i in range(n):
        await batch.add(
            "chat.completions.create",
            metadata={"id": i},
            model="Research",
            messages=[{"role": "user", "content": "say hello"}]
        )

    results = await batch.run()
    print(results)

    assert "id" in results.columns, "Should have id column"


async def test_index():
    n = 5
    batch = Batch(
        rpm=1000,
        tpm=10000,
        workers=5,
        index=["difficulty", "i"],
        azure=azure
    )

    difficulties = ["easy", "medium", "hard"]
    for difficulty in difficulties:
        for i in range(n):
            await batch.add(
                "chat.completions.create",
                metadata={"difficulty": difficulty, "i": i},
                model="Research",
                messages=[
                    {"role": "user", "content": f"difficulty: {difficulty}\nwrite a math problem."}
                ]
            )

    results = await batch.run()
    print(results)

    total = n * len(difficulties)
    assert len(results) == total, "Callback should be called for each result"
