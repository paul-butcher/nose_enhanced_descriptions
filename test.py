import os
import unittest
import nose
from nose.plugins import PluginTester
from nose_enhanced_descriptions import EnhancedDescriptions


class TestEnhancedDescriptions(PluginTester, unittest.TestCase):
    activate = "--with-enhanced-descriptions"
    args = ["--verbose"]
    plugins = [EnhancedDescriptions()]
    suitepath = os.path.join(
        os.path.dirname(
            os.path.realpath(__file__)
        ),
        "meta_tests"
    )

    def test_no_docstring(self):
        """
        A test without a docstring is described by its fully qualified name
        """
        self.assertIn(
            "meta_tests:MetaTest.test_without_docstring ... ok",
            self.output
        )

    def test_with_docstring(self):
        """
        A test with a docstring is described by its name, followed by the first docstring line
        """
        self.assertIn(
            "meta_tests:MetaTest.test_with_docstring"
            "\n\t(I have a docstring) ... ok",
            self.output
        )

    def test_empty_first_line(self):
        """
        The line chosen for the description is the first line with content,
        not any preceding whitespace
        """
        self.assertIn(
            "(The first line was empty, but this is the line to use.) ... ok",
            self.output
        )

    def test_blank_docstring(self):
        """
        A blank docstring is treated as though absent.
        """
        self.assertNotIn("() ...", self.output)

    def test_error(self):
        """
        Tests that raise an exception work the same way
        """
        self.assertIn(
            "(I have a docstring and I raise) ... ERROR",
            self.output
        )

    def test_falure(self):
        """
        Tests that fail work the same way
        """
        self.assertIn(
            "(I have a docstring and I fail) ... FAIL",
            self.output
        )



if __name__ == '__main__':
    nose.main()