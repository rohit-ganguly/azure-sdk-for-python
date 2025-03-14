# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.newrelicobservability import NewRelicObservabilityMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-newrelicobservability
# USAGE
    python tag_rules_list_by_new_relic_monitor_resource_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NewRelicObservabilityMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="ddqonpqwjr",
    )

    response = client.tag_rules.list_by_new_relic_monitor_resource(
        resource_group_name="rgopenapi",
        monitor_name="ipxmlcbonyxtolzejcjshkmlron",
    )
    for item in response:
        print(item)


# x-ms-original-file: specification/newrelic/resource-manager/NewRelic.Observability/preview/2022-07-01-preview/examples/TagRules_ListByNewRelicMonitorResource_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
