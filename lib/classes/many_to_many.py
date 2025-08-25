# lib/classes/many_to_many.py

class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        
        pass  
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be an instance of Author class")
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError("Magazine must be an instance of Magazine class")


class Author:
    all = []
    
    def __init__(self, name):
        self._name = name
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        
        pass  
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        return list({article.magazine for article in self.articles()})
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        magazines = self.magazines()
        if not magazines:
            return None
        return list({magazine.category for magazine in magazines})


class Magazine:
    all = []
    
    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        
        if isinstance(category, str) and len(category) > 0:
            self._category = category
      
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        return list({article.author for article in self.articles()})
    
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
    
    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        
        return [author for author, count in author_count.items() if count > 2] or None