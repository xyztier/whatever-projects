# The Josephus Problem is where n people stand in a circle,
# and every kth person is eliminated in a loop until only one survivor remains.

# Have this in the same folder of your circular_singly, or whatever list you use
from circular_singly import CircularSingly


n = 10
k = 2

# Initialize new Circular Singly linked list with `n` nodes
cs = CircularSingly()
for i in range(n):
    cs.add_last(i)
  
print(f"k = {k}\nStart: {cs.display()}\n")


count = 0
current_node = cs.front() # Start with head node


while True:

    # Increment count
    # `% k` ensures count max value is k-1, so it never exceeds k
    count = (count + 1) % k

    # This is the kth node being eliminated
    if count % k == 0:
        data = current_node.data
        cs.delete(current_node)
        #print(f"Removed {data} -> ({cs.display()})")

    # 1 node remaining, exit loop
    if cs.size() == 1:
        break

    # Move to next node
    current_node = current_node.next_node
    

# Display last node
print(f"\nSurvivor: {cs.display()}")
