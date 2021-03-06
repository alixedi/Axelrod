"""Tests for mind controllers and other wizards."""

import unittest
import axelrod

class TestMindController(unittest.TestCase):

    name = 'Mind Controller'

    def test_vs_cooperator(self):
        """ Will always make opponent cooperate """

        P1 = axelrod.MindController()
        P2 = axelrod.Cooperator()
        self.assertEqual(P1.strategy(P2), 'D')
        self.assertEqual(P2.strategy(P1), 'C')

    def test_vs_defect(self):
        """ Will force even defector to cooperate """

        P1 = axelrod.MindController()
        P2 = axelrod.Defector()
        self.assertEqual(P1.strategy(P2), 'D')
        self.assertEqual(P2.strategy(P1), 'C')

    def test_vs_grudger(self):
        """ Will force even Grudger to forget its grudges"""

        P1 = axelrod.MindController()
        P2 = axelrod.Grudger()
        P1.history = ['D','D','D','D',]
        self.assertEqual(P1.strategy(P2), 'D')
        self.assertEqual(P2.strategy(P1), 'C')
        
    def test_stochastic(self):
        """Test to see if the method is stochastic or not (Important for caching results)"""
        self.assertFalse(axelrod.MindController().stochastic)

    def test_init(self):
        """Test to make sure parameters are initialised correctly """

        P1 = axelrod.MindController()
        self.assertEqual(P1.history, [])

    def test_reset(self):
        """ test for the reset method """
        P1 = axelrod.MindController()
        P1.history = ['C', 'D', 'D', 'D']
        P1.reset()
        self.assertEqual(P1.history, [])

class TestMindWarper(TestMindController):

    name = "Mind Warper"

class TestMindBender(TestMindController):

    name = "Mind Bender"