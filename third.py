"""
Testing challenge

Below is some code for determining the sound an animal makes and test stubs.
Complete the tests, and do not make any changes to the non-test code.
"""
import unittest

import mock


class AnimalNotFoundError(ValueError):
    """Raised if an animal is not found."""
    pass


def animal_sounds(animal):
    """Takes the name of an animal and returns the sound it makes.

    Raises AnimalNotFoundError if the animal is not known."""
    sound = ''
    if animal == 'cat':
        sound = 'meow'
    elif animal == 'dog':
        sound = 'bark'
    elif animal == 'fish':
        sound = 'blurp'
    else:
        sound = what_sound_does_a_bird_make(animal)

    if not sound:
        raise AnimalNotFoundError('{} cannot be found'.format(animal))

    return sound


def what_sound_does_a_bird_make(bird):
    """Takes the name of a bird and returns the sound it makes."""
    pass


class TestAnimalSounds(unittest.TestCase):
    """Test cases for animal_sounds."""

    def test_cat(self):
        """Should return 'meow'."""
        assert False

    def test_dog(self):
        """Should return 'bark'."""
        assert False

    def test_fish(self):
        """Should return 'blurp'."""
        assert False

    def test_no_matching_animal(self):
        """Should raise AnimalNotFoundError."""
        assert False

    def test_bird_function_called(self):
        """Should call what_sound_does_a_bird_make function once with correct params."""
        # For this test make sure the what_sound_does_a_bird_make function
        # is called once and only once, and that it received the correct parameters.
        assert False

