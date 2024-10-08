import os
from .vendor import factories

_factory = None


# ------------------------------------------------------------------------------
def get(identifier, *args, **kwargs):
    """
    This will return a SquiggleDictionary capable of serialising itself
    within the host application.

    :param identifier: Unique identifier to access a specific scribble
        dictionary.
    :type identifier: str

    :return: ScribbleDictionary
    """
    global _factory

    if not _factory:
        _factory = factories.Factory(
            abstract=SquiggleDictionary,
            plugin_identifier='__name__',
            paths=[
                os.path.join(
                    os.path.dirname(__file__),
                    'hosts',
                ),
            ],
            log_errors=False,
        )

    for plugin in sorted(_factory.plugins(), key=lambda p: p.Priority, reverse=True):
        if plugin.usable():
            return plugin(identifier, *args, **kwargs)

    raise Exception(
        'No plugin could be found for the given host'
    )


# ------------------------------------------------------------------------------
class SquiggleDictionary(dict):

    Priority = 1

    # --------------------------------------------------------------------------
    def __init__(self, identifier, *args, **kwargs):
        super(SquiggleDictionary, self).__init__(*args, **kwargs)

        # -- Store the identifier, as this is used whenever the
        # -- scribble dictionary is stored.
        self.identifier = identifier

        # -- Initiate a load of any persistent data for the given
        # -- identifier
        self.load()

    # --------------------------------------------------------------------------
    @classmethod
    def usable(cls):
        """
        This should only return True if the plugin is able to operate
        within the current environment.
        
        :return: bool
        """
        return False

    # --------------------------------------------------------------------------
    def load(self):
        """
        Loads the data from the disk if it exists and updates this
        dictionary.
        """
        pass

    # --------------------------------------------------------------------------
    def save(self):
        """
        Saves the ScribbleDictionary data to a persistent state
        """
        pass
