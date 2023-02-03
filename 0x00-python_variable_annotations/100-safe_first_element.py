#!/usr/bin/env python3
"""use more duck-type annotations in function declarations"""


from typing import Iterable, Sequence, List, Tuple, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
