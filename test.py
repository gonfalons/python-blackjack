from dataclasses import dataclass
print(dir(dataclass))


@dataclass
class Foo:
    potato: int


foo = Foo(64)


class Bar:
    def __init__(self, foo: Foo):
        self.butter = foo.potato


bar = Bar(foo)
bar.butter
