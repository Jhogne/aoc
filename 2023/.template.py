import re
import math
from functools import lru_cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().strip().splitlines()

