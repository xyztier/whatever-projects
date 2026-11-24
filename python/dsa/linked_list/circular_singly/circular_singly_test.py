### !!! NOTE !!!
### Please put this file (circular_singly_test.py) in the same folder and hierarchy as node.py,
### or the import may fail unless you configure Python's module search path.
from circular_singly import CircularSingly


cs = CircularSingly()

cs.add_last(9)
cs.add_last(7)
cs.add_last(5)

print("Added 9, 7, and 5\tTail %s -> head %s (%s)" % (
    str(cs.back().data), str(cs.front().data), cs.display()
))

cs.add_first(10)
print("Added 10 as new head\tTail %s -> head %s (%s)" % (
    str(cs.back().data), str(cs.front().data), cs.display()
))

cs.add_last(4)
print("Added 4 as new tail\tTail %s -> head %s (%s)" % (
    str(cs.back().data), str(cs.front().data), cs.display()
))

cs.add_before(7, 8)
print("Added 8 before 7\tTail %s -> head %s (%s)" % (
    str(cs.back().data), str(cs.front().data), cs.display()
))

cs.add_after(7, 6)
print("Added 6 after 7\t\tTail %s -> head %s (%s)" % (
    str(cs.back().data), str(cs.front().data), cs.display()
))

cs.add_before(10, 11)
print("Added 11 before 10\tTail %s -> head %s (%s)" % (
    str(cs.back().data), str(cs.front().data), cs.display()
))

cs.add_after(4, 3)
print("Added 3 after 4\t\tTail %s -> head %s (%s)" % (
    str(cs.back().data), str(cs.front().data), cs.display()
))

cs.add_after(3, 2)
print("Added 2 after 3\t\tTail %s -> head %s (%s)" % (
    str(cs.back().data), str(cs.front().data), cs.display()
))

cs.delete_front()
print("Deleted head\t\tTail %s -> head %s (%s)" % (
    str(cs.back().data), str(cs.front().data), cs.display()
))

cs.delete_back()
print("Deleted tail\t\tTail %s -> head %s (%s)" % (
    str(cs.back().data), str(cs.front().data), cs.display()
))

print("Popped front: %s\tTail %s -> head %s (%s)" % (
    str(cs.pop_front()), str(cs.back().data), str(cs.front().data), cs.display()
))

print("Popped back: %s\t\tTail %s -> head %s (%s)" % (
    str(cs.pop_back()), str(cs.back().data), str(cs.front().data), cs.display()
))

print("\nis_circular:", cs.is_circular())
