

class Plugin(object):
    """this is the base class that each plugin must inheritance from.Within this class
    you have to define the methods that all of your plugins must implement
    """

    def __init__(self):
        self.description = "UNKNOWN"

    def perform_operation(self, argument):
        """The method that we expect all plugins to implement. this is the framework our
        method will call
        """
        raise NotImplementedError
