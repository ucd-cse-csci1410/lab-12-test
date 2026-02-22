"""
test_01_student.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the Student class.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.Student import Student 

# # Student.py
# # Author: Dr. Salim Lakhani
# # Date: November 07, 2020

# class Student:
#     """Student class which can keep track of student data (name, total credit hours,
#     and total quality points. It can also calculate gpa"""
       

#     def __init__(self, name, hours, qpoints):
#         """Initialize name, credit hours, and quality points"""
#         self.name = name
#         self.hours = float(hours)
#         self.qpoints = float(qpoints)

#     def getName(self):
#         """Return student's name"""
#         return self.name

#     def getHours(self):
#         """Return total credit hours"""
#         return self.hours

#     def getQPoints(self):
#         """Return total quality points"""
#         return self.qpoints

#     def gpa(self):
#         """Calculate and return gpa"""
#         return self.qpoints/self.hours

#     def add_grade (self, grade_point, credits):
#         """Add a new course information (Credit hours and Quality Points)"""
#         self.hours = self.hours + credits
#         self.qpoints = self.qpoints + grade_point




class TestStudent(unittest.TestCase):
    """Unit tests for Student class."""

    # case_01: getName() should return the name of the student.
    def test_01_getName(self):
        """getName() should return the name of the student."""

        received = Student("John Doe", 2, 3).getName()
        expected = "John Doe"
        self.assertEqual(
            received,
            expected, 
            msg=f"\n Wrong output.\nExpected name: '{expected}'\nReceived name: '{received}'")

    # case_02: getHours() should return the total credit hours of the student.
    def test_02_getHours(self):
        """getHours() should return the total credit hours of the student."""

        received = Student("John Doe", 2, 3).getHours()
        expected = 2
        self.assertEqual(
            received,
            expected, 
            msg=f"\n Wrong output.\nExpected hours: '{expected}'\nReceived hours: '{received}'")

    # case_03: getQPoints() should return the total quality points of the student.
    def test_03_getQPoints(self):
        """getQPoints() should return the total quality points of the student."""

        received = Student("John Doe", 2, 3).getQPoints()
        expected = 3
        self.assertEqual(
            received,
            expected, 
            msg=f"\n Wrong output.\nExpected qpoints: '{expected}'\nReceived qpoints: '{received}'")

    # case_04: gpa() should return the gpa of the student.
    def test_04_gpa(self):
        """gpa() should return the gpa of the student."""

        received = Student("John Doe", 2, 3).gpa()
        expected = 1.5
        self.assertEqual(
            received,
            expected, 
            msg=f"\n Wrong output.\nExpected gpa: '{expected}'\nReceived gpa: '{received}'")

    # case_05: add_grade() should add a new course information (Credit hours and Quality Points) to the student.
    def test_05_add_grade(self):
        """add_grade() should add a new course information (Credit hours and Quality Points) to the student."""
        student = Student("John Doe", 2, 3)
        student.add_grade(3, 4)  # grade_point=3, credits=4
        received_hours = student.getHours()
        expected_hours = 6
        self.assertEqual(
            received_hours,
            expected_hours, 
            msg=f"\n Wrong output.\nExpected hours: '{expected_hours}'\nReceived hours: '{received_hours}'")

        received_qpoints = student.getQPoints()
        expected_qpoints = 6
        self.assertEqual(
            received_qpoints,
            expected_qpoints, 
            msg=f"\n Wrong output.\nExpected qpoints: '{expected_qpoints}'\nReceived qpoints: '{received_qpoints}'")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestStudent))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)