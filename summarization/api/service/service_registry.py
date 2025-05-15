from concurrent import futures
import grpc
import time
from protobufs import service_registry_pb2
from protobufs import service_registry_pb2_grpc


class ServiceRegistryClient:
    
    def __init__(self, host="localhost", port=50051):
        # Now accepts host and port as arguments
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = service_registry_pb2_grpc.ServiceRegistryStub(self.channel)


    def register_service(self, service_info):
        request = service_registry_pb2.ServiceRegisterRequest(**service_info)
        try:
            response = self.stub.RegisterService(request)
            print(f"Service Registered: {response}")
        except grpc.RpcError as e:
            print(f"Error occurred: {e}")

    def update_service(self, service_info):
        request = service_registry_pb2.ServiceUpdateRequest(**service_info)
        try:
            response = self.stub.UpdateService(request)
            print(f"Service Updated: {response}")
        except grpc.RpcError as e:
            print(f"Error occurred: {e}")

    def delete_service(self, service_id):
        request = service_registry_pb2.ServiceDeleteRequest(service_id=service_id)
        try:
            response = self.stub.DeleteService(request)
            print(f"Service Deleted: {response}")
        except grpc.RpcError as e:
            print(f"Error occurred: {e}")    

    def update_metadata(service_info, new_metadata):
        updated_service_info = service_info.copy() 
        updated_service_info["metadata"] = new_metadata
        return updated_service_info
            