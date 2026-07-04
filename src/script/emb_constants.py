__author__ = "fen.chan"
__version__ = "2026.03.16"

# Define all your global sets, lists, and threshold values here
"""
ETS : Embroidery Thread Stitching
ECS : Embroidery Cable Stitching
WIN : Cable Winding
""" 
THREAD_STITCH_TYPES = {"ETS", "ECS"}
CABLE_STOP_TYPES = {"ECS", "WIN"}
JUMP_THRESHOLD = 121
TIE_OFFSET = 10
MIRROR = True