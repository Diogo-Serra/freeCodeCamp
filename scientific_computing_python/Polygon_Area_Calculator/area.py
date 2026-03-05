class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Mutators
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    # Measures
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # ASCII picture
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        line = "*" * self.width
        return ("\n".join(line for _ in range(self.height))) + "\n"

    # Packing count (no rotation)
    def get_amount_inside(self, other):
        if other.width == 0 or other.height == 0:
            return 0
        fit_w = self.width // other.width
        fit_h = self.height // other.height
        return int(fit_w * fit_h)

    # String representation
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    # Keep square invariant when using rectangle-style setters
    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"
