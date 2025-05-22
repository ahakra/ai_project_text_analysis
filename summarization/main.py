from api.grpc_client.utils import run_service


if __name__ == "__main__":
    run_service(host="localhost", port=50051)
