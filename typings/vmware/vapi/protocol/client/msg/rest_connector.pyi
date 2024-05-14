"""
This type stub file was generated by pyright.
"""

from vmware.vapi.core import ApiProvider

"""
Rest client handler
"""
__author__ = ...
__copyright__ = ...
logger = ...
request_logger = ...

class RestClientProvider(ApiProvider):
    """Rest rpc client provider"""

    def __init__(
        self, http_provider, post_processors, rest_metadata_map=..., is_vapi_rest=...
    ) -> None:
        """
        Rest rpc client provider init

        :type  http_provider:
            :class:`vmware.vapi.protocol.client.rpc.provider.HTTPProvider`
        :param http_provider: rpc provider object
        :type  post_processors: :class:`list` of :class:`str`
        :param post_processors: List of post processor class names
        :type  rest_metadata_map: :class:`dict` of (:class:`str`, :class:`str`)
            and :class:`vmware.vapi.lib.rest.OperationRestMetadata`
        :param rest_metadata_map: Rest metadata for all operations
        :type  is_vapi_rest: :class:`bool`
        :param is_vapi_rest: Whether the Rest json message format is VAPI Rest
            or not
        """
        ...

    def add_rest_metadata(self, service_id, operation_id, rest_metadata):  # -> None:
        """
        Add rest metadata for an operation

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :type  rest_metadata:
            :class:`vmware.vapi.lib.rest.OperationRestMetadata`
        :param rest_metadata: Rest metadata for the operation
        """
        ...

    def set_rest_format(self, is_vapi_rest):  # -> None:
        """
        Set whether the rest format is VAPI or Swagger REST

        :type  is_vapi_rest: :class:`bool`
        :param is_vapi_rest: Whether the rest format is VAPI REST or not
        """
        ...

    def invoke(self, service_id, operation_id, input_value, ctx):  # -> MethodResult:
        """
        Invokes the specified method using the input value and the
        the execution context provided

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :type  input_value: :class:`vmware.vapi.data.value.DataValue`
        :param input_value: method input parameters
        :type  ctx: :class:`vmware.vapi.core.ExecutionContext`
        :param ctx: execution context object
        :rtype: :class:`vmware.vapi.core.MethodResult`
        :return: method result object
        """
        ...

def get_protocol_connector(
    http_provider, post_processors=..., provider_filter_chain=...
):  # -> GenericConnector:
    """
    Get protocol connector

    :type  http_provider:
        :class:`vmware.vapi.protocol.client.rpc.provider.HTTPProvider`
    :param http_provider: rpc provider object
    :type  post_processors: :class:`list` of :class:`str`
    :param post_processors: List of post processor class names
    :type  provider_filter_chain: :class:`list` of
        :class:`vmware.vapi.provider.filter.ApiProviderFilter`
    :param provider_filter_chain: List of API filters in order they are to be
        chained
    :rtype: :class:`vmware.vapi.protocol.client.connector.Connector`
    :return: json rpc connector object
    """
    ...
