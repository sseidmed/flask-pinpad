
import random


class Pinpad:
    def __init__(self):
        self.per_row = 3
        self._digits = list(range(10))
        self._code = ['5', '9', '2', '3']

    @property
    def x(self):
        return self._digits

    def shuffle_digits(self):
        random.shuffle(self._digits)
        return self._digits

    def append_row(self):
        keypad = []
        while self._digits:
            row = self._digits[:self.per_row]
            self._digits = self._digits[self.per_row:]
            if len(row) < 3:
                row.insert(0, '✗')
                row.append('✓')
            keypad.append(row)
        return keypad
