.. Kardiasclean documentation master file, created by
   sphinx-quickstart on Thu Nov 24 18:55:30 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Kardiasclean's documentation!
========================================

This package contains ETL functions for extracting all the unique natural language medical terms from a pandas DataFrame. The steps are much like any other ETL process for creating a bag of words/terms but this includes methods for normalizing the original column via "fuzzy string matching", as well as preparing new DataFrames for loading to an SQL database, and ML pre-processing like binning of low frequency records and categorical data encoding.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
