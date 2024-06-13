p = True
q = False
r = True

not p or q  # ~p or q == p -> q
not p or q and r  # ~p or (q and r)
