class NonPositiveError(Exception):
    pass 

class PositiveList(list):
    def append(self, item):
        if item < 0:
            raise NonPositiveError("This is a non positive item")
        super().append(item)