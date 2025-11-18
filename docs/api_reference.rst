API Reference
=============

This section provides detailed documentation for all public classes and functions in pytennisscorer.

TennisScorer
------------

.. autoclass:: pytennisscorer.TennisScorer
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

   .. rubric:: Example

   .. code-block:: python

      from pytennisscorer import TennisScorer, MatchType

      # Initialize a scorer for a Grand Slam match
      scorer = TennisScorer(MatchType.SINGLES_GRAND_SLAM)

      # Score points
      scorer.increase_score(0)  # Player 0 scores
      scorer.increase_score(1)  # Player 1 scores

      # Get current state
      state = scorer.get_score()
      print(f"Game score: {state['game_score']}")

      # Undo last action
      scorer.undo()

      # Check if match is complete
      if scorer.is_match_complete():
          winner = scorer.get_winner()
          print(f"Winner: Player {winner}")

MatchType
---------

.. autoclass:: pytennisscorer.MatchType
   :members:
   :undoc-members:
   :show-inheritance:

   .. rubric:: Available Match Types

   * ``SINGLES_GRAND_SLAM`` - Best of 5 sets with standard rules
   * ``SINGLES_ATP_FINALS`` - Best of 3 sets with standard rules
   * ``DOUBLES_DAVIS_CUP`` - Best of 3 sets with no-ad scoring
   * ``DOUBLES_ATP_TOUR`` - Best of 3 sets with match tiebreak
   * ``DOUBLES_GRAND_SLAM`` - Best of 3 sets with match tiebreak at 6-6

   .. rubric:: Example

   .. code-block:: python

      from pytennisscorer import MatchType

      # Available match types
      match_types = [
          MatchType.SINGLES_GRAND_SLAM,
          MatchType.SINGLES_ATP_FINALS,
          MatchType.DOUBLES_DAVIS_CUP,
          MatchType.DOUBLES_ATP_TOUR,
          MatchType.DOUBLES_GRAND_SLAM,
      ]

      for match_type in match_types:
          print(f"Match type: {match_type.value}")

Internal Modules
----------------

The following modules are part of the internal implementation and are not part of the public API. They are documented here for completeness.

models
~~~~~~

.. automodule:: pytennisscorer.models
   :members:
   :undoc-members:
   :show-inheritance:

scoring
~~~~~~~

.. automodule:: pytennisscorer.scoring
   :members:
   :undoc-members:
   :show-inheritance:

progression
~~~~~~~~~~~

.. automodule:: pytennisscorer.progression
   :members:
   :undoc-members:
   :show-inheritance:

formatter
~~~~~~~~~

.. automodule:: pytennisscorer.formatter
   :members:
   :undoc-members:
   :show-inheritance:

configs
~~~~~~~

.. automodule:: pytennisscorer.configs
   :members:
   :undoc-members:
   :show-inheritance:

Type Definitions
----------------

Score Dictionary
~~~~~~~~~~~~~~~~

The ``get_score()`` method returns a dictionary with the following structure:

.. code-block:: python

   {
       'sets_score': str,           # e.g., "1-0"
       'current_set': int,          # 0-indexed current set number
       'games_score': str,          # e.g., "3-2"
       'game_score': str,           # e.g., "30-15" or "40-A"
       'server': int,               # 0 or 1
       'in_tiebreak': bool,         # True if in tiebreak
       'in_match_tiebreak': bool,   # True if in match tiebreak
   }

Exceptions
----------

pytennisscorer raises the following exceptions:

.. py:exception:: ValueError

   Raised when:

   * Invalid player number (not 0 or 1) is passed to ``increase_score()``
   * ``undo()`` is called when there's no history to undo
   * ``get_winner()`` is called when the match is not complete

.. py:exception:: TypeError

   Raised when:

   * Invalid ``MatchType`` is passed to ``TennisScorer`` constructor
   * Wrong argument types are passed to any method