class Sym:
    tag = 'sym'
    def __init__(self, V): self.val = V ; self.nest = [] ; self.attr = {}
    def __repr__(self): return self.head()
    def head(self): return '<%s:%s> @%s' % (self.tag, self.val, id(self))
