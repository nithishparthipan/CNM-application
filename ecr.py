import boto3

ecr_client = boto3.client('ecr')

repository_name = 'new-cloud-native-repo'
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)
'''try:
    response = ecr_client.create_repository(repositoryName=repository_name)
    print("Repository created successfully!")
except Exception as e:
    print("Exception when creating repository: %s\n" % e)'''
