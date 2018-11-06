import json
import time
import grpc
import callapp_pb2
import callapp_pb2_grpc

def run():
    channel = grpc.insecure_channel(target = "localhost:50066")
    stub=callapp_pb2_grpc.CallAppStub(channel)
    res = stub.GetCallAppData(callapp_pb2.CallAppQuery(query="03167518866"))
    print(res.response)

    
if __name__ == "__main__":
    run()