"""Automate grading using SheetShuttle."""

from sheetshuttle import github_interaction, sheet_collector, util
import yaml

class Student:
    def __init__(self, name: str, email: str, username: str) -> None:
        """Define a student's name, email, username, and their grades."""
        # referenced from SheetShuttle's ee_grades.py sample plugin
        self.name = name
        self.email = email
        self.username = username
        # define grade values for each student
        self.grades = {
            "ee": {"num": 0, "sum": 0, "weight": 0.4},
            "projects": {"num": 0, "sum": 0, "weight": 0.15},
            "surveys": {"num": 0, "sum": 0, "weight": 0.15},
            "exams": [],
            "participation": {"grade": 0, "weight": 0.05},
        }
        
        
    # TODO: Implement functions to add grades for the following:
    # engineering efforts, projects, surveys, exams, and participation
    
    # TODO: Implement function to retrieve grades
    
    # TODO: Implement function to send grades to GitHub