

class Bar:
    value : int

class Foo:
    x : int
    bar : List[Bar]


obj : Foo = from_json(json.loads('{"x": 123, "bar":[{"value": 3}, {"value": 2}, {"value": 1}]}'), Foo)
print(obj.x)
print(obj.bar[2].value)