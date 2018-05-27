class Scale(object):
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes(self):
        return self._notes

    @property
    def tonic(self):
        return self._notes[0]

    def degree(self, degree):
        return self.notes[degree - 1]  # notes are zero-indexed


MAJOR_SCALES = [
    Scale(['C',  'D',  'E',  'F',  'G',  'A',  'B' ]),
    Scale(['G',  'A',  'B',  'C',  'D',  'E',  'F#']),
    Scale(['D',  'E',  'F#', 'G',  'A',  'B',  'C#']),
    Scale(['A',  'B',  'C#', 'D',  'E',  'F#', 'G#']),
    Scale(['E',  'F#', 'G#', 'A',  'B',  'C#', 'D#']),
    Scale(['B',  'C#', 'D#', 'E',  'F#', 'G#', 'A#']),
    Scale(['F#', 'G#', 'A#', 'B',  'C#', 'D#', 'E#']),
    Scale(['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F' ]),
    Scale(['Db', 'Eb', 'F',  'Gb', 'Ab', 'Bb', 'C' ]),
    Scale(['Ab', 'Bb', 'C',  'Db', 'Eb', 'F',  'G' ]),
    Scale(['Eb', 'F',  'G',  'Ab', 'Bb', 'C',  'D' ]),
    Scale(['Bb', 'C',  'D',  'Eb', 'F',  'G',  'A' ]),
    Scale(['F',  'G',  'A',  'Bb', 'C',  'D',  'E' ]),
]
