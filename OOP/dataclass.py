from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True, frozen=True)
class Person:
  sort_index: Any = field(init=False, repr=False)
  name: Any = "hamada"
  age: Any = 20
  height: Any = 1.40
  email: Any = "hamada@code"

  def __post_init__(self):
    object.__setattr__(self, "sort_index", self.age)


person1 = Person("ahmed", 40, 1.70, "ahmed@code.com")

person2 = Person("hamada", 35, 1.70, "ahmed@code.com")

print(person1 < person2)


@dataclass(frozen=True)
class Employee(Person):
  name: Any = "hany"
  age: Any = "80"
  job: Any = "developer"
  salary: Any = 3500


employee1 = Employee()
print(employee1.job)
