API
============

.. automodule:: kardiasclean

   .. autosummary::

      split_string
      clean_accents
      clean_symbols
      clean_stopwords
      clean_tokenize
      perform_binning_quantile
      perform_binning_scalar
      perform_matrix_encoding
      perform_frequency_split_quantile
      perform_frequency_split_scalar
      get_unique_stats
      evaluate_distribution
      PostgresManager

   .. rubric:: Transformation Functions

   .. autofunction:: split_string
   .. autofunction:: spread_column
   .. autofunction:: create_unique_list

   .. rubric:: Cleaning Functions

   .. autofunction:: clean_accents
   .. autofunction:: clean_symbols
   .. autofunction:: clean_stopwords
   .. autofunction:: clean_tokenize

   .. rubric:: Normalization Functions

   .. autofunction:: normalize_from_tokens

   .. rubric:: Pre-Processing Functions

   .. autofunction:: perform_binning_quantile
   .. autofunction:: perform_binning_scalar
   .. autofunction:: perform_frequency_split_quantile
   .. autofunction:: perform_frequency_split_scalar
   .. autofunction:: perform_matrix_encoding

   .. rubric:: Utility Functions

   .. autofunction:: get_unique_stats
   .. autofunction:: evaluate_distribution
   .. autofunction:: get_difference_index

   .. rubric:: SQL PostgresManager

   .. autoclass:: PostgresManager

      .. automethod:: PostgresManager.create_table
      .. automethod:: PostgresManager.read_table
      .. automethod:: PostgresManager.read_join
      .. automethod:: PostgresManager.read_query

