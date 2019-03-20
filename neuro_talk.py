#!/usr/bin/env python
# -*- coding: utf-8 -*-
path = 'textgenrnn_weights.hdf5'
from textgenrnn import textgenrnn

textgen = textgenrnn(path)

textgen.generate(n=20, prefix="", temperature=0.5)