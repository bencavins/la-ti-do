from music.note import Note
import unittest


class TestNote(unittest.TestCase):

    def test_note_init(self):
        note = Note('C')
        self.assertEqual(note.pitch, 'C')

    def test_note_init_sharp(self):
        note = Note('F#')
        self.assertEqual(note.pitch, 'F#')

    def test_note_init_flat(self):
        note = Note('Bb')
        self.assertEqual(note.pitch, 'Bb')

    def test_init_double_sharp(self):
        note = Note('B##')
        self.assertEqual(note.pitch, 'B##')

    def test_init_double_flat(self):
        note = Note('Ebb')
        self.assertEqual(note.pitch, 'Ebb')


if __name__ == '__main__':
    unittest.main()
