pyebook
========


About
-----
pyebook extract content and meta informations on ebook files. It relies on the
.epub standards by the idpf_

.. _idpf: http://idpf.org/epub


Installation
------------
from pip::

    pip install --upgrade pyebook

from easy_install::

    easy_install -ZU pyebook


Requirements
------------
pyebook requires beautifulsoup4_ .

.. _beautifulsoup4: http://pypi.python.org/pypi/beautifulsoup4


Usage
-----
Import::

    from pyebook.pyebook import Book

Initialize the book object::

    my_book = Book('my_ebook_file.epub')

Return the book metadata::

    my_book.metadata

Load the book content::

    my_book.load_content()

Return the book content::

    my_book.content

All the returned objects are dictionaries or dictionaries list like::

    # metadata
    {
        'date': <publication date>, 
        'identifier': <book identifier (generally the ISBN)>, 
        'creator': <book author>, 
        'language': <book language>, 
        'title': <book title>'
    }

    # content (list of dictionaries)
    [
      { 
        'part_name': <book part name>, 
        'source_url': <book part file url>, 
        'content_source': <book part html source code>, 
        'content_source_text': <book part content>
      }
    ]



Links
-----
* PyPI_
* GitHub_

.. _PyPI: http://pypi.python.org/pypi/pyebook/
.. _GitHub: https://github.com/diopib/pyebook
