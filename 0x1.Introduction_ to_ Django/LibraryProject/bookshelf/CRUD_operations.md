In [1]: from bookshelf.models import Book

In [2]: Book.objects.all()
Out[2]: <QuerySet []>

In [3]: book = Book(title="19841984",author="George Orwell",publication_year=1949)

In [4]: book.save()

In [5]: Book.objects.all().vlaues()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[5], line 1
----> 1 Book.objects.all().vlaues()

AttributeError: 'QuerySet' object has no attribute 'vlaues'

In [6]: Book.objects.all().values()
Out[6]: <QuerySet [{'id': 1, 'title': '19841984', 'author': 'George Orwell', 'publication_year': 1949}]>

In [7]: book =Book.objects.all()[1]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[7], line 1
----> 1 book =Book.objects.all()[1]

File ~\AppData\Local\Programs\Python\Python312\Lib\site-packages\django\db\models\query.py:452, in QuerySet.__getitem__(self, k)
    450 qs.query.set_limits(k, k + 1)
    451 qs._fetch_all()
--> 452 return qs._result_cache[0]

IndexError: list index out of range

In [8]: exit
PS C:\Users\kaali\ALXBackEnd\Alx_DjangoLearnLab\0x1.Introduction_ to_ Django\libraryproject> py manage.py shell
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.26.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from bookshelf.models import Book

In [2]: Book.objects.all(
   ...: )
Out[2]: <QuerySet [<Book: Book object (1)>]>

In [3]: x = Book.objects.all()[1]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[3], line 1
----> 1 x = Book.objects.all()[1]

File ~\AppData\Local\Programs\Python\Python312\Lib\site-packages\django\db\models\query.py:452, in QuerySet.__getitem__(self, k)
    450 qs.query.set_limits(k, k + 1)
    451 qs._fetch_all()
--> 452 return qs._result_cache[0]

IndexError: list index out of range

In [4]: x = Book.objects.all()[0]

In [5]: x.title
Out[5]: '19841984'

In [6]: x.title="1984"

In [7]: x.save()

In [8]: x = Book.objects.all()[0]

In [9]: x.t
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[9], line 1
----> 1 x.t

AttributeError: 'Book' object has no attribute 't'

In [10]: x.title
Out[10]: '1984'

In [11]: x.title="Nineteen Eighty-Fou"

In [12]: x.title="Nineteen Eighty-Four"

In [13]: x.save
Out[13]: <bound method Model.save of <Book: Book object (1)>>

In [14]: x.save()

In [15]: x.delete()
Out[15]: (1, {'bookshelf.Book': 1})

In [16]: Book.objects.all().values()
Out[16]: <QuerySet []>