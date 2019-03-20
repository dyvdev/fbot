#!/usr/bin/env python
# -*- coding: utf-8 -*-
path = 'mah boi.txt'
from textgenrnn import textgenrnn

textgen = textgenrnn()
textgen.reset()
textgen.train_from_file(path, num_epochs=10)