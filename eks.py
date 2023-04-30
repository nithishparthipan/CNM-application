from kubernetes import client, config

# Load the in-cluster configuration
config.load_incluster_config()

# Create an API client object for Kubernetes API
v1 = client.CoreV1Api()

# List all pods in the default namespace
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
