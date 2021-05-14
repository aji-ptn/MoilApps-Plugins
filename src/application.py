import inspect
import os
import pkgutil
from plugin import Plugin


class Application(object):
    def __init__(self, plugin_package):
        """
        Upon creation, this class will read the plugins package for modules that contains
        a class definition that is inheriting from the Plugin class.

        Args:
            plugin_package (): The folder name of plugins directory. i.e here is "plugins"
        """
        self.plugins = None
        self.name_application = None
        self.seen_paths = None
        self.path_folder = None
        self.plugin_package = plugin_package
        self.reload_plugins()

    def reload_plugins(self):
        """
        Reset the list of all plugins and initiate the walk over the main provided
        plugin package to load all available plugins.

        Returns:

        """
        self.plugins = []
        self.name_application = []
        self.seen_paths = []
        self.path_folder = []
        self.walk_package(self.plugin_package)

    def application(self, argument, index):
        """
        Apply all of the plugin on the argument supplied to this function.

        Args:
            argument ():
            index ():

        Returns:

        """
        plugin = self.plugins[index]
        plugin.perform_operation(argument)

    def walk_package(self, package):
        """
        Recursively walk the supplied package to retrieve all plugins.

        Args:
            package ():

        Returns:

        """
        imported_package = __import__(package, fromlist=['blah'])

        for _, pluginname, ispkg in pkgutil.iter_modules(
                imported_package.__path__, imported_package.__name__ + '.'):
            if not ispkg:
                plugin_module = __import__(pluginname, fromlist=['blah'])
                clsmembers = inspect.getmembers(plugin_module, inspect.isclass)
                for (_, c) in clsmembers:
                    # only add classes that are a sub class of plugin, but not
                    # plugin it self
                    if issubclass(c, Plugin) & (c is not Plugin):
                        # print(f'Found Plugin class: {c.__module__}')
                        self.path_folder.append(c.__module__)
                        self.name_application.append(c.__name__)
                        self.plugins.append(c())

        # Now that we have looked at all the modules in the current package, start looking
        # recursively for additional modules in sub packages
        all_curent_paths = []
        if isinstance(imported_package.__path__, str):
            all_curent_paths.append(imported_package.__path__)
        else:
            all_curent_paths.extend([x for x in imported_package.__path__])

        for pkg_path in all_curent_paths:
            if pkg_path not in self.seen_paths:
                self.seen_paths.append(pkg_path)

                # get sub directory of curent package path directory
                child_pkgs = [
                    p for p in os.listdir(pkg_path) if os.path.isdir(
                        os.path.join(
                            pkg_path, p))]
                # For each sub directory, apply the walk_package method
                # recursively
                for child_pkg in child_pkgs:
                    self.walk_package(package + '.' + child_pkg)
