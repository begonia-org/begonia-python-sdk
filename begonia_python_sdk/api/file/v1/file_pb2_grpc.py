# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import file_pb2 as file__pb2
from google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in file_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class FileServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Upload = channel.unary_unary(
                '/begonia.org.sdk.FileService/Upload',
                request_serializer=file__pb2.UploadFileRequest.SerializeToString,
                response_deserializer=file__pb2.UploadFileResponse.FromString,
                _registered_method=True)
        self.MakeBucket = channel.unary_unary(
                '/begonia.org.sdk.FileService/MakeBucket',
                request_serializer=file__pb2.MakeBucketRequest.SerializeToString,
                response_deserializer=file__pb2.MakeBucketResponse.FromString,
                _registered_method=True)
        self.UploadMultipartFile = channel.unary_unary(
                '/begonia.org.sdk.FileService/UploadMultipartFile',
                request_serializer=file__pb2.UploadMultipartFileRequest.SerializeToString,
                response_deserializer=file__pb2.UploadMultipartFileResponse.FromString,
                _registered_method=True)
        self.InitiateMultipartUpload = channel.unary_unary(
                '/begonia.org.sdk.FileService/InitiateMultipartUpload',
                request_serializer=file__pb2.InitiateMultipartUploadRequest.SerializeToString,
                response_deserializer=file__pb2.InitiateMultipartUploadResponse.FromString,
                _registered_method=True)
        self.CompleteMultipartUpload = channel.unary_unary(
                '/begonia.org.sdk.FileService/CompleteMultipartUpload',
                request_serializer=file__pb2.CompleteMultipartUploadRequest.SerializeToString,
                response_deserializer=file__pb2.CompleteMultipartUploadResponse.FromString,
                _registered_method=True)
        self.AbortMultipartUpload = channel.unary_unary(
                '/begonia.org.sdk.FileService/AbortMultipartUpload',
                request_serializer=file__pb2.AbortMultipartUploadRequest.SerializeToString,
                response_deserializer=file__pb2.AbortMultipartUploadResponse.FromString,
                _registered_method=True)
        self.Download = channel.unary_unary(
                '/begonia.org.sdk.FileService/Download',
                request_serializer=file__pb2.DownloadRequest.SerializeToString,
                response_deserializer=google_dot_api_dot_httpbody__pb2.HttpBody.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/begonia.org.sdk.FileService/Delete',
                request_serializer=file__pb2.DeleteRequest.SerializeToString,
                response_deserializer=file__pb2.DeleteResponse.FromString,
                _registered_method=True)
        self.DownloadForRange = channel.unary_unary(
                '/begonia.org.sdk.FileService/DownloadForRange',
                request_serializer=file__pb2.DownloadRequest.SerializeToString,
                response_deserializer=google_dot_api_dot_httpbody__pb2.HttpBody.FromString,
                _registered_method=True)
        self.ListFiles = channel.unary_unary(
                '/begonia.org.sdk.FileService/ListFiles',
                request_serializer=file__pb2.ListFilesRequest.SerializeToString,
                response_deserializer=file__pb2.ListFilesResponse.FromString,
                _registered_method=True)
        self.Metadata = channel.unary_unary(
                '/begonia.org.sdk.FileService/Metadata',
                request_serializer=file__pb2.FileMetadataRequest.SerializeToString,
                response_deserializer=file__pb2.FileMetadataResponse.FromString,
                _registered_method=True)


class FileServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Upload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MakeBucket(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadMultipartFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitiateMultipartUpload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteMultipartUpload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AbortMultipartUpload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Download(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadForRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Metadata(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Upload': grpc.unary_unary_rpc_method_handler(
                    servicer.Upload,
                    request_deserializer=file__pb2.UploadFileRequest.FromString,
                    response_serializer=file__pb2.UploadFileResponse.SerializeToString,
            ),
            'MakeBucket': grpc.unary_unary_rpc_method_handler(
                    servicer.MakeBucket,
                    request_deserializer=file__pb2.MakeBucketRequest.FromString,
                    response_serializer=file__pb2.MakeBucketResponse.SerializeToString,
            ),
            'UploadMultipartFile': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadMultipartFile,
                    request_deserializer=file__pb2.UploadMultipartFileRequest.FromString,
                    response_serializer=file__pb2.UploadMultipartFileResponse.SerializeToString,
            ),
            'InitiateMultipartUpload': grpc.unary_unary_rpc_method_handler(
                    servicer.InitiateMultipartUpload,
                    request_deserializer=file__pb2.InitiateMultipartUploadRequest.FromString,
                    response_serializer=file__pb2.InitiateMultipartUploadResponse.SerializeToString,
            ),
            'CompleteMultipartUpload': grpc.unary_unary_rpc_method_handler(
                    servicer.CompleteMultipartUpload,
                    request_deserializer=file__pb2.CompleteMultipartUploadRequest.FromString,
                    response_serializer=file__pb2.CompleteMultipartUploadResponse.SerializeToString,
            ),
            'AbortMultipartUpload': grpc.unary_unary_rpc_method_handler(
                    servicer.AbortMultipartUpload,
                    request_deserializer=file__pb2.AbortMultipartUploadRequest.FromString,
                    response_serializer=file__pb2.AbortMultipartUploadResponse.SerializeToString,
            ),
            'Download': grpc.unary_unary_rpc_method_handler(
                    servicer.Download,
                    request_deserializer=file__pb2.DownloadRequest.FromString,
                    response_serializer=google_dot_api_dot_httpbody__pb2.HttpBody.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=file__pb2.DeleteRequest.FromString,
                    response_serializer=file__pb2.DeleteResponse.SerializeToString,
            ),
            'DownloadForRange': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadForRange,
                    request_deserializer=file__pb2.DownloadRequest.FromString,
                    response_serializer=google_dot_api_dot_httpbody__pb2.HttpBody.SerializeToString,
            ),
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=file__pb2.ListFilesRequest.FromString,
                    response_serializer=file__pb2.ListFilesResponse.SerializeToString,
            ),
            'Metadata': grpc.unary_unary_rpc_method_handler(
                    servicer.Metadata,
                    request_deserializer=file__pb2.FileMetadataRequest.FromString,
                    response_serializer=file__pb2.FileMetadataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'begonia.org.sdk.FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('begonia.org.sdk.FileService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FileService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Upload(request,
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
            '/begonia.org.sdk.FileService/Upload',
            file__pb2.UploadFileRequest.SerializeToString,
            file__pb2.UploadFileResponse.FromString,
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
    def MakeBucket(request,
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
            '/begonia.org.sdk.FileService/MakeBucket',
            file__pb2.MakeBucketRequest.SerializeToString,
            file__pb2.MakeBucketResponse.FromString,
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
    def UploadMultipartFile(request,
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
            '/begonia.org.sdk.FileService/UploadMultipartFile',
            file__pb2.UploadMultipartFileRequest.SerializeToString,
            file__pb2.UploadMultipartFileResponse.FromString,
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
    def InitiateMultipartUpload(request,
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
            '/begonia.org.sdk.FileService/InitiateMultipartUpload',
            file__pb2.InitiateMultipartUploadRequest.SerializeToString,
            file__pb2.InitiateMultipartUploadResponse.FromString,
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
    def CompleteMultipartUpload(request,
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
            '/begonia.org.sdk.FileService/CompleteMultipartUpload',
            file__pb2.CompleteMultipartUploadRequest.SerializeToString,
            file__pb2.CompleteMultipartUploadResponse.FromString,
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
    def AbortMultipartUpload(request,
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
            '/begonia.org.sdk.FileService/AbortMultipartUpload',
            file__pb2.AbortMultipartUploadRequest.SerializeToString,
            file__pb2.AbortMultipartUploadResponse.FromString,
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
    def Download(request,
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
            '/begonia.org.sdk.FileService/Download',
            file__pb2.DownloadRequest.SerializeToString,
            google_dot_api_dot_httpbody__pb2.HttpBody.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/begonia.org.sdk.FileService/Delete',
            file__pb2.DeleteRequest.SerializeToString,
            file__pb2.DeleteResponse.FromString,
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
    def DownloadForRange(request,
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
            '/begonia.org.sdk.FileService/DownloadForRange',
            file__pb2.DownloadRequest.SerializeToString,
            google_dot_api_dot_httpbody__pb2.HttpBody.FromString,
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
    def ListFiles(request,
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
            '/begonia.org.sdk.FileService/ListFiles',
            file__pb2.ListFilesRequest.SerializeToString,
            file__pb2.ListFilesResponse.FromString,
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
    def Metadata(request,
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
            '/begonia.org.sdk.FileService/Metadata',
            file__pb2.FileMetadataRequest.SerializeToString,
            file__pb2.FileMetadataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
