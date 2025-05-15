
from api.protobufs.service_registry import ServiceRegistryClient,update_metadata
from api.service.service_constants import SERVICE_REGISTER_INFO,SERVICE_UPDATE_INFO

from datetime import datetime

current_timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    client = ServiceRegistryClient(host="localhost", port=50051)

    service_info = SERVICE_REGISTER_INFO
    client.register_service(service_info)

    # updated_info = update_metadata(SERVICE_UPDATE_INFO, {"last_updated": current_timestamp})
    # client.update_service(updated_info)
    # client.delete_service(SERVICE_UPDATE_INFO)