from bson import ObjectId
from datetime import datetime

current_timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

service_id = ObjectId()

SERVICE_UPDATE_INFO = {
    "service_id": str(service_id),
    "category": "ai",
    "subcategory": "text_analysis",
    "status": "active",
    "version": "v1.0",
    "metadata": {"key": "static_value"}
}

SERVICE_REGISTER_INFO = {
    "service_id": str(service_id),
    "service_name": "text_summarization",
    "category": "ai",
    "subcategory": "text_analysis",
    "type": "summarization",
    "task": "summarize",
    "version": "v1.0",
    "status": "active",
    "metadata": {
        "last_updated": str(current_timestamp),
        "NATS":"text_summarization"
    }
}
