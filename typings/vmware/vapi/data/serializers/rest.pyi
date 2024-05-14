"""
This type stub file was generated by pyright.
"""

"""
REST de/serializer
"""
__author__ = ...
__copyright__ = ...
logger = ...

class RequestSerializer:
    """REST request serializer"""

    @staticmethod
    def serialize_request(
        input_value, ctx, rest_metadata, is_vapi_rest
    ):  # -> tuple[Any | None, dict[Any, Any], str, None]:
        """
        Serialize the request as a REST request

        :type  input_value: :class:`vmware.vapi.data.value.StructValue`
        :param input_value: method input parameters
        :type  ctx: :class:`vmware.vapi.core.ExecutionContext`
        :param ctx: execution context object
        :type  rest_metadata:
            :class:`vmware.vapi.lib.rest.OperationRestMetadata`
        :param rest_metadata: Rest request metadata
        :type  is_vapi_rest: :class:`bool`
        :param is_vapi_rest: Whether the Rest json message format is VAPI Rest
            or not
        :rtype   :class:`tuple`
        :return: Tuple of URL path, HTTP headers, request body and cookies
        """
        ...

    @staticmethod
    def serialize_input(
        input_value, rest_metadata
    ):  # -> tuple[Any | None, dict[Any, Any], str]:
        """
        Serialize the input value

        :type  input_value: :class:`vmware.vapi.data.value.StructValue`
        :param input_value: method input parameters
        :type  rest_metadata:
            :class:`vmware.vapi.lib.rest.OperationRestMetadata`
        :param rest_metadata: Rest request metadata
        :rtype   :class:`tuple`
        :return: Tuple of URL path, HTTP headers and request body
        """
        ...

    @staticmethod
    def get_authorization_headers(
        security_context, is_vapi_rest
    ):  # -> tuple[dict[Any, Any], None] | tuple[dict[str, Any | bytes], None] | tuple[dict[str, Any], None] | tuple[dict[str, str], None]:
        """
        Get the authorization headers for the corresponding security context

        :type  security_context: :class:`vmware.vapi.core.SecurityContext`
        :param security_context: Security context
        :type  is_vapi_rest: :class:`bool`
        :param is_vapi_rest: Whether the Rest json message format is VAPI Rest
            or not
        :rtype   :class:`tuple`
        :return: Tuple of HTTP headers and cookies
        """
        ...

class ResponseDeserializer:
    """REST response deserializer"""

    @staticmethod
    def deserialize_response(status, response_str, is_vapi_rest):  # -> MethodResult:
        """
        Deserialize the REST response

        :type  status: :class:`int`
        :param status: HTTP response status code
        :type  response_str: :class:`str`
        :param response_str: HTTP response body
        :type  is_vapi_rest: :class:`bool`
        :param is_vapi_rest: Whether the Rest json message format is VAPI Rest
            or not
        :rtype   :class:`vmware.vapi.core.MethodResult`
        :return: VAPI MethodResult
        """
        ...

class RestSerializer:
    """
    Rest request de/serializer
    """

    @staticmethod
    def serialize_request(
        input_value, ctx, rest_metadata, is_vapi_rest
    ):  # -> tuple[Any | None, dict[Any, Any], str, None]:
        """
        Serialize the request as a REST request

        :type  input_value: :class:`vmware.vapi.data.value.StructValue`
        :param input_value: method input parameters
        :type  ctx: :class:`vmware.vapi.core.ExecutionContext`
        :param ctx: execution context object
        :type  rest_metadata:
            :class:`vmware.vapi.lib.rest.OperationRestMetadata`
        :param rest_metadata: Rest request metadata
        :type  is_vapi_rest: :class:`bool`
        :param is_vapi_rest: Whether the Rest json message format is VAPI Rest
            or not
        :rtype   :class:`tuple`
        :return: Tuple of URL path, HTTP headers, request body and cookies
        """
        ...

    @staticmethod
    def deserialize_response(status, response_str, is_vapi_rest):  # -> MethodResult:
        """
        Deserialize the REST response

        :type  status: :class:`int`
        :param status: HTTP response status code
        :type  response_str: :class:`str`
        :param response_str: HTTP response body
        :type  is_vapi_rest: :class:`bool`
        :param is_vapi_rest: Whether the Rest json message format is VAPI Rest
            or not
        :rtype   :class:`vmware.vapi.core.MethodResul`
        :return: VAPI MethodResult
        """
        ...
