
from api.protobufs.service_registry import ServiceRegistryClient
from bson import ObjectId

from datetime import datetime


if __name__ == "__main__":
    client = ServiceRegistryClient(host="localhost", port=50051)

   
    service_id = ObjectId()
    current_timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')


    service_info = {
        "service_id": str(service_id),
        "service_name": "text_summarization",
        "category": "ai",
        "subcategory": "text_analysis",
        "type": "summarization",
        "task": "summarize",
        "version": "v1.0",
        "status": "active",
        "metadata": {"last_updated": str(current_timestamp)}
    }
    client.register_service(service_info)

   