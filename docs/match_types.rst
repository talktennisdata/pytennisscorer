Match Types
===========

pytennisscorer supports various tennis match formats, each with specific rules for sets, games, and tiebreaks.

Available Match Types
---------------------

Singles Grand Slam
~~~~~~~~~~~~~~~~~~

**Format:** Best of 5 sets

**Characteristics:**

* Standard scoring (15, 30, 40, game)
* Deuce and advantage rules apply
* Tiebreak at 6-6 in all sets
* Standard tiebreak (first to 7, win by 2)
* Used in: Grand Slam tournaments (men's singles)

.. code-block:: python

   from pytennisscorer import TennisScorer, MatchType

   scorer = TennisScorer(MatchType.SINGLES_GRAND_SLAM)

Singles ATP Finals
~~~~~~~~~~~~~~~~~~

**Format:** Best of 3 sets

**Characteristics:**

* Standard scoring system
* Deuce and advantage rules apply
* Tiebreak at 6-6 in all sets
* Standard tiebreak (first to 7, win by 2)
* Used in: ATP Finals, most ATP Tour events

.. code-block:: python

   scorer = TennisScorer(MatchType.SINGLES_ATP_FINALS)

Doubles Davis Cup
~~~~~~~~~~~~~~~~~

**Format:** Best of 3 sets

**Characteristics:**

* Standard scoring with no-ad rule
* Deciding point at deuce (receiver chooses service side)
* No tiebreak in any set (play until 2-game margin)
* Used in: Davis Cup doubles matches

.. code-block:: python

   scorer = TennisScorer(MatchType.DOUBLES_DAVIS_CUP)

   # At deuce, next point wins the game
   # No tiebreak - sets continue until won by 2 games

Doubles ATP Tour
~~~~~~~~~~~~~~~~

**Format:** Best of 3 sets

**Characteristics:**

* No-ad scoring (deciding point at deuce)
* Match tiebreak instead of third set
* Match tiebreak is first to 10 points, win by 2
* Standard tiebreak at 6-6 in first two sets
* Used in: ATP Tour doubles events

.. code-block:: python

   scorer = TennisScorer(MatchType.DOUBLES_ATP_TOUR)

   # Third set is replaced by match tiebreak (to 10)

Doubles Grand Slam
~~~~~~~~~~~~~~~~~~

**Format:** Best of 3 sets

**Characteristics:**

* Standard scoring with deuce/advantage
* Match tiebreak at 6-6 in the final set
* Match tiebreak is first to 10 points, win by 2
* Standard tiebreak at 6-6 in first two sets
* Used in: Grand Slam doubles events

.. code-block:: python

   scorer = TennisScorer(MatchType.DOUBLES_GRAND_SLAM)

Comparison Table
----------------

+----------------------+--------+--------+-------------+------------------+----------------+
| Match Type           | Sets   | Deuce  | Tiebreak    | Final Set        | Deciding Point |
+======================+========+========+=============+==================+================+
| Singles Grand Slam   | Bo5    | Yes    | 7 points    | Standard tiebreak| No             |
+----------------------+--------+--------+-------------+------------------+----------------+
| Singles ATP Finals   | Bo3    | Yes    | 7 points    | Standard tiebreak| No             |
+----------------------+--------+--------+-------------+------------------+----------------+
| Doubles Davis Cup    | Bo3    | No     | None        | No tiebreak      | Yes            |
+----------------------+--------+--------+-------------+------------------+----------------+
| Doubles ATP Tour     | Bo3    | No     | 7 points    | Match tiebreak   | Yes            |
+----------------------+--------+--------+-------------+------------------+----------------+
| Doubles Grand Slam   | Bo3    | Yes    | 7 points    | Match tiebreak   | No             |
+----------------------+--------+--------+-------------+------------------+----------------+

Code Examples
-------------

Checking Match Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pytennisscorer import TennisScorer, MatchType

   # Each match type has specific rules
   scorer = TennisScorer(MatchType.DOUBLES_ATP_TOUR)

   # The rules are automatically applied during scoring
   score = scorer.get_score()

   # Check if in final set (which would be match tiebreak)
   if score['current_set'] == 2:
       print("Final set will be a match tiebreak to 10")

Working with No-Ad Scoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Doubles Davis Cup uses no-ad scoring
   scorer = TennisScorer(MatchType.DOUBLES_DAVIS_CUP)

   # Score to deuce (3-3 in standard notation)
   for _ in range(3):
       scorer.increase_score(0)
       scorer.increase_score(1)

   score = scorer.get_score()
   print(f"Score: {score['game_score']}")  # Will show deuce

   # Next point wins (no advantage)
   scorer.increase_score(0)
   score = scorer.get_score()
   print(f"Game won by player 0")

Match Tiebreak Example
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Simulate reaching a match tiebreak
   scorer = TennisScorer(MatchType.DOUBLES_ATP_TOUR)

   # ... simulate play to reach third set ...
   # In third set, it's a match tiebreak to 10

   score = scorer.get_score()
   if score['in_match_tiebreak']:
       print("Now playing match tiebreak to 10 points")

Choosing the Right Match Type
------------------------------

Consider these factors when selecting a match type:

1. **Tournament Format**: Match the official tournament rules
2. **Time Constraints**: Bo3 matches are shorter than Bo5
3. **Scoring Complexity**: No-ad scoring speeds up games
4. **Tiebreak Preferences**: Some formats avoid tiebreaks entirely

Custom Configurations
---------------------

While pytennisscorer provides standard match types, the underlying architecture supports custom configurations through the internal ``ScoringRules`` class. Contact the maintainers if you need support for additional match formats.