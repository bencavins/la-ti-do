class PitchClass(object):
    C = 0
    D = 1
    E = 2
    F = 3
    G = 4
    A = 5
    B = 6


PITCH_CLASSES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


class Note(object):
    def __init__(self, pitch):
        self._pitch_class = None
        self._mod = None

        pitch_class = pitch[0]
        if pitch_class not in PITCH_CLASSES:
            raise ValueError('{0} is not a valid pitch class: {1}'.format(pitch_class, PITCH_CLASSES))
        self._pitch_class = pitch_class

        if len(pitch) > 1:
            mod = pitch[1]
            if mod not in ['#', 'b']:
                raise ValueError('{0} is not a valid character'.format(mod))
            self._mod = mod

        if len(pitch) > 2:
            mod = pitch[2]
            if mod not in ['#', 'b']:
                raise ValueError('{0} is not a valid character'.format(mod))
            self._mod += mod

    @property
    def pitch(self):
        return '{0}{1}'.format(self._pitch_class, self._mod if self._mod else '')

    def __str__(self):
        return 'Note({0})'.format(self.pitch)

