import unittest
from jet.analyze import genderize


class GenderizeTests(unittest.TestCase):

    def test_cleaner(self):
        """
        Check the cleaner spits out a cleaned list.
        """
        test = genderize.Gender()

        self.assertEqual(test.cleaner(["This is a clean list!"]), ['this', 'is', 'a', 'clean', 'list'])

        
        print "The world is sane!"

    def test_openfile(self):
        """
        Ensure that files can be opened.
        """
        test = genderize.Gender()
        example = test.opentext('tests/test')
        self.assertEqual(example[0], "TEST This is the first line!")


    def test_filetodict(self):
        """

        Checks that lists can be turned into dictionaries without a problem.
        """
        test = genderize.Gender()

        part1 = test.listtodic(['this', 'is', 'a', 'clean', 'this', 'list'])

        self.assertEqual(part1, {'this': 2, 'a': 1, 'is': 1, 'list': 1, 'clean': 1})
        self.assertIs(type(part1), dict)


    def test_genderize(self):
        """
        Checks that gendered words are counted and turned in tuple.
        """
        test = genderize.Gender()

        part1 = test.genderize(["princess", "man", "word" ])

        self.assertEqual(part1, (1,1,1))
        self.assertIs(type(part1), tuple)