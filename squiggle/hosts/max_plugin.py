import json
import squiggle
import MaxPlus


# ------------------------------------------------------------------------------
class MaxSquiggleDictionary(squiggle.SquiggleDictionary):

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
        root_node = MaxPlus.Core.GetRootNode()

        try:
            self.update(
                json.load(
                    root_node.GetAppData(abs(hash(self.identifier)))
                )
            )

        except BaseException:
            pass

    # --------------------------------------------------------------------------
    def save(self):
        """
        Saves the ScribbleDictionary data to a persistent state
        """
        root_node = MaxPlus.Core.GetRootNode()

        root_node.SetAppData(
            abs(hash(self.identifier)),
            json.dumps(
                self,
            )
        )
