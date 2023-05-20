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


quickbot(api_key, input_function).run() # /url for url input and /text for text input
```
#### Quickly create label telegram bot:
```python
from oneline.quickbot import labelbot, highlight_text


labelbot(api_key, jsonl_input_dir, jsonl_output_dir).run() # /a to get text and /b to label

# optional
highlight_function = highlight_text(highlight_list)
labelbot(api_key, jsonl_input_dir, jsonl_output_dir, highlight_function).run()
```
#### Quickly generation for seq2seq model:
```python
from oneline.quickgen import quickgen


pipeline = quickgen(huggingface_model_name)
pipeline.predict(text) # max_input_length = 1024, max_gen_length = 256
```
