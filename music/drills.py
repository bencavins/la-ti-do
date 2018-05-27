import random
import time

from music.scales import MAJOR_SCALES


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
