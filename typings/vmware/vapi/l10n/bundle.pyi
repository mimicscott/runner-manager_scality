"""
This type stub file was generated by pyright.
"""

from vmware.vapi.message import MessageBundle

"""
Helper classes for creation of resource bundles
"""
__author__ = ...
__copyright__ = ...

class PropertiesResourceBundle(MessageBundle):
    """
    Class for creating resource bundles using property files in the
    distributable. i.e. egg or zip file.
    """

    def __init__(self, property_files) -> None:
        """
        Initialize PropertiesResourceBundle

        :type  property_files: :class:`list` of :class:`tuple` or :class:`tuple`
        :param property_files: List of property files to be processed. The tuple
            should be of the form (package, resource_name). For ex: If a file
            named runtime.properties is present in vmware.vapi package, the
            tuple to be passed is ('vmware.vapi', 'runtime.properties')
        """
        ...

class FileMessageBundle(MessageBundle):
    """
    Class for creating resource bundles using list of files
    that contain messages
    """

    def __init__(self, message_files) -> None:
        """
        Initialize FileMessageBundle

        :type  message_files: :class:`list` of :class:`str` or :class:`str`
        :param message_files: List of message files to be processed. Each
            element in the list should be a fully qualified file path.
        """
        ...

class DictionaryResourceBundle(MessageBundle):
    """
    Class for creating resource bundles using dictionary of messages
    """

    def __init__(self, msgs) -> None:
        """
        Initialize DictionaryResourceBundle

        :type  msgs: :class:`dict`
        :param msgs: Message bundle
        """
        ...
