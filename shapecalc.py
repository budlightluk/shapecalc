#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math

class ShapeCalculator:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    @staticmethod
    def is_right_triangle(side1, side2, side3):
        sides = [side1, side2, side3]
        hypotenuse = max(sides)
        sides.remove(hypotenuse)
        return hypotenuse ** 2 == sum(side ** 2 for side in sides)

import unittest

class TestShapeCalculator(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(ShapeCalculator.circle_area(3), 28.274, places=3)

    def test_triangle_area(self):
        self.assertAlmostEqual(ShapeCalculator.triangle_area(3, 4, 5), 6)

    def test_is_right_triangle(self):
        self.assertTrue(ShapeCalculator.is_right_triangle(3, 4, 5))
        self.assertFalse(ShapeCalculator.is_right_triangle(3, 4, 6))

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)


