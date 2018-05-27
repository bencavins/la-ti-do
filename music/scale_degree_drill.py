import random
import time


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


class Drill(object):
    def __init__(self, **kwargs):
        self.total = 0
        self.correct = 0
        self.time_limit = kwargs.get('time_limit', 0)  # in seconds
        self.start_time = None

    def setup(self):
        """Called at the beginning of a drill run"""

        self.start_time = time.time()

    def run(self):
        self.setup()

        while self.can_run():
            try:
                correct = self.drill()
            except EOFError:  # thrown on ctrl+d
                break

            if correct:
                self.correct += 1
            self.total += 1

        self.tearDown()

    def drill(self):
        """Return True if correct, False if incorrect"""
        return False

    def tearDown(self):
        """Called at the end of a drill run"""
        print('''
Results:
{0}/{1} correct: {2}%
'''.format(self.correct, self.total, (float(self.correct) / self.total) * 100))

    def can_run(self):
        """Drill runs as long as this is true"""

        if self.time_limit:
            return self.is_out_of_time()
        else:
            return True

    def is_out_of_time(self):
        elapsed = time.time() - self.start_time
        return elapsed < self.time_limit


class ScaleDegreeDrill(Drill):

    def drill(self):
        scale = self.random_scale()
        degree = self.random_degree()

        prompt = 'What is scale degree {0} for {1}? '.format(degree, scale.tonic)
        answer = input(prompt)

        print('Answer: {0}'.format(scale.degree(degree)))

        return answer == scale.degree(degree)

    @staticmethod
    def random_scale():
        return random.choice(MAJOR_SCALES)

    @staticmethod
    def random_degree():
        return random.randint(1, 7)


def main():
    drill = ScaleDegreeDrill(time_limit=60)
    drill.run()


if __name__ == '__main__':
    main()
