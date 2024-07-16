from collections import deque
from queue import Queue

q = deque(["Oleh", "Ivan", "Ivan", "Serhii", "Artem"], maxlen=3)

q.reverse()
print(q)

q.pop()
print(q)

q.popleft()
print(q)

q.remove("Ivan")
print(q)

waitlist = Queue(maxsize=4)

waitlist.put('Erin')
waitlist.put('Samantha')
waitlist.put('Joe')
waitlist.put('Martin')

print(waitlist.queue)
print(waitlist.get())
print(waitlist.queue)