# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
len(d)

# TODO: deques can be iterated over
for x in d:
    print(x.capitalize())

# TODO: manipulate items from either end
d.pop()
d.popleft()
d.append(1)
d.appendleft(2)
print(d)
d.rotate(-2)

# TODO: use an index to get a particular item
d[0]