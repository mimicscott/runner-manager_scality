"""
This type stub file was generated by pyright.
"""

"""
Convenience methods for converting variable names
"""
__author__ = ...
__copyright__ = ...

class Converter:
    """
    Convenience methods for converting variable names
    """

    _mixedcase_to_underscore = ...
    _underscore_to_mixedcase = ...
    @staticmethod
    def capitalize(name):
        """
        Capitalize the first letter of the name

        :type  name: :class:`str`
        :param name: name to be converted

        :rtype: :class:`str`
        :return: name with first letter capitalized
        """
        ...

    @staticmethod
    def uncapitalize(name):
        """
        Uncapitalize the first letter of the name

        :type  name: :class:`str`
        :param name: name to be converted

        :rtype: :class:`str`
        :return: name with first letter uncapitalized
        """
        ...

    @staticmethod
    def mixedcase_to_underscore(name):  # -> str:
        """
        Convert from mixedCase to lower_case_with_underscore format

        :type  name: :class:`str`
        :param name: name in mixedCase format

        :rtype: :class:`str`
        :return: name in lower_case_with_underscore format
        """
        ...

    @staticmethod
    def underscore_to_mixedcase(name):  # -> str:
        """
        Convert from lower_case_with_underscore to mixedCase format

        :type  name: :class:`str`
        :param name: name in lower_case_with_underscore

        :rtype: :class:`str`
        :return: name in mixedCase
        """
        ...

    @staticmethod
    def capwords_to_underscore(name):  # -> str:
        """
        Convert from CapWords to lower_case_with_underscore format

        :type  name: :class:`str`
        :param name: name in CapWords format

        :rtype: :class:`str`
        :return: name in lower_case_with_underscore format
        """
        ...

    @staticmethod
    def underscore_to_capwords(name):
        """
        Convert from lower_case_with_underscore to CapWords format

        :type  name: :class:`str`
        :param name: name in lower_case_with_underscore

        :rtype: :class:`str`
        :return: name in CapWords
        """
        ...

    @staticmethod
    def unreserve_name(name):
        """
        Converts the argument if it clashes with a python keyword. If the string
        matches a keyword, adds a trailing underscore, else it returns the same
        string

        :type  name: :class:`str`
        :param name: The string to be converted

        :rtype:  :class:`str`
        :return: The converted string
        """
        ...

    @staticmethod
    def pepify(name):
        """
        Converts the argument into a name that conforms to PEP8 standard.
        i.e. lower_case_with_underscore

        :type  name: :class:`str`
        :param name: The string to be converted

        :rtype:  :class:`str`
        :return: The converted string
        """
        ...

    @staticmethod
    def canonical_to_pep(name):
        """
        Converts the argument from vAPI canonical format to PEP8 compliant
        parameter or attribute name

        :type  name: :class:`str`
        :param name: The string to be converted
        :rtype:  :class:`str`
        :return: The converted string
        """
        ...