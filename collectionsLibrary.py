from collections import Counter,namedtuple,OrderedDict,defaultdict,deque
from typing import DefaultDict
e = deque()
e.append(1)
e.appendleft(2)
e.extend([5,6,3,'cool'])
d = DefaultDict(int)
d["pehli"] = "prushat me"
d["rooko"] = "jara"
d[3] = 50
c = OrderedDict()
machkardi = {
    "patase": "headshot",
    "45": "50",
    "oh": "mukuni"
}
c["cool"] = "bro"
c["oh"] = "bete"
c[1] = 5
point = namedtuple('cool','x,y')
pt = point(1,-4)
a = 'aaaaaadfgh'
b = Counter(a)
print(b)
print(list(b.elements()))
print(pt)
print(c)
print(machkardi.get("mukuni","cool bro"))
print(d["me"])
print(e)