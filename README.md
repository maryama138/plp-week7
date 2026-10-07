# Week 7 Assignment - Shopping List Manager

## Files

* `list_warmup.py` - Demonstrates list indexes, append, remove, and len.
* `shopping_list.py` - Provides a menu for adding, removing, showing, and finishing a shopping list.
* `list_report.py` - Prints a numbered shopping list, counts item names with more than 4 letters, and finds the longest item.

## Why check `in` before using `.remove()`?

Checking `in` first is safer because `.remove()` causes an error if the item is not in the list. Using `in` allows the program to check whether the item exists before trying to remove it, so the program can continue running without crashing.
