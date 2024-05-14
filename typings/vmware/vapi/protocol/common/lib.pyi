"""
This type stub file was generated by pyright.
"""

"""
Common libraries
"""
__author__ = ...
__copyright__ = ...

class RequestProcessor:
    """
    Implementations of this interface might be attached to client
    :class:`vmware.vapi.core.ApiProvider` implementations as request
    post-processors or to the server :class:`vmware.vapi.core.ApiProvider`
    implementations as pre-processors
    """

    def process(self, message):
        """
        Processes and possibly modifies the provided request byte array

        :type  message: :class:`str`
        :param message: request message. cannot be null. If text is passed as
                        it MUST be UTF-8 encoded.
        :rtype: :class:`str`
        :return: result of the processor. cannot be null. If text is returned it
                 MUST be UTF-8 encoded.
        """
        ...
