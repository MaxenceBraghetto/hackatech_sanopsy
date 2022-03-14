#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 17:38:25 2021

@author: herisson
"""

import numpy as np
import pandas as pd
import random
import nltk
#nltk.download("movie_reviews")
nltk.download("punkt")
from nltk.corpus import movie_reviews
from nltk import word_tokenize


df = pd.read_csv("data/csv/full_dataset.csv").iloc[:,[0,-1]]


