#!/usr/bin/env python3

#!/usr/bin/env python3


#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if type(size) == int:
            self.size = size
        else:
            print("size must be an integer")

    def get_size(self):
        return self._size

    def set_size(self, size_value):
        if type(size_value) == int:
            self._size = size_value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    size = property(get_size, set_size)


stan_smith = Shoe("Adidas", 19)
stan_smith.size = "pp"