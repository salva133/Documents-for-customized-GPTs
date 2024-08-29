import random

class Character:
    def __init__(self, name, generation, clan, attributes, skills, disciplines):
        self.name = name
        self.generation = generation
        self.clan = clan
        self.attributes = attributes  # Dictionary of attributes (e.g., {"Strength": 2, "Dexterity": 3})
        self.skills = skills  # Dictionary of skills (e.g., {"Melee": 2, "Stealth": 2})
        self.disciplines = disciplines  # Dictionary of disciplines (e.g., {"Thaumaturgy": 3, "Auspex": 2})

    def roll(self, pool_size):
        """Rolls a number of d10 equal to the pool size and returns the number of successes."""
        successes = 0
        for _ in range(pool_size):
            result = random.randint(1, 10)
            if result >= 6:
                successes += 1
            if result == 10:  # Critical success
                successes += 1
        return successes

    def check_attribute(self, attribute_name, skill_name=None):
        """Performs a check using an attribute and optionally a skill."""
        pool_size = self.attributes.get(attribute_name, 0)
        if skill_name:
            pool_size += self.skills.get(skill_name, 0)
        return self.roll(pool_size)

    def use_discipline(self, discipline_name):
        """Performs a check using a vampire discipline."""
        pool_size = self.disciplines.get(discipline_name, 0)
        return self.roll(pool_size)


# Example of how to create a character and perform checks

# Create a character
attributes = {"Strength": 2, "Dexterity": 3, "Intelligence": 3}
skills = {"Melee": 2, "Stealth": 2, "Occult": 4}
disciplines = {"Thaumaturgy": 3, "Auspex": 2}