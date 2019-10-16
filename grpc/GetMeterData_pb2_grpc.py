# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import GetMeterData_pb2 as GetMeterData__pb2


class GetMeterDataStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetData = channel.unary_unary(
        '/testgRPC.GetMeterData/GetData',
        request_serializer=GetMeterData__pb2.DataRequest.SerializeToString,
        response_deserializer=GetMeterData__pb2.MeterDataResponse.FromString,
        )


class GetMeterDataServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetData(self, request, context):
    """Get Meter Data
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GetMeterDataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetData': grpc.unary_unary_rpc_method_handler(
          servicer.GetData,
          request_deserializer=GetMeterData__pb2.DataRequest.FromString,
          response_serializer=GetMeterData__pb2.MeterDataResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'testgRPC.GetMeterData', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))