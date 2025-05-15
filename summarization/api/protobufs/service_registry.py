from concurrent import futures
import grpc
import time
from . import service_registry_pb2 as service__registry__pb2
from . import service_registry_pb2_grpc as service__registry__pb2_grpc


class ServiceRegistryClient:
    
    def __init__(self, host="localhost", port=50051):
        # Now accepts host and port as arguments
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = service__registry__pb2_grpc.ServiceRegistryStub(self.channel)



    def register_service(self, service_info):
        metadata = {k: str(v) for k, v in service_info["metadata"].items()}
        request = service__registry__pb2.ServiceRegisterRequest(
            service_id=service_info["service_id"],
            service_name=service_info["service_name"],
            category=service_info["category"],
            subcategory=service_info["subcategory"],
            type=service_info["type"],
            task=service_info["task"],
            version=service_info["version"],
            status=service_info["status"],
            metadata=metadata
        )
        # Add debug prints here
        print(f"Attempting to call RegisterService on {self.stub}")
        print(f"With request: {request}")
        try:
            response = self.stub.RegisterService(request)
            print(f"Service Registered: {response}")
        except grpc.RpcError as e:
            print(f"Error occurred: {e}")

    def update_service(self, service_info):
        metadata = {k: str(v) for k, v in service_info["metadata"].items()}
        request = service__registry__pb2.ServiceUpdateRequest(
            service_id=service_info["service_id"],
            category=service_info["category"],
            subcategory=service_info["subcategory"],
            status=service_info["status"],
            version=service_info["version"],
            health_endpoint=service_info.get("health_endpoint", ""),
            metadata=metadata
        )
        try:
            response = self.stub.UpdateService(request)
            print(f"Service Updated: {response}")
        except grpc.RpcError as e:
            print(f"Error occurred: {e}")

    def delete_service(self, service_info):
        request = service__registry__pb2.ServiceDeleteRequest(
            service_id=service_info["service_id"],
            category=service_info["category"],
            subcategory=service_info.get("subcategory", "")
        )
        try:
            response = self.stub.DeleteService(request)
            print(f"Service Deleted: {response}")
        except grpc.RpcError as e:
            print(f"Error occurred: {e}")

def update_metadata(service_info, new_metadata):
        updated_service_info = service_info.copy() 
        updated_service_info["metadata"] = new_metadata
        return updated_service_info
            