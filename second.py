""""""
import unittest


def flip_dict(source_dict):
    """
    Given a dictionary where the values are lists,
     returns a dictionary where each element in a source dictionary's
     value list is a key, and the keys from the source dictionary
     are the value.

     Example:
         given {'a': [1, 2]} should return {1: 'a', 2: 'a'}
    """
    flipped = {}

    return flipped


class TestFlipDict(unittest.TestCase):
    """Tests that flip_dict works as intended."""
    def test_flip_dict(self):
        """
        Should make values from source dict's lists into keys,
         and keys into values.
        """
        famous_animals = {
            'cat': ['garfield', 'felix', 'lil bub', 'sassy', 'puss n boots'],
            'dog': ['beethoven', 'lassie', 'chance', 'shadow', 'buddy',
                    'comet'],
            'bird': ['revali', 'zazu'],
            'fish': ['nemo', 'dory', 'flounder']
        }

        result = flip_dict(famous_animals)

        self.assertEqual(
            result,
            {
                'beethoven': 'dog',
                'buddy': 'dog',
                'chance': 'dog',
                'comet': 'dog',
                'dory': 'fish',
                'felix': 'cat',
                'flounder': 'fish',
                'garfield': 'cat',
                'lassie': 'dog',
                'lil bub': 'cat',
                'nemo': 'fish',
                'puss n boots': 'cat',
                'revali': 'bird',
                'sassy': 'cat',
                'shadow': 'dog',
                'zazu': 'bird'
            }
        )
