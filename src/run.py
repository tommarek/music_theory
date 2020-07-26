#!/usr/bin/env python3

from cof import CircleOfFifths
from note import Note

circle = CircleOfFifths(is_major=False)

print(circle.semitones)
print(circle.notes)

print('-----------------')

c4 = Note('B2')

print(c4)
print(c4.frequency)
