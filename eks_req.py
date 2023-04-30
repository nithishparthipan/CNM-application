from kubernetes import client, config
from kubernetes.client.rest import ApiException

# load Kubernetes config
config.load_kube_config()

# create a Kubernetes API client
apps_api = client.AppsV1Api()

# define deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="my-flask-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-flask-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "my-flask-app"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-flask-app",
                        image="314937863587.dkr.ecr.us-east-1.amazonaws.com/new-cloud-native-repo:tagged-image",
                        ports=[client.V1ContainerPort(container_port=5000)],
                    )
                ]
            ),
        ),
    ),
)

# create deployment
try:
    apps_api.replace_namespaced_deployment(
        name="my-flask-app",
        namespace="default",
        body=deployment
    )
    print("Deployment updated successfully!")
except ApiException as e:
    print("Exception when updating deployment: %s\n" % e)

