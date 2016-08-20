class DiffLine(object):
    def __init__(self, first, second):
        if first == second:
            self.result = ''
        elif len(first) < len(second):
            self.result = self._parse_for_diffs(first, second)
        else:
            self.result = self._parse_for_diffs(second, first, reverse=True)

    def _parse_for_diffs(self, shorter, longer, reverse=False):
        if shorter not in longer:
            left, right = shorter, longer
        else:
            begin = longer.find(shorter)
            parts = [s for s in [longer[:begin], longer[begin+len(shorter):]] if s]
            left, right = "", (" "*len(shorter)).join(parts)
        return self._prefixes_for_lines(left, right, reverse)

    def _prefixes_for_lines(self, left, right, reverse=False):
        if reverse:
            return self._prefixes_for_lines(right, left)
        accum = ""
        if left:
            accum += "< "+left+"\n"
        if right:
            accum += "> "+right+"\n"
        return accum[:-1]

class DiffStrings(DiffLine):
    pass
