#!/usr/bin/env python
"""
Generate supplemental figures 2 and 3
"""
import sys
sys.path.insert(0, '.')

from hnsccMakeFigures import supp2, supp3

print("Generating Supplemental Figures 2a-2e...")
supp2()

print("\nGenerating Supplemental Figures 3b-3f...")
supp3()

print("\nSupplemental figures generation complete!")
