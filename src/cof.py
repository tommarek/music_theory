#!/usr/bin/env python3

import const

from note import Note

class CircleOfFifths():
    semitones = [(i * 7) % 12 for i in range(12)]

    def __init__(self, is_major: bool = True) -> None:
        self.notes = self.generate_cof(is_major)

    def generate_cof(self, is_major: bool) -> list:
        shift = const.NOTES.index('C' if is_major else 'A')
        return [
            Note(const.NOTES[(semitone + shift) % len(const.NOTES)])
            for semitone in self.semitones
        ]

    def get_accidentals(self, scale_root: str) -> list:
        pass
