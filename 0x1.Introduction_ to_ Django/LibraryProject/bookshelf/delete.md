### delete.md

```md
# Delete the created Book instance
## Command:
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(books)