from tkinter import *
import cv2
from PIL import Image
import os
import face_recognition
import xlwt
from xlwt import Workbook
from xlutils.copy import copy
from xlrd import *

wb = open_workbook('ATTENDENCE.xlsx')
sheet = wb.get_sheet

sheet.write(1,1,"hjhdf")
