# One line of code for common task

### Example usage

```python
from timer import timer
from time import sleep

with timer() as t:
    sleep(5)

print(t)
```

```python
from quickbot import quickbot

quickbot(api_key, input_function).run()
```