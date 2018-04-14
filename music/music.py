class Note(object):
    def __init__(self, notation):
        self._pitch, self._pitch_class = self.parse(notation)

    @property
    def pitch(self):
        return self._pitch

    @property
    def pitch_class(self):
        return self._pitch_class

    @staticmethod
    def parse(notation):
        # TODO wrote this while smelling flowers -- make this function less stupid

        is_sharp = False
        is_flat = False

        if len(notation) >= 1:
            if notation[1] == '#':
                is_sharp = True
            elif notation[1] == 'b':
                is_flat = True

        if is_sharp or is_flat:
            pitch_class = notation[:2]
        else:
            pitch_class = notation[:1]

        pitch = notation[0].upper()
        if is_sharp or is_flat:
            pitch += notation[1]

        return pitch.upper(), pitch_class.upper()
