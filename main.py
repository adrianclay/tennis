import unittest


class Game:
  def __init__(self):
    self.playerOneScore = 0
  
  def tellMeTheScore(self):
    return self.scoreification(self.playerOneScore) + '-0'
  
  def scoreification(self, score):
    if score == 45:
      return "40"
    else:
      return str(score)

  def playerOneWinsPoint(self):
    self.playerOneScore += 15

class TennisTest(unittest.TestCase):
  def test_game_tellMeTheScore_returns_0_0(self):
    game = Game()
    self.assertEqual(game.tellMeTheScore(), "0-0")

  def test_playerOneWinsOnePoint_tellMeTheScore_returns_15_0(self):
    game = Game()
    game.playerOneWinsPoint()
    self.assertEqual(game.tellMeTheScore(), "15-0")

  def test_playerOneWinsTwoPoints_tellMeTheScore_returns_30_0(self):
    game = Game()
    game.playerOneWinsPoint()
    game.playerOneWinsPoint()
    self.assertEqual(game.tellMeTheScore(), "30-0")

  def test_playerOneWinsThreePoints_tellMeTheScore_returns_40_0(self):
    game = Game()
    game.playerOneWinsPoint()
    game.playerOneWinsPoint()
    game.playerOneWinsPoint()
    self.assertEqual(game.tellMeTheScore(), "40-0")

if __name__ == '__main__':
    unittest.main()
