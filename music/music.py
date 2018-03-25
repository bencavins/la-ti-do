

class Note(object):
    """
    Uses Scientific Pitch Notation (https://en.wikipedia.org/wiki/Scientific_pitch_notation)
    Ex: Middle C = c4
    """
    def __init__(self, notation):
        self._pitch = notation.upper()[:2]

    @property
    def pitch(self):
        return self._pitch

    @property
    def pitch_class(self):
        return self._pitch[0]


class PitchClass(object):
    pass

class A(PitchClass):
    pass
