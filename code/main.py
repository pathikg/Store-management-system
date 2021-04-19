# import all the modules
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random

conn = sqlite3.connect("./Database/store.db")
c = conn.cursor()

# date
date = datetime.datetime.now().date()
