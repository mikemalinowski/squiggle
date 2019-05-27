import json
import squiggle
import maya.cmds as mc


# ------------------------------------------------------------------------------
class MayaSquiggleDictionary(squiggle.SquiggleDictionary):

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
        self.update(
            json.loads(
                mc.getAttr(self._attribute()),
            ),
        )

    # --------------------------------------------------------------------------
    def save(self):
        """
        Saves the ScribbleDictionary data to a persistent state
        """
        try:
            data = json.dumps(self)

        except BaseException:
            raise Exception(
                'Could not encode the data within the Squiggle Dictionary '
                'to JSON. Please ensure any stored data can be serialised '
                'to JSON.'
            )

        mc.setAttr(
            self._attribute(),
            data,
            type='string',
        )

    # --------------------------------------------------------------------------
    def _attribute(self):

        # -- Look for a node with the given identifier
        for attr in mc.ls('*.squiggle', recursive=True):
            if mc.getAttr(attr) == self.identifier:
                return attr.split('.')[0] + '.repository'

        # -- No node was found, so we create one and return the
        # -- path to the repository attribute
        node = mc.createNode(
            'network',
            name='squiggle',
        )

        data = dict(
            squiggle=self.identifier,
            repository='{}'
        )
        for attr_name, value in data.items():
            mc.addAttr(
                shortName=attr_name,
                dataType='string',
            )

            # -- Set the default value of the attribute
            mc.setAttr(
                node + '.' + attr_name,
                value,
                type='string',
            )

        # -- Return the path to the repository
        return node + '.repository'
