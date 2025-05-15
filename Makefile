###########################################################
#########AI/Text Analysis/Summarization###################


PROTO_OUT_AI_TEXTANALSIS_SUMMARIZATIPN=ai_text_analysis/summarization/api/protobufs
.PHONY: ai/ta/s
ai/ta/s:
	python -m grpc_tools.protoc \
		-I$(PROTO_SRC_SERVICE_REGISTRY) \
		--python_out=$(PROTO_OUT_AI_TEXTANALSIS_SUMMARIZATIPN) \
		--grpc_python_out=$(PROTO_OUT_AI_TEXTANALSIS_SUMMARIZATIPN) \
		$(PROTO_FILE)
