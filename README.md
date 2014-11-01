pyLruCache.py
====

```python

from pyLruCache import *
In [1]: from pyLruCache import *

In [2]: a = pyLruCache(3)

In [3]: for i in a.iteritems():
   ...:     print i
   ...:

In [4]: for i in ran
KeyboardInterrupt

In [4]:

In [4]: a[1] = 1

In [5]: a[2] = 2

In [6]: a[3] = 3

In [7]: for i in a.iteritems():
   ...:     print i
   ...:
(1, 1)
(2, 2)
(3, 3)

In [8]: a[4] = 4

In [9]: for i in a.iteritems():
    print i
   ...:
(2, 2)
(3, 3)
(4, 4)

In [10]: print a[2]
2

In [11]: a[5] = 5

In [12]: for i in a.iteritems():
    print i
   ....:
(4, 4)
(2, 2)
(5, 5)

In [13]: a[6] = []

In [14]: a[6].append(1)

In [15]: a[6].append(2)

In [16]: a[6].append(3)

In [17]: for i in a.iteritems():
    print i
   ....:
(2, 2)
(5, 5)
(6, [1, 2, 3])

In [18]: a[7]=7

In [19]: for i in a.iteritems():
    print i
   ....:
(5, 5)
(6, [1, 2, 3])
(7, 7)
```
## Installation
pyLruCache can be installed using Pypi, `pip install pyLruCache`

## Detail
现在暂时不支持list，有时间把列表也支持。 

