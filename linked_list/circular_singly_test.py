from circular_singly import CircularSingly


cs = CircularSingly()

cs.add_last(9)
cs.add_last(8)
cs.add_last(7)

print(cs.display())
print("Tail with value %s is linked to head with value %s" % (
    str(cs.back().data), str(cs.front().data)
))

cs.add_first(10)

print(cs.display())
print("Tail with value %s is linked to head with value %s" % (
    str(cs.back().data), str(cs.front().data)
))

cs.add_last(6)

print(cs.display())
print("Tail with value %s is linked to head with value %s" % (
    str(cs.back().data), str(cs.front().data)
))