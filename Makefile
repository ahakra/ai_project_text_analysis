###########################################################
# Protobuf Build Configurations
###########################################################

SUMMARIZATION_PROTO = summarization/api/protobufs/service_registry.proto
SUMMARIZATION_PROTO_OUT = summarization/api/protobufs


.PHONY: proto-sum run-sum clean-sum rebuild-sum \
        proto-all run-all clean-all rebuild-all

###########################################################
# Summarization Service Commands
###########################################################

proto-sum:
	python -m grpc_tools.protoc \
		-I$(SUMMARIZATION_PROTO_OUT) \
		--python_out=$(SUMMARIZATION_PROTO_OUT) \
		--grpc_python_out=$(SUMMARIZATION_PROTO_OUT) \
		$(SUMMARIZATION_PROTO)

run-sum:
	poetry run python summarization/main.py

clean-sum:
	find $(SUMMARIZATION_PROTO_OUT) -type f \( -name "*_pb2.py" -o -name "*_pb2_grpc.py" \) -delete

rebuild-sum: clean-sum proto-sum run-sum

###########################################################
# All Services (if you expand)
###########################################################

proto-all: proto-sum
run-all: run-sum
clean-all: clean-sum
rebuild-all: rebuild-sum


