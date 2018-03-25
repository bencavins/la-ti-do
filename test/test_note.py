from music.music import Note
import unittest


class TestNote(unittest.TestCase):
    def test_init_note_pitch(self):
        note = Note('C4')
        self.assertEqual(note.pitch, 'C4')
        self.assertNotEqual(note.pitch, 'C5')

    def test_init_note_pitch_lower(self):
        note = Note('c4')
        self.assertEqual(note.pitch, 'C4')
        self.assertNotEqual(note.pitch, 'c4')

    def test_init_note_pitch_class(self):
        note = Note('C4')
        self.assertEqual(note.pitch_class, 'C')
        self.assertNotEqual(note.pitch_class, 'B')

    def test_init_note_pitch_class_lower(self):
        note = Note('c4')
        self.assertEqual(note.pitch_class, 'C')
        self.assertNotEqual(note.pitch_class, 'c')


if __name__ == '__main__':
    unittest.main()
