from concurrent import futures
import grpc
import time

from api.protobufs import service_registry_pb2 as service__registry__pb2
from api.protobufs import service_registry_pb2_grpc as service__registry__pb2_grpc
from datetime import datetime

def format_service_response(response):
    metadata = ", ".join(f"{k}: {v}" for k, v in response.metadata.items())
    return (
        f"service_name: {response.service_name}, "
        f"category: {response.category}, "
        f"subcategory: {response.subcategory}, "
        f"type: {response.type}, "
        f"task: {response.task}, "
        f"version: {response.version}, "
        f"status: {response.status}, "
        f"metadata: {{{metadata}}}"
    )


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
            print(f"[gRPC success] - Register Service - {format_service_response(response)}")
        except grpc.RpcError as e:
            print(f"[gRPC Error] - Register Service - {e.code().name}: {e.details()}")
            raise
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
            print(f"[gRPC success] - Update Service - {format_service_response(response)}")
        except grpc.RpcError as e:
            print(f"[gRPC Error] - Update Service - {e.code().name}: {e.details()}")
            raise
    def delete_service(self, service_info):
        request = service__registry__pb2.ServiceDeleteRequest(
            service_id=service_info["service_id"],
            category=service_info["category"],
            subcategory=service_info.get("subcategory", "")
        )
        try:
            response = self.stub.DeleteService(request)
            print(f"[gRPC success] - Delete Service - {format_service_response(response)}")
        except grpc.RpcError as e:
            print(f"[gRPC Error] - Delete Service - {e.code().name}: {e.details()}")
            raise
