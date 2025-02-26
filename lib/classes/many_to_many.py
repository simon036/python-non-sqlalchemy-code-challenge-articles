class Article:
    all= []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise ValueError("The title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("The title must be between 5 % 50 characters")
        if hasattr(self, "_title"):
            raise ValueError("Title cannot be changed after instantiation")
        self._title = title
        

    @property #object property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be of type Author")
        self._author = author

    @property #object property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        self._magazine = magazine


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        if hasattr(self, "_name"):
            raise ValueError("Name can't be changed after author is instantiated")
        self._name = name

    def articles(self): #object relationship & property
        return [article for article in Article.all if article.author == self]
    pass

    def magazines(self):  #object relationship & property
        return list(set(article.magazine for article in self.articles()))
    pass

    def add_article(self, magazine, title): #Aggregate & Association method
        return Article(self, magazine, title)
    pass

    def topic_areas(self): #Aggregate & Association method
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))
    pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = category

    def articles(self):  #object relationship & property
        return [article for article in Article.all if article.magazine == self]
    pass

    def contributors(self):  #object relationship & property
        return list(set(article.author for article in self.articles()))
    pass

    def article_titles(self): #Aggregate & Association method
        if not self.articles():
            return None
        return [article.title for article in self.articles()]
    pass

    def contributing_authors(self): #Aggregate & Association method
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2] or None 
    pass


author1 = Author("Carry Bradshaw")
author2 = Author("Nathaniel Hawthorne")

magazine1 = Magazine("AD", "Architecture")
magazine2 = Magazine("Vogue", "Fashion")

article1 = author1.add_article(magazine1, "Python Basics")
article2 = author1.add_article(magazine2, "AI in 2023")
article3 = author2.add_article(magazine1, "Advanced Python")

print(author1.articles())
print(author1.magazines())
print(magazine1.articles())
print(magazine1.contributors())
print(author1.topic_areas())
print(magazine1.article_titles())
print(magazine1.contributing_authors())