import time
import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
 
    def size(self):
        return len(self.items)

    def simulate_line(self, till_show, max_time):
        person_in_line = Queue()
        tickets_sold = []

        for i in range(10):
            person_in_line.enqueue("Spider-Man " + str(i))

        time_end = time.time() + till_show
        now = time.time()

        while now < time_end and not person_in_line.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = person_in_line.dequeue()
            print(person)
            tickets_sold.append(person)

        return tickets_sold 

    
