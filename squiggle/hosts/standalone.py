import scribble
import squiggle


# ------------------------------------------------------------------------------
class StandaloneSquiggleDictionary(squiggle.SquiggleDictionary):

    Priority = 1

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
        data = scribble.get(self.identifier)
        self.update(data)

    # --------------------------------------------------------------------------
    def save(self):
        """
        Saves the ScribbleDictionary data to a persistent state
        """
        data = scribble.get(self.identifier)
        data.clear()
        data.update(self)
        data.save()
