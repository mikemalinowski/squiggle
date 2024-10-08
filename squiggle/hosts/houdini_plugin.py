import hou
import sys
import json
import squiggle


# ------------------------------------------------------------------------------
class HoudiniSquiggleDictionary(squiggle.SquiggleDictionary):

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
        try:
            self.update(
                json.loads(hou.node('/').userData(self.identifier))
            )

        except BaseException:
            pass

    # --------------------------------------------------------------------------
    def save(self):
        """
        Saves the ScribbleDictionary data to a persistent state
        """
        try:
            hou.node('/').setUserData(
                self.identifier,
                json.dumps(self),
            )

        except:
            print(
                    'Could not save data (%s) : %s' % (
                self.identifier,
                str(sys.exc_info())),
            )
