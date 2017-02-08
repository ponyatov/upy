class Sym:
    tag = 'sym'
    def __init__(self, V):
        self.val = V ; self.nest = [] ; self.attr = {}
        self.text = '' ; self.data = '' ; self.bss = '' ; self.stack = '' 
    def __iadd__(self, o): self.nest.append(o) ; return self
    def __repr__(self): return self.head()
    def head(self):
        return '<%s:%s> @%s' % (self.tag, self.val, id(self))
    def dump(self, depth=0):
        S = '\n' + '\t' * depth + self.head()
#         for i in self.attr: S += ' %s=%s' % (i, self.attr[i])
        for j in self.nest: S += j.dump(depth + 1)
        return S
class Num(Sym): tag = 'num'
class Op(Sym):  tag = 'op'
