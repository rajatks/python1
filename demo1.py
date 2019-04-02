def abc():
    print("Hi");
    yield 12;
    yield 22;

collection=abc();
print(collection.__next__())

for i in collection:
    print(i);

def cube():
    for i in range(1,11):
        yield i*i*i;

result=cube();

for i in result:
    print(i);
