class Queue:
    def __init__(self):
        self.values: list = []

    def insert(self, value):
        if value is None:
            raise Exception('Value can not be None')
        else:
            self.values.append(value)

    def get(self):
        if len(self.values) == 0:
            return None
        else:
            return self.values[0]

    def qpop(self):
        self.values.pop(0)

    def length(self):
        return len(self.values)
