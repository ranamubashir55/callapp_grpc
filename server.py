import json
import time
import grpc
import callapp_pb2
import callapp_pb2_grpc
from concurrent import futures
import callapp

class CallApp(callapp_pb2_grpc.CallAppServicer):
    def GetCallAppData(self , req , context):
        
        number = req.query
        print(number)
        myvar=callapp.CallApp()
        var2=myvar.test_add_contacts(number)
        print(var2)
        # r= imo.get_user(email)
        # return imo_pb2.ImoResponse(response=r )
        return callapp_pb2.CallAppResponse(response=json.dumps(var2) )
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    callapp_pb2_grpc.add_CallAppServicer_to_server(CallApp(),server)
    server.add_insecure_port('[::]:50066')
    server.start()
    print ("started CallApp")
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()

