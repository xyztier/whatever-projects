from linear_queue import LinearQueue
from circular_queue import CircularQueue
from priority_queue import PriorityQueue
from deque import Deque


def run_linear_queue():
    lq = LinearQueue()
    given = [ 2, 4, 6, 8, "La Peace", 10, 1, 3, 5, 7.6, 9, True ]
    
    # enqueue all items in `given`
    for i in range(len(given)):
        lq.enqueue(given[i])
    
    print("========== LINEAR QUEUE ==========")
    print(f"Display: {lq.display()}")
    print(f"Dequeue: {lq.dequeue()}")
    print(f"Dequeue: {lq.dequeue()}")
    print(f"Display: {lq.display()}")
    new_data = 100
    lq.enqueue(new_data)
    print(f"Enqueue: {new_data}")
    print(f"Display: {lq.display()}")


def run_circular_queue():
    cq = CircularQueue()
    given = [ -5, 123, "Christ", "is", "King", 420, 68, "paparapapa", -1.9, False ]
    
    # enqueue all items in `given`
    for i in range(len(given)):
        cq.enqueue(given[i])
        
    print("\n========== CIRCULAR QUEUE ==========")
    print(f"Display: {cq.display()}")
    print(f"Circular: {cq.is_circular()}")
    print(f"Dequeue: {cq.dequeue()}")
    print(f"Dequeue: {cq.dequeue()}")
    print(f"Display: {cq.display()}")
    print(f"Circular: {cq.is_circular()}")
    new_data = 12345
    cq.enqueue(new_data)
    print(f"Enqueue: {new_data}")
    print(f"Display: {cq.display()}")
    print(f"Circular: {cq.is_circular()}")


def run_deque():
    dq = Deque()
    given_front = [ 11, 22, 33, 44, 55, 66, ]
    given_rear = [ 67, 77, 88, 99, 111, "?" ]
    
    # enqueue_front all items in `given_front`
    for i in range(len(given_front)):
        dq.enqueue_front(given_front[i])
        
    print("\n========== DEQUE ==========")
    print(f"Display: {dq.display()}")
        
    # enqueue_rear all items in `given_rear`
    for i in range(len(given_rear)):
        dq.enqueue_rear(given_rear[i])
        
    print("Enqueued all items in `given_front`")
    print(f"Display: {dq.display()}")
    print(f"Dequeue front: {dq.dequeue_front()}")
    print(f"Dequeue rear: {dq.dequeue_rear()}")
    print(f"Display: {dq.display()}")
    new_data = "hi"
    dq.enqueue_front(new_data)
    print(f"Enqueue front: {new_data}")
    print(f"Display: {dq.display()}")
    print(f"Dequeue rear: {dq.dequeue_rear()}")
    print(f"Dequeue front: {dq.dequeue_front()}")
    print(f"Display: {dq.display()}")
    newer_data = "hello"
    dq.enqueue_rear(newer_data)
    print(f"Enqueue rear: {newer_data}")
    print(f"Display: {dq.display()}")
    

def run_priority_queue():
    pq = PriorityQueue()
    given = [
        (1, 169), (7, "profile"), (6, "in"), (5, "Discord"), (4, "join"), (2, "pls"),
        (4, "my"), (5, "link"), (1, 1),
    ] # (priority, data)

    # enqueue all entries in `given`
    # you can very muchc change how you input stuff, but i find this easier to debug
    for i in range(len(given)):
        entry = given[i]              # get the entry; for example, given[0] is (1, 169) and given[2] is (7, 12)
        priority = entry[0]           # get the first item; for example, if entry is (1, 169), entry[0] is 1
        data = entry[1]               # get the second item; for example, if entry is (7, 12), entry[1] is 12
        pq.enqueue(priority, data)

    print("\n========== PRIORITY QUEUE ==========")
    print(f"Priority of each entry:\t\t\t{pq.display_priority()}")
    print(f"Data entries (sorted by priority):\t{pq.display_data()}")
    print(f"Priority and data:\t\t\t{pq.display_all()}")
    

run_linear_queue()
run_circular_queue()
run_deque()
run_priority_queue()
