class DiffLine(object):
    def __init__(self, first, second):
        if first == second:
            self.result = ''
        elif first in second:
            self.result = "> "+second
        elif second in first:
            self.result = "< "+first
        else:
            self.result = "\n".join(["< "+first, "> "+second])

class DiffStrings(DiffLine):
    pass
