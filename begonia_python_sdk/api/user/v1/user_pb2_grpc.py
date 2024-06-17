# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import user_pb2 as user__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/begonia.org.sdk.UserService/Register',
                request_serializer=user__pb2.PostUserRequest.SerializeToString,
                response_deserializer=user__pb2.Users.FromString,
                )
        self.Update = channel.unary_unary(
                '/begonia.org.sdk.UserService/Update',
                request_serializer=user__pb2.PatchUserRequest.SerializeToString,
                response_deserializer=user__pb2.Users.FromString,
                )
        self.Get = channel.unary_unary(
                '/begonia.org.sdk.UserService/Get',
                request_serializer=user__pb2.GetUserRequest.SerializeToString,
                response_deserializer=user__pb2.Users.FromString,
                )
        self.Delete = channel.unary_unary(
                '/begonia.org.sdk.UserService/Delete',
                request_serializer=user__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=user__pb2.DeleteUserResponse.FromString,
                )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=user__pb2.PostUserRequest.FromString,
                    response_serializer=user__pb2.Users.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=user__pb2.PatchUserRequest.FromString,
                    response_serializer=user__pb2.Users.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=user__pb2.GetUserRequest.FromString,
                    response_serializer=user__pb2.Users.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=user__pb2.DeleteUserRequest.FromString,
                    response_serializer=user__pb2.DeleteUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'begonia.org.sdk.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/begonia.org.sdk.UserService/Register',
            user__pb2.PostUserRequest.SerializeToString,
            user__pb2.Users.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/begonia.org.sdk.UserService/Update',
            user__pb2.PatchUserRequest.SerializeToString,
            user__pb2.Users.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/begonia.org.sdk.UserService/Get',
            user__pb2.GetUserRequest.SerializeToString,
            user__pb2.Users.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/begonia.org.sdk.UserService/Delete',
            user__pb2.DeleteUserRequest.SerializeToString,
            user__pb2.DeleteUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
