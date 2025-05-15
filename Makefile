###########################################################
#########AI/Text Analysis/Summarization###################

PROTO_FILE=service_registry.proto
PROTO_OUT_AI_TEXTANALSIS_SUMMARIZATIPN=summarization/api/protobufs
.PHONY: ta/s
ta/s:
	python -m grpc_tools.protoc \
		-I$(PROTO_OUT_AI_TEXTANALSIS_SUMMARIZATIPN) \
		--python_out=$(PROTO_OUT_AI_TEXTANALSIS_SUMMARIZATIPN) \
		--grpc_python_out=$(PROTO_OUT_AI_TEXTANALSIS_SUMMARIZATIPN) \
		$(PROTO_FILE)
