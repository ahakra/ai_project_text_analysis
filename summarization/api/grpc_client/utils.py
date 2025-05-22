
from datetime import datetime

from api.grpc_client.service_registry import ServiceRegistryClient
from  service_constants import SERVICE_UPDATE_INFO,SERVICE_REGISTER_INFO
import grpc
from grpc import StatusCode
import time


def current_timestamp():
    return str(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

def update_metadata(service_info, new_metadata):
        updated_service_info = service_info.copy()
        updated_service_info["metadata"] = new_metadata
        return updated_service_info

def try_register_service(client, service_info, retry_delay=5):
    while True:
        try:
            print("Trying to register service...")
            client.register_service(service_info)
            print("Service registered successfully.")
            break
        except grpc.RpcError as e:
            print(f"[Register Error] gRPC failed: {e}. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)

def run_service(host:str ,port:int):
    client = ServiceRegistryClient(host=host, port=port)
    service_info = SERVICE_REGISTER_INFO
    while True:
            try:
                print("Trying to register service...")
                try_register_service(client, service_info)
                print("Service registered successfully.")
                break
            except grpc.RpcError as e:
                print(f"[Register Error] gRPC failed: {e}. Retrying in 5 seconds...")
                time.sleep(5)

            try:
                print("Service started. Press Ctrl+C to stop.")
                while True:
                    try:
                        updated_info = update_metadata(SERVICE_UPDATE_INFO, {"last_updated": current_timestamp()})
                        client.update_service(updated_info)
                        print(f"Updated service metadata at {updated_info['metadata']['last_updated']}")
                    except grpc.RpcError as e:
                        code = e.code()
                        #details = e.details()

                        if code == StatusCode.NOT_FOUND:
                            try_register_service(client, service_info)
                        else:
                            print(f"[Update Error] gRPC failed: {e}. Will retry on next loop.")

                    time.sleep(10)
            except KeyboardInterrupt:
                print("\nStopping service...")

                try:
                    client.delete_service(SERVICE_UPDATE_INFO)
                    print("Service unregistered.")
                except grpc.RpcError as e:
                    print(f"[Delete Error] Failed to delete service: {e}")
