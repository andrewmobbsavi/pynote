import unittest
import sys

sys.path.insert(0, '../')

import model

class Testing(unittest.TestCase):
    def test_note_add(self):
        
        """
        Test that adds a new note and checks if new note is added
        """
        resultgetStart = model.get_note_count()
        model.save_note("TEST NOTE")
        resultgetEnd = model.get_note_count()

        resultCount = resultgetEnd[0][0] - resultgetStart[0][0]

        self.assertIs(type(resultCount), int)
        self.assertEqual(resultCount, 1)


    def test_note_count(self):
        
        """
        Test that checks that the note count is an integer
        """
        resultget = model.get_note_count()
        self.assertIs(type(resultget[0][0]), int)

if __name__ == '__main__':
    unittest.main()