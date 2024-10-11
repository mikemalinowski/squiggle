import sys
import json
import squiggle
from hashlib import md5

from pymxs import runtime as rt


# ------------------------------------------------------------------------------
class MaxSquiggleDictionary(squiggle.SquiggleDictionary):

    Priority = 2

    # --------------------------------------------------------------------------
    @classmethod
    def usable(cls):
        return True

    def get_standard_id(self):
        return int(str(int(md5(self.identifier.encode('utf-8')).hexdigest(), 16))[:6])

    # --------------------------------------------------------------------------
    def get_legacy_id(self):
        return abs(hash(self.identifier))

    # --------------------------------------------------------------------------
    def get_id(self, version=None):

        if not version:
            version_info = rt.maxVersion()
            version = version_info[0]

        if version <= 21000:  # -- Max 2019 or earlier:
            return self.get_legacy_id()

        return self.get_standard_id()


    # ------------------------------------------------------------------------------
    @classmethod
    def get_storage_node(cls):
        scene = rt.rootScene
        world = scene[rt.Name('world')]
        return world.object

    # --------------------------------------------------------------------------
    def load(self):
        """
        Loads the data from the disk if it exists and updates this
        dictionary.
        """
        storage_node = self.get_storage_node()

        try:
            data = rt.getAppData(
                storage_node, 
                self.get_id(),
            )   

            if data is not None:
                self.update(
                    json.loads(data)
                )

        except BaseException:
            pass

    # --------------------------------------------------------------------------
    def save(self):
        """
        Saves the ScribbleDictionary data to a persistent state
        """
        storage_node = self.get_storage_node()

        try:
            rt.setAppData(
                storage_node,
                self.get_id(),
                json.dumps(
                    self,
                )
            )

        except:
            print("Failed to save save data ({self.identifier}) : ")
            print(str(sys.exc_info()))
