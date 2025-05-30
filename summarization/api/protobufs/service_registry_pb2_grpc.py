# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import service_registry_pb2 as service__registry__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in service_registry_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ServiceRegistryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetServiceInfo = channel.unary_unary(
                '/service_registry.ServiceRegistry/GetServiceInfo',
                request_serializer=service__registry__pb2.ServiceInfoRequest.SerializeToString,
                response_deserializer=service__registry__pb2.ServiceInfoResponse.FromString,
                _registered_method=True)
        self.RegisterService = channel.unary_unary(
                '/service_registry.ServiceRegistry/RegisterService',
                request_serializer=service__registry__pb2.ServiceRegisterRequest.SerializeToString,
                response_deserializer=service__registry__pb2.ServiceInfoResponse.FromString,
                _registered_method=True)
        self.UpdateService = channel.unary_unary(
                '/service_registry.ServiceRegistry/UpdateService',
                request_serializer=service__registry__pb2.ServiceUpdateRequest.SerializeToString,
                response_deserializer=service__registry__pb2.ServiceInfoResponse.FromString,
                _registered_method=True)
        self.DeleteService = channel.unary_unary(
                '/service_registry.ServiceRegistry/DeleteService',
                request_serializer=service__registry__pb2.ServiceDeleteRequest.SerializeToString,
                response_deserializer=service__registry__pb2.ServiceDeleteResponse.FromString,
                _registered_method=True)
        self.GetServicesByCategory = channel.unary_unary(
                '/service_registry.ServiceRegistry/GetServicesByCategory',
                request_serializer=service__registry__pb2.ServicesByCategoryRequest.SerializeToString,
                response_deserializer=service__registry__pb2.ServicesByCategoryResponse.FromString,
                _registered_method=True)


class ServiceRegistryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetServiceInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServicesByCategory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServiceRegistryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetServiceInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceInfo,
                    request_deserializer=service__registry__pb2.ServiceInfoRequest.FromString,
                    response_serializer=service__registry__pb2.ServiceInfoResponse.SerializeToString,
            ),
            'RegisterService': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterService,
                    request_deserializer=service__registry__pb2.ServiceRegisterRequest.FromString,
                    response_serializer=service__registry__pb2.ServiceInfoResponse.SerializeToString,
            ),
            'UpdateService': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateService,
                    request_deserializer=service__registry__pb2.ServiceUpdateRequest.FromString,
                    response_serializer=service__registry__pb2.ServiceInfoResponse.SerializeToString,
            ),
            'DeleteService': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteService,
                    request_deserializer=service__registry__pb2.ServiceDeleteRequest.FromString,
                    response_serializer=service__registry__pb2.ServiceDeleteResponse.SerializeToString,
            ),
            'GetServicesByCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServicesByCategory,
                    request_deserializer=service__registry__pb2.ServicesByCategoryRequest.FromString,
                    response_serializer=service__registry__pb2.ServicesByCategoryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'service_registry.ServiceRegistry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('service_registry.ServiceRegistry', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ServiceRegistry(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetServiceInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/service_registry.ServiceRegistry/GetServiceInfo',
            service__registry__pb2.ServiceInfoRequest.SerializeToString,
            service__registry__pb2.ServiceInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RegisterService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/service_registry.ServiceRegistry/RegisterService',
            service__registry__pb2.ServiceRegisterRequest.SerializeToString,
            service__registry__pb2.ServiceInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/service_registry.ServiceRegistry/UpdateService',
            service__registry__pb2.ServiceUpdateRequest.SerializeToString,
            service__registry__pb2.ServiceInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/service_registry.ServiceRegistry/DeleteService',
            service__registry__pb2.ServiceDeleteRequest.SerializeToString,
            service__registry__pb2.ServiceDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetServicesByCategory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/service_registry.ServiceRegistry/GetServicesByCategory',
            service__registry__pb2.ServicesByCategoryRequest.SerializeToString,
            service__registry__pb2.ServicesByCategoryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
