# Makefile (transformers server)

PROTO_DIR = ../../shared_proto
OUT_DIR = api/protobufs

# Proto files
SERVICE_REGISTRY_PROTO_FILE = $(PROTO_DIR)/service_registry.proto

# The command to compile .proto files
PROTOC = python -m grpc_tools.protoc

.PHONY:  service_registry clean


# Target to compile only service_registry.proto (client-side)
service_registry:
	$(PROTOC) -I$(PROTO_DIR) --python_out=$(OUT_DIR) --grpc_python_out=$(OUT_DIR) $(SERVICE_REGISTRY_PROTO_FILE)

# Clean up generated files for service_registry and transformers
clean:
	rm -f $(OUT_DIR)/service_registry_pb2.py $(OUT_DIR)/service_registry_pb2_grpc.py
