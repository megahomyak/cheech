# Cheech

Cheech is a little program to get arguments from the command line

## Usage

```python
from cheech import require, Arg

apple, blueberry, cherry = require("apple", Arg("blueberry", default=None), "cherry")

print(apple, blueberry, cherry)
```
