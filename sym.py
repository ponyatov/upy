class Sym:
    tag = 'sym'
    def __init__(self, V): self.val = V ; self.nest = [] ; self.attr = {}
    def __iadd__(self, o): self.nest.append(o) ; return self
    def __repr__(self): return self.head()
    def head(self):
        return '<%s:%s> @%s' % (self.tag, self.val, id(self))
    def dump(self, depth=0):
        S = '\n' + '\t' * depth + self.head()
        for i in self.attr:
            S += '\n' + '\t' * (depth + 1) + i + ' ='
            S += self.attr[i].dump(depth + 2)
        for j in self.nest: S += j.dump(depth + 1)
        return S
class Num(Sym): tag = 'num'
class Str(Sym): tag = 'str'
class Op(Sym):  tag = 'op'
