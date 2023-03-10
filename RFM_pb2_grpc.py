# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import RFM_pb2 as RFM__pb2


class RemoteFolderManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.actionF = channel.unary_unary(
                '/example.RemoteFolderManager/actionF',
                request_serializer=RFM__pb2.Msg.SerializeToString,
                response_deserializer=RFM__pb2.Resp.FromString,
                )


class RemoteFolderManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def actionF(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RemoteFolderManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'actionF': grpc.unary_unary_rpc_method_handler(
                    servicer.actionF,
                    request_deserializer=RFM__pb2.Msg.FromString,
                    response_serializer=RFM__pb2.Resp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'example.RemoteFolderManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RemoteFolderManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def actionF(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/example.RemoteFolderManager/actionF',
            RFM__pb2.Msg.SerializeToString,
            RFM__pb2.Resp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
