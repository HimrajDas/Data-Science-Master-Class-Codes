import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from course import course_details

def payment():
    print("Price is : 3500")


course_details.course_name()