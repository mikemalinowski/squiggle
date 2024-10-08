import json
from json import JSONDecodeError

import squiggle
import pyfbsdk as mobu


# ------------------------------------------------------------------------------
class MobuSquiggleDictionary(squiggle.SquiggleDictionary):

    Priority = 2

    # --------------------------------------------------------------------------
    @classmethod
    def usable(cls):
        return True

    # --------------------------------------------------------------------------
    def load(self):
        """
        Loads the data from the disk if it exists and updates this
        dictionary.
        """
        note = self.get_note()

        if not note:
            return

        try:
            self.update(
                json.loads(
                    self.get_property(note).Data,
                ),
            )

        except (AttributeError, JSONDecodeError):
            pass

    # --------------------------------------------------------------------------
    def save(self):
        """
        Saves the ScribbleDictionary data to a persistent state
        """

        note = self.get_note()

        if not note:
            note = mobu.FBNote(self.attr_name())

        property_ = self.get_property(note)

        if not property_:
            raise Exception("Could not access the StaticComment Property")

        property_.Data = json.dumps(self)

    # ----------------------------------------------------------------------------------
    def attr_name(self):
        return f"squiggle_{self.identifier}"

    # ----------------------------------------------------------------------------------
    def get_note(self):

        note = [
            note
            for note in mobu.FBSystem().Scene.Notes
            if note.Name == self.attr_name()
        ]

        try:
            return note[0]

        except IndexError:
            return None

    # ----------------------------------------------------------------------------------
    @classmethod
    def get_property(cls, note):

        property_ = None

        for p in note.PropertyList:
            if p.Name == "StaticComment":
                return p
