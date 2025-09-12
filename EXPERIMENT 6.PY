import random

class VacuumCleaner:
    def __init__(self):
        # Environment has 2 locations: A and B
        # Each may be "Dirty" or "Clean"
        self.environment = {
            "A": random.choice(["Dirty", "Clean"]),
            "B": random.choice(["Dirty", "Clean"])
        }
        self.location = "A"  # start at location A
        self.steps = 0

    def perceive(self):
        return self.location, self.environment[self.location]

    def action(self, percept):
        location, status = percept
        if status == "Dirty":
            print(f"Location {location} is Dirty. Cleaning...")
            self.environment[location] = "Clean"
        else:
            print(f"Location {location} is Clean. Moving...")
            self.location = "B" if location == "A" else "A"

    def run(self, max_steps=10):
        print("Initial Environment:", self.environment)
        for _ in range(max_steps):
            percept = self.perceive()
            self.action(percept)
            self.steps += 1
            print("Step:", self.steps, "| Environment:", self.environment, "| Location:", self.location)
            if all(status == "Clean" for status in self.environment.values()):
                print("\nAll locations are clean. Task completed!")
                break


if __name__ == "__main__":
    agent = VacuumCleaner()
    agent.run()
