# OpenAI Batcher (`oaib`)

A Python library for making rate-limited, async batch requests to the OpenAI
API.

- Use `Batch` to make batch requests as quickly as possible given TPM/RPM
  limits.
- Use `Auto` to automatically read your rate limits from OpenAI's response
  headers, and run the job as fast as possible.

*This notebook is available at [README.ipynb](README.ipynb).*

## Usage

### Set OpenAI API Key


```python
import os
os.environ['OPENAI_API_KEY'] = input()
```

### Using the `Batch` class

You can mix and match endpoints as needed for regular `Batch`, but it's not
recommended as the rate limits for different endpoints/models will differ. For
maximum efficiency, use `Auto`.


```python
from oaib import Batch

# Use low rate limits for this example.
batch = Batch(rpm=100, tpm=1_000, workers=5)

# Creating a batch with 20 chat completions.
for i in range(20):
    await batch.add(
        "chat.completions.create", 
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": "say hello"}]
    )

await batch.run()
```


<pre style="font-size: 0.7rem">
✅ DONE: 100%|█████████████| 20/20 [00:22<00:00,  1.12s/req]
RPM:  53%|█████████████████████▏                  | 53.0/100
TPM:  93%|███████████████████████████████████▎  | 928.0/1000

Run took 20.02s.
</pre>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>endpoint</th>
      <th>model</th>
      <th>messages</th>
      <th>result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzMf7oXHlLWpsISVpAaUPxps0g5...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzNeFY9TLN71o2FMEqGssHIrOQq...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzNDiD3ikFtBZ4hHXWEsLONHUeS...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzP9dccsvrGsOR3X5HgmHqsR2fm...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzQV7ZnIoXccx9R8dIfS4rdPd0U...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzRVQvp3wwmEvbFzNPtrXBmcOhR...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzRSw7iTCLs0uu8fWZwDcaPGB0s...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzS6D1gACsJW6JXvuS42N4lQLh7...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzUFmpIzWjKsNGnlLvZW3DhF752...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzU6Mg6Zk4BC5uelndmHjmGAQ0I...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzV5K4OEk80dDuSwohiTualLOoO...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzXCcmbcuy1EQPskJrfN5po1Ix9...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzX4UfaBPDO3fF8vMO1dsQ6tfiT...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzZme2VBNhckfItEZRJqmpC3E53...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzaYddjxrFpmYUDjMHXlDPgS7G4...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzcTLFClvwjtPNNyv3KJ2xvZ8dQ...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzcuWlMUwqXj0AeMQkZqzNIQvJo...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzepfAhFnZj1AlnVSyNHHMyZ0mK...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzfdULvZx6OyUZpARpTMNKYzfKx...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVzfyEru2f67JyunYCdPMaC0fD2H...</td>
    </tr>
  </tbody>
</table>


### Using the `Auto` class

Automatically use the given TPM/RPM rate limits provided by OpenAI API
responses.


```python
from oaib import Auto

# Automatically set rate limits.
batch = Auto(workers=8)

# Fetch 1,000 chat completions as quickly as possible, setting rate limits
# automatically from OpenAI's response headers.
for i in range(1000):
    await batch.add(
        "chat.completions.create", 
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": "say hello"}]
    )

await batch.run()
```


<pre style="font-size: 0.7rem">
✅ DONE: 100%|█████████| 1000/1000 [00:10<00:00, 92.98req/s]
RPM:  56%|████████████████████                | 5573.0/10000
TPM:   5%|█▌                               | 94401.0/2000000

Run took 12.58s.
</pre>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>endpoint</th>
      <th>model</th>
      <th>messages</th>
      <th>result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVxz211nsiQQSY2k54r4r141UX83...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVy0TrnGax3XqkDOlEiImosPnvIL...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVxzMdsF5v1je6iAmvjK7BCZKQna...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVy0KiRWYPtQ099p3b1k1HfYBYwT...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVy0M7l6Fg0mvWCpOXomVSqV6Pow...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>995</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVyBemEPgb6lV5Opnu8X9UQ7T9iZ...</td>
    </tr>
    <tr>
      <th>996</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVyBBlh4PMbI9qtca80UyMbrOGAF...</td>
    </tr>
    <tr>
      <th>997</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVyBWveGsMeSLS5SzUbXIiMLvGaS...</td>
    </tr>
    <tr>
      <th>998</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVyBbBnX5SleJWSDIHqZ8lS0y15V...</td>
    </tr>
    <tr>
      <th>999</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'say hello'}]</td>
      <td>{'id': 'chatcmpl-8qVyBYTizFbBIu3RQ9XlvKDlnSuEG...</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 4 columns</p>


### Metadata and Index

You can add custom metadata to your observations with `add(metadata={...}`, and
set the index for the DataFrame with `Batch(index=[...])` and
`Auto(index=[...])`.


```python
from oaib import Batch

n = 5
batch = Batch(rpm=1000, tpm=10000, workers=5, index=["difficulty", "i"])
difficulties = ["easy", "medium", "hard"]

for difficulty in difficulties:
    for i in range(n):
        await batch.add(
            "chat.completions.create",
            metadata={"difficulty": difficulty, "i": i},
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user", 
                "content": f"difficulty: {difficulty}. write a math problem."
            }]
        )

await batch.run()
```

```
✅ DONE: 100%|█████████| 15/15 [00:01<00:00, 10.52req/s]
RPM:  56%|████████████████████                | 631.0/1000
TPM:     |                                    | 10781.0/?

Run took 1.43s.
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>endpoint</th>
      <th>model</th>
      <th>messages</th>
      <th>result</th>
    </tr>
    <tr>
      <th>difficulty</th>
      <th>i</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">easy</th>
      <th>0</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: easy...</td>
      <td>{'id': 'chatcmpl-8rdiFkLTnjs4LbX2ZUKyb1UaRcPwH...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: easy...</td>
      <td>{'id': 'chatcmpl-8rdiFtEcz6CEvO8K9jZpAdbFaaJ3o...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: easy...</td>
      <td>{'id': 'chatcmpl-8rdiFEmy4TfO4iR3aJbh4u9lgAD1W...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: easy...</td>
      <td>{'id': 'chatcmpl-8rdiFVw5YuHY8WhuNqJjyJcFO9Mhs...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: easy...</td>
      <td>{'id': 'chatcmpl-8rdiGoYqWA5wH3xoFKVl8pRGGTuDZ...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">hard</th>
      <th>0</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: hard...</td>
      <td>{'id': 'chatcmpl-8rdiG8ZAUhcsBOtgtPuOjblzEo14a...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: hard...</td>
      <td>{'id': 'chatcmpl-8rdiGgl9uEe4ASQgt5uzwMpeJhnU6...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: hard...</td>
      <td>{'id': 'chatcmpl-8rdiGfVkiZqrE1p2TxeKnCxc2zzUb...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: hard...</td>
      <td>{'id': 'chatcmpl-8rdiGdKxmYC6mS4QSuiW3HjsMRW05...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: hard...</td>
      <td>{'id': 'chatcmpl-8rdiGqTe3MVy8FGJ6qtVAjxmMODy6...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">medium</th>
      <th>0</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: medi...</td>
      <td>{'id': 'chatcmpl-8rdiGsk7ohvIVwzuFMfO3cH9zNLW4...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: medi...</td>
      <td>{'id': 'chatcmpl-8rdiG64Y66W8CZZ9MI4xiVNHheHiF...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: medi...</td>
      <td>{'id': 'chatcmpl-8rdiGGmXfXx0uRuKafeKODGQe42vz...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: medi...</td>
      <td>{'id': 'chatcmpl-8rdiG95XCozUiFXY7ryA4rSfzbwRk...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>chat.completions.create</td>
      <td>gpt-3.5-turbo</td>
      <td>[{'role': 'user', 'content': 'difficulty: medi...</td>
      <td>{'id': 'chatcmpl-8rdiGi6nF5FLMdPIYrkrYgI15Yfcw...</td>
    </tr>
  </tbody>
</table>
</div>

### Use with Microsoft Azure
<sub>See [`tests/test_azure.py`](tests/test_azure.py).</sub>

To use a Cognitive Services deployment:

#### 1. Go to to `Azure OpenAI Studio > Chat playground > View Code`.

This view will provide your Azure endpoint, API version, and API key.

#### 2. Use `AzureConfig` to configure the Azure endpoint.

With `AZURE_OPENAI_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_VERSION` env keys
set:

```python
from oaib import Batch, AzureConfig

# Auto is not supported for Azure.
azure = AzureConfig()
batch = Batch(azure=azure)
```

Or, manually:

```python
import os
from oaib import Batch, AzureConfig

azure = AzureConfig(
  azure_endpoint = "https://spellcraft.openai.azure.com/", 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-02-15-preview"
)

# Auto is not supported for Azure.
batch = Batch(azure=azure)
```


## Notes

1. It is not possible to perfectly guarantee the tokens per minute limit is not
   breached because we cannot know the total token usage until the response
   comes back.
   
   Use the `safety` param to set the rate limit tolerance.  By default it is set
   to 10%, and will wait until the predicted TPM (the current TPM plus the
   average number of tokens per request) drops below 90% of the limit.

  
2. By default, important logs are stored at `oaib.txt`.  This can be disabled
   using `loglevel=0`.

3. There's an error with TPM/RPM progress bar display in Jupyter Notebooks for
   the `Auto` class only. This is caused by a `tqdm.notebook` bug where only the
   initial totals (here, our limits) are used to calculate the width of the bar,
   and the `Auto` class updates these values only after the first request. The
   text percentage displays are accurate.

