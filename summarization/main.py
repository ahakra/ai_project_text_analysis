
from api.service.service_registry import ServiceRegistryClient
from api.service.transformers import summarize_text
from bson import ObjectId

from datetime import datetime


if __name__ == "__main__":
    client = ServiceRegistryClient(host="192.168.1.100", port=50052)

   
    service_id = ObjectId()
    current_timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    
    service_info = {
        "service_id": service_id,
        "service_name": "text_summarization",
        "subcategory": "text_analysis",
        "type": "summarization",
        "task": "summarize",
        "version": "v1.0",
        "status": "active",
        "metadata": {"last_updated": current_timestamp}
    }
    client.register_service(service_info)

   