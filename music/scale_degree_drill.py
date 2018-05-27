import random


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


def random_scale():
    return random.choice(MAJOR_SCALES)


def random_degree():
    return random.randint(1, 7)


def main():
    total = 0
    correct = 0

    while True:
        scale = random_scale()
        degree = random_degree()

        prompt = 'What is scale degree {0} for {1}? '.format(degree, scale.tonic)
        answer = input(prompt)

        if answer == scale.degree(degree):
            correct += 1
        total += 1
        print('Answer: {0}'.format(scale.degree(degree)))

        print('{0}/{1}'.format(correct, total))


if __name__ == '__main__':
    main()
