from dataclasses import dataclass

@dataclass
class DOG:
    num_legs = 4
    num_eyes = 2
    speech = "bark!"

print(DOG.num_legs)
