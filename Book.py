# Importar los módulos necesarios para la ejecución del programa.
from Genre import GENRE
from datetime import date
class Book:
    """Constructor of the class.

        The constructor of the class Book is used to create a new book.

        Syntax
        ------
          book = Book(id, title, author, pages, publication_date, genres)

        Parameters
        ----------
          id : int
            The unique identifier of the book.
          title : str
            The title of the book.
          author : str
            The author of the book.
          pages : int
            The number of pages of the book.
          publication_date : date
            The publication date of the book.
          genres : list
            The genres of the book.

        Returns
        -------
          The new book.

        Example
        -------
          book = Book(1, "Harry Potter", "J.K. Rowling", 345, date.today(), [Genre.FANTASY])
        """
    
    # Realizar la implementación de la clase Book.
    def __init__(self, id, title, author, pages, date, genres,):
        """Constructor of the class.

        The constructor of the class Book is used to create a new book.

        Syntax
        ------
          book = Book(id, title, author, pages, publication_date, genres)

        Parameters
        ----------
          id : int
            The unique identifier of the book.
          title : str
            The title of the book.
          author : str
            The author of the book.
          pages : int
            The number of pages of the book.
          publication_date : date
            The publication date of the book.
          genres : list
            The genres of the book.


        Returns
        -------
          The new book.

        Example
        -------
          book = Book(1, "Harry Potter", "J.K. Rowling", 345, date.today(), [Genre.FANTASY])
        """
        self.id = id
        self.title = title
        self.author = author
        self.pages = pages
        self.date = date
        self.genres = genres
       


    def get_id(self):
         return self.id

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_pages(self):
        return self.pages
    
    def get_date(self):
        return self.date
    
    def get_genres(self):
        return self.genres
    
    
    def add_genre(self, genre):
        self.genres.append(genre)

    def __eq__(self, other):
      if isinstance(other, Book):
        return self.id == other.id
      return False
    
    def __str__(self):
        return f"{self.author} escribió {self.title} con {self.pages} páginas en la fecha {self.date}."


def main():
    """Function main of the module.

    The function main of this module is used to test the Class Book.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Book.")
    print("=================================================================.")
    book = Book(1, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])

    if book.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_title() == "Harry Potter":
        print("Test PASS. The parameter title has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_author() == "J.K. Rowling":
        print("Test PASS. The parameter author has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_pages() == 345:
        print("Test PASS. The parameter pages has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_date() == date.today():
        print("Test PASS. The parameter publication_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_genres() == [GENRE.FANTASY]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    book2 = Book(2, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])

    if str(book2) == "J.K. Rowling escribió Harry Potter con 345 páginas.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(book2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(book2))


    print("=================================================================.")
    print("Test Case 3: book add_genre")
    print("=================================================================.")
    book2.add_genre(GENRE.FICTION)
    genres = book2.get_genres()
    if genres == [GENRE.FANTASY, GENRE.FICTION]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))
    
    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    book3 = Book(2, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])
    if book2 == book3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")

# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
