# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import abac_pb2 as abac__pb2


class ABACServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Auth = channel.unary_unary(
                '/begonia.org.sdk.ABACService/Auth',
                request_serializer=abac__pb2.AccessContext.SerializeToString,
                response_deserializer=abac__pb2.AccessResponse.FromString,
                )
        self.PolicyPut = channel.unary_unary(
                '/begonia.org.sdk.ABACService/PolicyPut',
                request_serializer=abac__pb2.PutPolicyRequest.SerializeToString,
                response_deserializer=abac__pb2.PutPolicyResponse.FromString,
                )
        self.PolicyPatch = channel.unary_unary(
                '/begonia.org.sdk.ABACService/PolicyPatch',
                request_serializer=abac__pb2.PutPolicyRequest.SerializeToString,
                response_deserializer=abac__pb2.PatchPolicyResponse.FromString,
                )
        self.PolicyDelete = channel.unary_unary(
                '/begonia.org.sdk.ABACService/PolicyDelete',
                request_serializer=abac__pb2.PolicyRequest.SerializeToString,
                response_deserializer=abac__pb2.Policy.FromString,
                )
        self.PolicyGet = channel.unary_unary(
                '/begonia.org.sdk.ABACService/PolicyGet',
                request_serializer=abac__pb2.PolicyRequest.SerializeToString,
                response_deserializer=abac__pb2.Policy.FromString,
                )
        self.PolicyList = channel.unary_unary(
                '/begonia.org.sdk.ABACService/PolicyList',
                request_serializer=abac__pb2.Policy.SerializeToString,
                response_deserializer=abac__pb2.Policy.FromString,
                )


class ABACServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Auth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PolicyPut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PolicyPatch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PolicyDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PolicyGet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PolicyList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ABACServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Auth': grpc.unary_unary_rpc_method_handler(
                    servicer.Auth,
                    request_deserializer=abac__pb2.AccessContext.FromString,
                    response_serializer=abac__pb2.AccessResponse.SerializeToString,
            ),
            'PolicyPut': grpc.unary_unary_rpc_method_handler(
                    servicer.PolicyPut,
                    request_deserializer=abac__pb2.PutPolicyRequest.FromString,
                    response_serializer=abac__pb2.PutPolicyResponse.SerializeToString,
            ),
            'PolicyPatch': grpc.unary_unary_rpc_method_handler(
                    servicer.PolicyPatch,
                    request_deserializer=abac__pb2.PutPolicyRequest.FromString,
                    response_serializer=abac__pb2.PatchPolicyResponse.SerializeToString,
            ),
            'PolicyDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.PolicyDelete,
                    request_deserializer=abac__pb2.PolicyRequest.FromString,
                    response_serializer=abac__pb2.Policy.SerializeToString,
            ),
            'PolicyGet': grpc.unary_unary_rpc_method_handler(
                    servicer.PolicyGet,
                    request_deserializer=abac__pb2.PolicyRequest.FromString,
                    response_serializer=abac__pb2.Policy.SerializeToString,
            ),
            'PolicyList': grpc.unary_unary_rpc_method_handler(
                    servicer.PolicyList,
                    request_deserializer=abac__pb2.Policy.FromString,
                    response_serializer=abac__pb2.Policy.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'begonia.org.sdk.ABACService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ABACService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Auth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/begonia.org.sdk.ABACService/Auth',
            abac__pb2.AccessContext.SerializeToString,
            abac__pb2.AccessResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PolicyPut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/begonia.org.sdk.ABACService/PolicyPut',
            abac__pb2.PutPolicyRequest.SerializeToString,
            abac__pb2.PutPolicyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PolicyPatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/begonia.org.sdk.ABACService/PolicyPatch',
            abac__pb2.PutPolicyRequest.SerializeToString,
            abac__pb2.PatchPolicyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PolicyDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/begonia.org.sdk.ABACService/PolicyDelete',
            abac__pb2.PolicyRequest.SerializeToString,
            abac__pb2.Policy.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PolicyGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/begonia.org.sdk.ABACService/PolicyGet',
            abac__pb2.PolicyRequest.SerializeToString,
            abac__pb2.Policy.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PolicyList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/begonia.org.sdk.ABACService/PolicyList',
            abac__pb2.Policy.SerializeToString,
            abac__pb2.Policy.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
