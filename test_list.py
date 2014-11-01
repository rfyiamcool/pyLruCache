from pyLruCache import pyLruListCache

a = pyLruListCache(5)


for i in range(100):
    a.appendd(i)
