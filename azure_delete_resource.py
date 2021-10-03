# Import credential and management objects.
from logging import error
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
import os

print(f"Provisioning a virtual machine in Azure using Python.")

# Acquire credential object using CLI-based authentication.
credential = AzureCliCredential()

# Retrieve subscription ID from environment variable.
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]


# 1 - delete the resource group

# Get the management object for resources, this uses the credentials from the CLI login.
resource_client = ResourceManagementClient(credential, subscription_id)

# Set constants we need in multiple places.  You can change these values however you want.
RESOURCE_GROUP_NAME = input("Enter resource group name: ")
LOCATION = "eastus"

# create the resource group.
try:
    rg_result = resource_client.resource_groups.begin_delete(RESOURCE_GROUP_NAME)
    print("Resource group deleted")
except Exception as e:
    print(f"Exception occured with message {e}")
