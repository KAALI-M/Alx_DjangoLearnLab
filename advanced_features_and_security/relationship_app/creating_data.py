import os
import django



# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()
from relationshipapp.models import Author, Book, Library, Librarian

def run():
    # Clear existing data
    Librarian.objects.all().delete()
    Library.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()

    # Insert 10 authors
    authors = [
        Author(name='Jane Austen', publication_year=1813),
        Author(name='Charles Dickens', publication_year=1850),
        Author(name='Mark Twain', publication_year=1876),
        Author(name='Leo Tolstoy', publication_year=1869),
        Author(name='F. Scott Fitzgerald', publication_year=1925),
        Author(name='George Orwell', publication_year=1949),
        Author(name='J.K. Rowling', publication_year=1997),
        Author(name='Harper Lee', publication_year=1960),
        Author(name='J.R.R. Tolkien', publication_year=1954),
        Author(name='Agatha Christie', publication_year=1920),
    ]
    Author.objects.bulk_create(authors)

    # Insert 50 books
    books = [
        Book(title='Pride and Prejudice', author=authors[0]),
        Book(title='Emma', author=authors[0]),
        Book(title='Great Expectations', author=authors[1]),
        Book(title='A Tale of Two Cities', author=authors[1]),
        Book(title='The Adventures of Tom Sawyer', author=authors[2]),
        Book(title='Adventures of Huckleberry Finn', author=authors[2]),
        Book(title='War and Peace', author=authors[3]),
        Book(title='Anna Karenina', author=authors[3]),
        Book(title='The Great Gatsby', author=authors[4]),
        Book(title='Tender Is the Night', author=authors[4]),
        Book(title='1984', author=authors[5]),
        Book(title='Animal Farm', author=authors[5]),
        Book(title='Harry Potter and the Philosopher\'s Stone', author=authors[6]),
        Book(title='Harry Potter and the Chamber of Secrets', author=authors[6]),
        Book(title='To Kill a Mockingbird', author=authors[7]),
        Book(title='Go Set a Watchman', author=authors[7]),
        Book(title='The Lord of the Rings: The Fellowship of the Ring', author=authors[8]),
        Book(title='The Lord of the Rings: The Two Towers', author=authors[8]),
        Book(title='Murder on the Orient Express', author=authors[9]),
        Book(title='The Mysterious Affair at Styles', author=authors[9]),
        Book(title='Persuasion', author=authors[0]),
        Book(title='Bleak House', author=authors[1]),
        Book(title='The Prince and the Pauper', author=authors[2]),
        Book(title='Resurrection', author=authors[3]),
        Book(title='This Side of Paradise', author=authors[4]),
        Book(title='Homage to Catalonia', author=authors[5]),
        Book(title='Harry Potter and the Prisoner of Azkaban', author=authors[6]),
        Book(title='To Kill a Mockingbird', author=authors[7]),
        Book(title='The Hobbit', author=authors[8]),
        Book(title='The Murder of Roger Ackroyd', author=authors[9]),
        Book(title='Sense and Sensibility', author=authors[0]),
        Book(title='Oliver Twist', author=authors[1]),
        Book(title='The Innocents Abroad', author=authors[2]),
        Book(title='The Death of Ivan Ilyich', author=authors[3]),
        Book(title='The Beautiful and Damned', author=authors[4]),
        Book(title='Down and Out in Paris and London', author=authors[5]),
        Book(title='Harry Potter and the Goblet of Fire', author=authors[6]),
        Book(title='Harry Potter and the Order of the Phoenix', author=authors[6]),
        Book(title='Harry Potter and the Half-Blood Prince', author=authors[6]),
        Book(title='Harry Potter and the Deathly Hallows', author=authors[6]),
        Book(title='Go Set a Watchman', author=authors[7]),
        Book(title='The Silmarillion', author=authors[8]),
        Book(title='The Body in the Library', author=authors[9]),
        Book(title='And Then There Were None', author=authors[9]),
        Book(title='The A.B.C. Murders', author=authors[9]),
        Book(title='Lord Edgware Dies', author=authors[9]),
        Book(title='The Secret Adversary', author=authors[9]),
    ]
    Book.objects.bulk_create(books)

    # Insert 5 libraries
    libraries = [
        Library(name='Central City Library'),
        Library(name='Riverside Public Library'),
        Library(name='Greenwood County Library'),
        Library(name='Sunset Valley Library'),
        Library(name='Harborview Library'),
    ]
    Library.objects.bulk_create(libraries)

    # Assign books to libraries (assuming each library gets 10 books)
    for i, library in enumerate(libraries):
        library.books.set(books[i*10:(i+1)*10])

    # Insert 10 librarians, each associated with a library
    librarians = [
        Librarian(name='John Smith', library=libraries[0]),
        Librarian(name='Emily Johnson', library=libraries[1]),
        Librarian(name='Michael Brown', library=libraries[2]),
        Librarian(name='Jessica Davis', library=libraries[3]),
        Librarian(name='Daniel Martinez', library=libraries[4]),
        Librarian(name='Laura Wilson', library=libraries[0]),
        Librarian(name='David Anderson', library=libraries[1]),
        Librarian(name='Sarah Taylor', library=libraries[2]),
        Librarian(name='Christopher Thomas', library=libraries[3]),
        Librarian(name='Elizabeth Garcia', library=libraries[4]),
    ]
    Librarian.objects.bulk_create(librarians)

    print("Data created successfully!")

if __name__ == "__main__":
    run()