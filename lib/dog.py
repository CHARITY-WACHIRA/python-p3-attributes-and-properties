#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="", breed=""):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")
            self._name = ""

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value.capitalize() in APPROVED_BREEDS:
            self._breed = value.capitalize()
        else:
            print("Breed must be in the list of approved breeds.")
            self._breed = ""

    @name.deleter
    def name(self):
        del self._name

    @breed.deleter
    def breed(self):
        del self._breed