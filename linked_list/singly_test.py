from singly import Singly


s = Singly()

s.add_first(1)
s.add_first(2)
s.add_first(3)
s.add_first(4)
s.add_first("Head")
print(s.display())

s.delete_first()
print(s.display())

s.delete_last()
print(s.display())

s.add_last("Tail")
print(s.display())

s.add_before(4, 10)
print(s.display())

print(s.front())
print(s.rear())
