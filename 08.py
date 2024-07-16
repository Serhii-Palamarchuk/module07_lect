# iterator / iterable / generators

def simple_gen():
    yield "Ivan"
    yield "Oleh"
    yield "Petro"

for name in simple_gen():
    print(name)
