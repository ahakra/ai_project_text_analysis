from bson import ObjectId

service_id = ObjectId()

SERVICE_UPDATE_INFO = {
    "service_id": service_id,
    "category": "ai",
    "subcategory": "text_analysis",
    "status": "active",
    "version": "v1.0",
    "metadata": {"key": "static_value"}  
}
