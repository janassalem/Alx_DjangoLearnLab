from bookshelf.models import Book

#book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

#expected output
<Book: 1984>