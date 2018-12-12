from collections import namedtuple

CellBase = namedtuple("Cell", "x y")


class Cell(CellBase):
    power = None

    def _get_hundred_digit(self, number):
        return number // 100 % 10

    def calculate_power(self, grid_serial_number):
        if self.power is not None:
            return self.power
        rack_id = self.x + 10
        power_level = rack_id * self.y
        power_level += grid_serial_number
        power_level *= rack_id
        power_level = self._get_hundred_digit(power_level)
        power_level -= 5

        self.power = power_level
        return self.power
