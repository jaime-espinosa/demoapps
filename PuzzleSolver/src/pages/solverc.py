import pathlib
import utils.display as udisp

import core.CustomSolver as CustomSolver

import streamlit as st

def write():
    udisp.title_awesome("Step by Step Walkthrough")
    CustomSolver.run_main("Title", "Subtitle")
