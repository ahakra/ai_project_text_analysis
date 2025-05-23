
from datetime import datetime

from api.grpc_client.service_registry import ServiceRegistryClient
from  .service_constants import SERVICE_UPDATE_INFO,SERVICE_REGISTER_INFO
import grpc
from grpc import StatusCode
import time


def current_timestamp():
    return str(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

def update_metadata(service_info, new_metadata):
        updated_service_info = service_info.copy()
        updated_service_info["metadata"] = new_metadata
        return updated_service_info

def try_register_service( host:str,port:int,retry_delay=5):

    while True:
        client = ServiceRegistryClient(host=host, port=port)
        service_info = SERVICE_REGISTER_INFO
        try:
            print("Trying to register service...")
            client.register_service(service_info)
            print("Service registered successfully.")
            break
        except grpc.RpcError as e:
            print(f"[Register Error] gRPC failed: {e}. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)

def run_service(host: str, port: int):
    client = ServiceRegistryClient(host=host, port=port)
    print("Starting service...")

    # Keep trying to register the service until it succeeds
    while True:
        try:
            try_register_service(host=host,port=port)
            break
        except Exception as e:
            print(f"[Initial Register Error] {e}. Retrying in 5 seconds...")
            time.sleep(5)

    print("Service registered successfully.")
    print("Service started. Press Ctrl+C to stop.")

    try:
        while True:
            updated_info = update_metadata(SERVICE_UPDATE_INFO, {"last_updated": current_timestamp()})
            try:
                client.update_service(updated_info)
            except grpc.RpcError as e:
                if e.code() == StatusCode.NOT_FOUND:
                    print("[Update Error] Service not found. Attempting to re-register...")
                    try_register_service(host, port)
                else:
                    print(f"[Update Error] gRPC failed: {e}. Will retry on next loop.")
                    try_register_service(host, port)
            except Exception as e:
                print(f"[Unexpected Error] {e}")
                try_register_service(host, port)
            print(f"Updated service metadata at {updated_info['metadata']['last_updated']}")
            time.sleep(10)

    except KeyboardInterrupt:
        print("\nStopping service...")
        try:
            client.delete_service(SERVICE_UPDATE_INFO)
            print("Service unregistered.")
        except grpc.RpcError as e:
            print(f"[Delete Error] Failed to delete service: {e}")
