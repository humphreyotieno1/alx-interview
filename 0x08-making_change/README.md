# Making Change

This is a Python function that determines the fewest number of coins needed to meet a given amount total, given a pile of coins of different values.

## Usage

The function takes two arguments:

- `coins`: a list of the values of the coins in your possession
- `total`: the target amount you want to reach

The function returns:

- the fewest number of coins needed to meet the `total` amount
- `0` if the `total` is 0 or less
- `-1` if the `total` cannot be met by any number of coins you have

## Example

```python
from 0-making_change import makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```
