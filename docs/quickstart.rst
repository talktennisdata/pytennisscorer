Quick Start Guide
=================

This guide will help you get started with pytennisscorer in just a few minutes.

Basic Usage
-----------

Creating a Scorer
~~~~~~~~~~~~~~~~~

Start by importing the necessary components and creating a scorer for your match:

.. code-block:: python

   from pytennisscorer import TennisScorer, MatchType

   # Create a scorer for different match types
   grand_slam = TennisScorer(MatchType.SINGLES_GRAND_SLAM)  # Best of 5
   atp_match = TennisScorer(MatchType.SINGLES_ATP_FINALS)   # Best of 3

Scoring Points
~~~~~~~~~~~~~~

Score points by specifying which player (0 or 1) wins the point:

.. code-block:: python

   scorer = TennisScorer(MatchType.SINGLES_GRAND_SLAM)

   # Player 0 wins a point
   scorer.increase_score(0)

   # Player 1 wins a point
   scorer.increase_score(1)

   # Continue scoring...
   scorer.increase_score(0)
   scorer.increase_score(0)

Getting the Current Score
~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve the current match state at any time:

.. code-block:: python

   score = scorer.get_score()

   print(f"Sets: {score['sets_score']}")
   print(f"Current Set: {score['current_set'] + 1}")
   print(f"Games in current set: {score['games_score']}")
   print(f"Current game: {score['game_score']}")
   print(f"Server: Player {score['server']}")
   print(f"In tiebreak: {score['in_tiebreak']}")

Complete Example
----------------

Here's a complete example simulating a short tennis game:

.. code-block:: python

   from pytennisscorer import TennisScorer, MatchType

   # Initialize scorer
   scorer = TennisScorer(MatchType.SINGLES_ATP_FINALS)

   # Simulate a game
   points = [0, 0, 1, 0, 1, 0]  # Player 0 wins 4-2

   for player in points:
       scorer.increase_score(player)
       score = scorer.get_score()
       print(f"Point to Player {player}: {score['game_score']}")

   # Check final state
   score = scorer.get_score()
   print(f"\nGame complete!")
   print(f"Games in set: {score['games_score']}")

Working with Match State
-------------------------

Checking Match Progress
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Check if the match is complete
   if scorer.is_match_complete():
       winner = scorer.get_winner()
       print(f"Match winner: Player {winner}")

   # Get detailed score information
   score = scorer.get_score()
   if score['in_tiebreak']:
       print("Currently in a tiebreak!")

Undo Functionality
~~~~~~~~~~~~~~~~~~

Made a mistake? Use the undo feature:

.. code-block:: python

   # Score a point
   scorer.increase_score(0)
   print(f"After scoring: {scorer.get_score()['game_score']}")

   # Undo the last point
   scorer.undo()
   print(f"After undo: {scorer.get_score()['game_score']}")

Server Tracking
~~~~~~~~~~~~~~~

The scorer automatically tracks and rotates servers:

.. code-block:: python

   score = scorer.get_score()
   current_server = score['server']
   print(f"Current server: Player {current_server}")

   # Server changes automatically after games
   # and follows tiebreak rules

Advanced Features
-----------------

Handling Different Tiebreak Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Different match types have different tiebreak rules:

.. code-block:: python

   # Standard tiebreak (first to 7, win by 2)
   singles_match = TennisScorer(MatchType.SINGLES_GRAND_SLAM)

   # Match tiebreak (first to 10, win by 2)
   doubles_match = TennisScorer(MatchType.DOUBLES_ATP_TOUR)

   # No tiebreak, deciding point at deuce
   davis_cup = TennisScorer(MatchType.DOUBLES_DAVIS_CUP)

Score History
~~~~~~~~~~~~~

The scorer maintains a complete history of the match:

.. code-block:: python

   # Score multiple points
   for i in range(10):
       scorer.increase_score(i % 2)

   # You can undo multiple times
   scorer.undo()  # Undo last point
   scorer.undo()  # Undo second-to-last point

Error Handling
--------------

The scorer includes built-in error handling:

.. code-block:: python

   try:
       # Invalid player number
       scorer.increase_score(2)  # Raises ValueError
   except ValueError as e:
       print(f"Error: {e}")

   try:
       # Undo when no history exists
       new_scorer = TennisScorer(MatchType.SINGLES_GRAND_SLAM)
       new_scorer.undo()  # Raises ValueError
   except ValueError as e:
       print(f"Error: {e}")

Next Steps
----------

Now that you understand the basics:

1. Learn about different :doc:`match_types`
2. Explore the complete :doc:`api_reference`
3. Check out example notebooks in the repository
4. Read about :doc:`contributing` if you want to help improve the package