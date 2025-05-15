
from api.protobufs.service_registry import ServiceRegistryClient
from api.service.service_constants import SERVICE_REGISTER_INFO



if __name__ == "__main__":
    client = ServiceRegistryClient(host="localhost", port=50051)

    service_info = SERVICE_REGISTER_INFO
    client.register_service(service_info)

   