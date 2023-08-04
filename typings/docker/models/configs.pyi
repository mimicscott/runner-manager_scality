"""
This type stub file was generated by pyright.
"""

from .resource import Collection, Model

class Config(Model):
    """A config."""
    id_attribute = ...
    def __repr__(self): # -> str:
        ...
    
    @property
    def name(self):
        ...
    
    def remove(self):
        """
        Remove this config.

        Raises:
            :py:class:`docker.errors.APIError`
                If config failed to remove.
        """
        ...
    


class ConfigCollection(Collection):
    """Configs on the Docker server."""
    model = Config
    def create(self, **kwargs): # -> Model:
        ...
    
    def get(self, config_id): # -> Model:
        """
        Get a config.

        Args:
            config_id (str): Config ID.

        Returns:
            (:py:class:`Config`): The config.

        Raises:
            :py:class:`docker.errors.NotFound`
                If the config does not exist.
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    
    def list(self, **kwargs): # -> list[Model | Unknown]:
        """
        List configs. Similar to the ``docker config ls`` command.

        Args:
            filters (dict): Server-side list filtering options.

        Returns:
            (list of :py:class:`Config`): The configs.

        Raises:
            :py:class:`docker.errors.APIError`
                If the server returns an error.
        """
        ...
    

