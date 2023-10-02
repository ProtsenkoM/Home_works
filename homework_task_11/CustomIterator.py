
class CustomIterator():
    def __init__(self, sequence, start_idex, stop_idex) -> None:
        self.sequence = sequence
        self.start_index = start_idex
        self.stop_index = stop_idex

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_index <= self.stop_index:
            if self.start_index < len(self.sequence):
                result = self.sequence[self.start_index]
                self.start_index += 1
                return result
            else:
                raise StopIteration
        else:
            raise StopIteration
