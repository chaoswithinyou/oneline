# One line of code for common task

### Installation
#### Install from source
```
pip install git+https://github.com/chaoswithinyou/oneline
```
#### Editable install
```
git clone https://github.com/chaoswithinyou/oneline
cd oneline
pip install -e .
```
### Example usage
#### Mesure execution time:
```python
from oneline.timer import timer
from time import sleep

with timer() as t:
    sleep(5)

print(t)
```
#### Quickly test news API with telegram bot:
```python
from oneline.quickbot import quickbot

quickbot(api_key, input_function).run()
```
#### Quickly generation for seq2seq model:
```python
from oneline.quickgen import quickgen

pipeline = quickgen('VietAI/vit5-base-vietnews-summarization')
pipeline.predict(text)
```
