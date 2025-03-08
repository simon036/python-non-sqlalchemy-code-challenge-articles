class Article:
    all=[] # Store all article instances

    def __init__(self, author, magazine, title):
        # Ensuring the author and magazine are instances
        if not isinstance(author, Author):
            raise Exception("Author article must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Article magazine must be an instance of Magazine")

        self.author = author
        self.magazine = magazine
        self.title = title
        
        Article.all.append(self)

        # Establish many-to-many relationship by adding the article to the author and magazine
        self.magazine._authors.add(self.author)
        self.magazine._articles.append(self)
        
        self.author._magazines.add(self.magazine)
        self.author._articles.append(self)

    @property #getter for title
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, "_title"):
            raise Exception("Cannot change the title of the article")
        elif isinstance(title, str) and 5 < len(title) < 50:
            self._title = title
        else:
            raise Exception("Title must be a string and have characters between 5-50")

class Author:
    def __init__(self, name):
        self.name = name
        self._articles =[]
        self._magazines =set()

    
    @property #getter method for author's name
    def name (self):
        return self._name
    
    @name.setter #setter method
    def name(self,name):
        if hasattr(self, "_name"):  #ensures authors name is not changed
            raise Exception ("You cannot be able to change the name of the author after is instantiated")
        elif isinstance(name, str) and len(name) > 0: #ensures the name is a str and of more than 0 char
            self._name= name
        else:
            raise Exception ("author's name should be longer than 0 characters")



    def articles(self): #return list of articles the author has written
        return self._articles
    pass

    def magazines(self): #returns unique list of magazine contributed
        return list(self._magazines)
    pass

    def add_article(self, magazine, title): 
        if not isinstance(magazine, Magazine): # magazine is an instance
            raise Exception ("Magazine must be an instance of magazine")
        return Article(self, magazine, title)
    
    pass

    def topic_areas(self):
        if not self._articles:
            return None #returns none if author has no article
        
        return list(set(magazine.category for magazine in self._magazines))  #returns a unique list
    pass

    def _repr_(self):
        # Return a string representation of the author
        return f"Author({self.name})"
    pass


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles =[]
        self._authors=set()
        

    @property #getter method for magazine's name
    def name(self):
        return self._name
    
    @name.setter #setter method
    def name (self,name):
        if isinstance(name , str) and 2 <= len(name) <= 16:
            self._name =name
        else:
            raise Exception ("Magazine's name should be between 2-16 characters")
        
    
    @property #getter method for category
    def category(self):
        return self._category 
    
    @category.setter
    def category (self, category):
        if isinstance(category ,str) and len(category) > 0:
            self._category=category
        else:
            raise Exception ("magazine category must be a str and greater than 0")

    def articles(self): #list of all articles magazine has published
        return self._articles
    pass

    def contributors(self): #returns a unique list of authors who have written for this magazine
        return list(self._authors)
    pass

    def article_titles(self):
        if not self._articles: #return none if there are no articles
            return None
        
        return [article.title for article in self._articles] #Returns a list of the titles strings of all articles written for that magazine
    pass

    def contributing_authors(self):
        author_count={}  #creating a dictionary to store the count

        for article in self._articles:
            if article.author in author_count:
                author_count[article.author] +=1
            else:
                author_count[article.author]=1

        frequent_authors =[author for author, count in author_count.items() if count >2]
        return frequent_authors if frequent_authors else None
    pass
