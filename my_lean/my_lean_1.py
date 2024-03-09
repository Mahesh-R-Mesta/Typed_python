import imp
from typing import Final, Any, Callable
from enum import Enum, auto

# enumarated
class Size(Enum):
    SMALL = 10
    MEDIUAM = 20
    LARGE = 30


Size.LARGE
Size.MEDIUAM


class Type(Enum):
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()


# constants
GRAVITY_CONSTANT: Final[float] = 9.8
ITEM_WEIGHT: Final[int | float] = 30

# variables
year: int = 365
mars_gravity: float = 12.4
name: str = "Hello world"
isEarth: bool = False
rocket: tuple[str, str, float] = ("Atlas", "4 engine", 1200.0)
name, engine_type, trust = rocket
path: list[float] = [1.023, 3.056, 6.76, 3.45, 8.98]
example_map: dict[str, Any] = {"name": "Hello world", "year": 2022}
print(example_map)
animals: set[str] = {"cat", "dog", "cow", "goat"}
animals.update(["cat", "elephent"])
example_map.values()
example_map.keys()
for key, name in example_map.items():
    print(f"{key}:{name}")
example_map.get("name")
print(animals)

first, *rest = [1, 2, 3, 5, 7, 8, 10]
print(first)
print(rest)


def get_force(weight: float) -> float:
    return weight * GRAVITY_CONSTANT


force: float = get_force(12)
print(f"gravity force : {force}")


def sum(num1: int, num2: int) -> int:
    return num1 + num2


divide: Callable[[int, int], int] = lambda x, y: x - y
multiply: Callable[[int, int], float] = lambda x, y: x * y

# we can also declare type keword as assigned variable
MathCallable = Callable[[int, int], float | int]


def calculate(num1: int, num2: int, callback: MathCallable) -> float | int:
    value: int | float = callback(num1, num2)
    return value


print(f"sum: {calculate(12, 14, sum)}")
v2 = calculate(14, 10, divide)
print(f"divide: {v2}")
v3 = calculate(12, 12, multiply)
print(f"multiply: {v3}")


class User:
    def __init__(self, fname, lname) -> None:
        self.f_name = fname
        self.l_name = lname

    def full_name(self):
        return self.f_name + " " + self.l_name


def createUser(fname: str, lname: str) -> User:
    return User(fname, lname)


user = createUser("mahesh", "mesta")
print(user.full_name())
