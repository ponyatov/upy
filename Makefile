log.log: src.src py.py sym.py
	python py.py < $< > $@ && tail $(TAIL) $@