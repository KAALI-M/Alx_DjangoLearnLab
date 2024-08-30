from models import Author, Book, Library, Librarian

#creation of authors
author = Author.objects.create(name="M. Le Daillou")
author2 = Author.objects.create(name="H.j Bernard")

#cration of books
book1 = Book.objects.create(title="Tiny habbits",author=author1)
book2 = Book.objects.create(title="time management", author=author2)
book3 = Book.objects.create(title="Harry potter and the sneak", author=author1)

# creation of liuibrary
library_name = Library.objects.create(name="HD Library")

#add books 
library1.books.add(book1,book2,book3)
# add librarian and set of the library
librarian1 = Librarian.objects.create(name="Moussa Lib", library = library1)
#change of librarian's library
librarian1.library.add(library1)


# Retrieve data

all_books = Book.objects.prefetch_related(Author).all()
print(f"books :")
for bk in all_books:
    print(f"{bk.title} by {bk.author.name} ")

#books by author
books = Book.objects.filter(author=author)
print(f"books by {author1.name}")
for bk in books:
    print(f"{bk.title} by {bk.author.name} ")

# get spec libarary and it's book 
library2 = Library.objects.get(name=library_name)
library = Library.objects.prefetch_related(Book).get(name=library_name)
for bk in library.books.all() :
    print(f"{bk.title} by {bk.author.name}")

#retrieve librairian for library 
librarian  = Librarian.objects.get(library=library1)
print(f"The librarian of the library '{library1.name}' is {librarian1.name}")

