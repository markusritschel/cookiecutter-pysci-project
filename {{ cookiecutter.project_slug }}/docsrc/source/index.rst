.. Test documentation master file, created by
   sphinx-quickstart on Thu Oct 21 14:52:12 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================================={{ '='*cookiecutter.project_name|length }}
Welcome to the documentation of *{{ cookiecutter.project_name }}*
=================================={{ '='*cookiecutter.project_name|length }}

.. note::

    This is the main page of your project's `Sphinx`_ documentation.
    It is formatted in `reStructuredText`_. Add additional pages
    by creating rst-files in ``docs`` and adding them to the `toctree`_ below.
    Use then `references`_ in order to link them from this page, e.g.
    :ref:`authors` and :ref:`changes`.

    It is also possible to refer to the documentation of other Python packages
    with the `Python domain syntax`_. By default you can reference the
    documentation of `Sphinx`_, `Python`_, `NumPy`_, `SciPy`_, `matplotlib`_,
    `Pandas`_, `Scikit-Learn`_. You can add more by extending the
    ``intersphinx_mapping`` in your Sphinx's ``conf.py``.

    The pretty useful extension `autodoc`_ is activated by default and lets
    you include documentation from docstrings. Docstrings can be written in
    `Google style`_ (recommended!), `NumPy style`_ and `classical style`_.


A full description of the functions and the underlying algorithms can be found in the Module reference.

.. TODO: Add a more extensive description here. Maybe include photos/images of the OceanPack etc. Mention any pecularities.


Contribution
============
The entire code is publicly available on `Github <https://github.com/{{ cookiecutter.project_author }}/{{ cookiecutter.project_slug }}>`_.
If you feel like contributing, issues and pull requests are welcome :-)



.. toctree::
   :maxdepth: 1
   :caption: Content

   README <_readme>
   Changelog <_changelog>
   License <_license>
   

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: API
   
   Module Reference <api/modules>
   genindex
   py-modindex


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`py-modindex`



------------

References
==========
    .. bibliography::



.. _toctree: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _references: https://www.sphinx-doc.org/en/master/tutorial/narrative-documentation.html?highlight=references#adding-cross-references
.. _Python domain syntax: https://www.sphinx-doc.org/en/master/#the-python-domain
.. _Sphinx: https://www.sphinx-doc.org/
.. _Python: https://docs.python.org/
.. _Numpy: https://numpy.org/
.. _SciPy: https://docs.scipy.org/doc/scipy/index.html
.. _matplotlib: https://matplotlib.org/
.. _Pandas: https://pandas.pydata.org/pandas-docs/stable
.. _Scikit-Learn: https://scikit-learn.org/
.. _autodoc: https://www.sphinx-doc.org/en/stable/ext/autodoc.html
.. _Google style: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
.. _NumPy style: https://numpydoc.readthedocs.io/en/latest/format.html
.. _classical style: https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#info-field-lists
