import pytest

from classes.many_to_many import Article
from classes.many_to_many import Magazine
from classes.many_to_many import Author


class TestMagazine:
    """Magazine in many_to_many.py"""

    def test_category_len(self):
        """magazine category has length greater than 0"""
        magazine_1 = Magazine("Vogue", "Fashion")  # Corrected initialization
        assert magazine_1.category != ""

        # Ensure that setting an empty category raises an exception
        with pytest.raises(Exception, match="magazine category must be a str and greater than 0"):
            magazine_1.category = ""

    def test_has_many_articles(self):
        """magazine has many articles"""
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")  # Corrected initialization
        magazine_2 = Magazine("AD", "Architecture")
        article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
        assert article_1 in magazine_1.articles()

    # Additional test methods...
