class Sky:
    """
    silent night
    """

    def __init__(self, points):
        self.stars = points

        self.height, self.width, \
            self.min_x, self.min_y = self.calculate_heights(0)

        self.old_min_x = None
        self.old_min_y = None
        self.warned = False

    def calculate_heights(self, seconds):
        sorted_x = sorted(self.stars,
                          key=lambda x: x.get_position_at(seconds)[0])

        sorted_y = sorted(self.stars,
                          key=lambda x: x.get_position_at(seconds)[1])

        min_x = sorted_x[0].get_position_at(seconds)[0]
        max_x = sorted_x[len(sorted_x) - 1].get_position_at(seconds)[0]

        min_y = sorted_y[0].get_position_at(seconds)[1]
        max_y = sorted_y[len(sorted_y) - 1].get_position_at(seconds)[1]

        width = max_x - min_x + 1
        height = max_y - min_y + 1

        return height, width, min_x, min_y

    def calculate_star_position(self, x, y):
        return x - self.min_x, y - self.min_y

    def construct_sky(self, seconds):
        self.old_min_x = self.min_x
        self.old_min_y = self.min_y

        self.height, self.width, \
            self.min_x, self.min_y = self.calculate_heights(seconds)

        if self.old_min_x - self.min_x > 0:
            print("X difference is getting bigger!")
            self.warned = True

        if self.warned:
            exit()

        sky = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(" ")
            sky.append(row)

        for star in self.stars:
            star_x, star_y = star.get_position_at(seconds)
            x, y = self.calculate_star_position(star_x, star_y)
            sky[y][x] = "*"

        return sky

    def contains_negative_values(self, seconds):
        self.height, self.width, \
            self.min_x, self.min_y = self.calculate_heights(seconds)
        return self.min_x < 0 or self.min_y < 0

    def print(self, seconds):
        sky = self.construct_sky(seconds)
        to_print = ""
        for row in sky:
            to_print += "".join(row)
            to_print += "\n"

        print(to_print)


class Star:
    def __init__(self, position, velocity):
        self.vel_x, self.vel_y = velocity
        self.x, self.y = position

    def __repr__(self):
        return f"<Star x={self.x} y={self.y} vel_x={self.vel_x} vel_y={self.vel_y}>"  # noqa

    def get_position_at(self, seconds):
        return self.x + (self.vel_x * seconds), \
               self.y + (self.vel_y * seconds)

    @classmethod
    def from_text(cls, text):
        position_start = text[10:].split()
        position_x = int(position_start[0].rstrip(","))
        position_y = int(position_start[1].rstrip(">"))

        velocity_start = text.find("velocity=<")
        velocity_string = text[velocity_start + 10:].split(", ")

        vel_x = int(velocity_string[0])
        vel_y = int(velocity_string[1].rstrip(">"))

        return cls((position_x, position_y), (vel_x, vel_y))
