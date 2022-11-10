"""Automate grading using SheetShuttle."""

from sheetshuttle import github_interaction, sheet_collector, util
import yaml

class Student:
    def __init__(self, name: str, email: str, username: str) -> None:
        """Define a student's name, email, username, and their grades."""
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
        
        
    # TODO: Implement functions for the student class