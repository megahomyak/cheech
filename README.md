# Cheech

Cheech is a little program to require arguments from the command line

## Usage

```python
from cheech import require, WithDefault

apple, blueberry, cherry = require("apple", WithDefault("blueberry", None), "cherry")

print(apple, blueberry, cherry)
```
