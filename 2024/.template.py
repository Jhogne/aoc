import re
import math
from functools import cache
from ast import literal_eval
from itertools import count, pairwise
from collections import defaultdict

with open('test.in', 'r') as f:
    lines = f.read().strip().splitlines()

