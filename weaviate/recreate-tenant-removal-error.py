# To reproduce the bug edit
# tenant_to_update = 'steve85' and tenant_to_remove = 'steve85' so that user
# steve85 is in DEACTIVATED state when you try to remove the tenant.
# If steve85 is reset to ACTIVE, the tenant can be removed.

import weaviate, os
from datetime import datetime, timezone
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.tenants import Tenant, TenantActivityStatus
from weaviate.classes.query import Filter

collection_name = "MultiTenantDemo"

###############################
# Connect to a local instance #
###############################
client = weaviate.connect_to_local(
    headers={
        "X-Cohere-Api-Key": os.environ["COHERE_API_KEY"],
    }
)

#########################
# Create the collection #
#########################
# Uncomment to delete data from prior runs
if (client.collections.exists(collection_name)):
    client.collections.delete(collection_name)

multi_tenant_collection = client.collections.create(
    name=collection_name,
    multi_tenancy_config=Configure.multi_tenancy(
        enabled=True,
        auto_tenant_creation=True,
        auto_tenant_activation=True,
    ),
    properties=[
        Property(name="text", data_type=DataType.TEXT),
        Property(name="date", data_type=DataType.DATE),
        Property(name="tags", data_type=DataType.TEXT_ARRAY),
    ],
    vectorizer_config=[
        Configure.NamedVectors.text2vec_cohere(
            name="text",
            source_properties=["text"],
            vector_index_config=Configure.VectorIndex.dynamic(
                hnsw=Configure.VectorIndex.hnsw(
                    quantizer=Configure.VectorIndex.Quantizer.sq(training_limit=50000)
                ),
                flat=Configure.VectorIndex.flat(
                    quantizer=Configure.VectorIndex.Quantizer.bq()
                ),
                threshold=10000
            )
        )
    ],
    generative_config=Configure.Generative.cohere(model="command-r-plus")
)

#########################
# Get collection object #
#########################
multi_tenant_collection = client.collections.get(collection_name)

###################
# Create a Tenant #
###################
multi_tenant_collection.tenants.create(
    tenants=[
        Tenant(name="steve85"),
        Tenant(name="bobby84"),
    ]
)

##########################
# Add data to one tenant #
##########################
# Get collection object then specify the tenant
multi_tenant_collection = client.collections.get(collection_name)
tenant = multi_tenant_collection.with_tenant("steve85")

return_value = tenant.data.insert(
    properties={
        "text": "What amazing food we had at Quay! It was totally worth it.",
        "date": datetime(2024, 5, 15).replace(tzinfo=timezone.utc),
        "tags": ["restaurant", "experience"],
    }
)

########################
# Auto create a tenant #
########################
# Specify a tenant that doesn't exist yet
new_tenant = multi_tenant_collection.with_tenant("yana42")
new_tenant.data.insert({
    "date": datetime(2024, 7, 7).replace(tzinfo=timezone.utc),
    "tags": ["events", "grand prix"],
    "text": "La nacional rocks",
})


#######################
# Deactivate a tenant #
#######################
# Select a tenant to update
# tenant_to_update = 'yana42'   # auto created
tenant_to_update = 'steve85'  # Explicitly created

# Check the initial status
tenants = multi_tenant_collection.tenants.get()
print(f"DEACTIVATE BEFORE: name: {tenants[tenant_to_update].name} status: {tenants[tenant_to_update].activityStatus}")

multi_tenant_collection.tenants.update(
    Tenant(name=tenant_to_update, activity_status=TenantActivityStatus.INACTIVE)
)

# Check the updated status
tenants = multi_tenant_collection.tenants.get()
print(f"DEACTIVATE AFTER: name: {tenants[tenant_to_update].name} status: {tenants[tenant_to_update].activityStatus}")

#######################
# Reactivate a tenant #
#######################
# Uncomment to reset the status to ACTIVE
multi_tenant_collection.tenants.update(
    Tenant(name=tenant_to_update, activity_status=TenantActivityStatus.ACTIVE)
)
print(f"REACTIVATED: name: {tenants[tenant_to_update].name} status: {tenants[tenant_to_update].activityStatus}")

#######################
# Remove a tenant #
#######################
# Select a tenant to remove
# tenant_to_remove = 'yana42'  # auto created
tenant_to_remove = 'steve85'  # explicitly created

# Check the initial status
tenants = multi_tenant_collection.tenants.get()
print(f"REMOVE BEFORE: name: {tenants[tenant_to_remove].name} status: {tenants[tenant_to_remove].activityStatus}")

# Remove the tenant
multi_tenant_collection.tenants.remove(tenant_to_remove)

# Progress check
print("REMOVE DONE")

# Check all tenants
tenants = multi_tenant_collection.tenants.get()
for t in tenants:
    print(f"REMOVE T CHECK: name: {tenants[t].name} status: {tenants[t].activityStatus}")

########################
# Close the connection #
########################
client.close()