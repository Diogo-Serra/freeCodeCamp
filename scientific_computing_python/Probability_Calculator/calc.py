import copy
import random


class Hat:
    def __init__(self, **kwargs):
        # Build contents as a flat list of color names
        self.contents = []
        for color, qty in kwargs.items():
            self.contents.extend([color] * int(qty))

        if len(self.contents) == 0:
            # Problem spec says a hat will always be created with at least one ball,
            # but guard anyway.
            raise ValueError("Hat must contain at least one ball.")

    def draw(self, num_balls):
        # If requesting more than available, return everything
        if num_balls >= len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn

        # Randomly draw without replacement and remove from contents
        drawn = random.sample(self.contents, num_balls)
        # Remove each drawn ball from contents one by one
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Returns the approximate probability of drawing at least the counts in expected_balls.
    """
    def meets_expectation(picks, expected_dict):
        # Count picks
        counts = {}
        for p in picks:
            counts[p] = counts.get(p, 0) + 1
        # Check at-least condition for each expected color
        for color, needed in expected_dict.items():
            if counts.get(color, 0) < needed:
                return False
        return True

    successes = 0

    for _ in range(num_experiments):
        # Work on a deep copy so original hat isn't modified
        trial_hat = copy.deepcopy(hat)
        picked = trial_hat.draw(num_balls_drawn)
        if meets_expectation(picked, expected_balls):
            successes += 1

    return successes / num_experiments if num_experiments > 0 else 0.0
