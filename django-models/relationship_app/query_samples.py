from LibraryProject.relationship_app.models import Author,Book, Library, Librarian
#creation of authors
author1 = Author.objects.create(name="M. Le Daillou")
author2 = Author.objects.create(name="H.j Bernard")

#cration of books
book1 = Book.objects.create(title="Tiny habbits",author=author1)
book2 = Book.objects.create(title="time management", author=author2)
book3 = Book.objects.create(title="Harry potter and the sneak", author=author1)

# creation of liuibrary
library1 = Library.objects.create(name="HD Library")

#add books 
library1.books.add(book1,book2,book3)

# Retrieve data
all_books = Book.objects.prefetch_related(Author).all()

print("books :")
for book in all_books:
    print(f"{book.title} by {book.author.name} ")

