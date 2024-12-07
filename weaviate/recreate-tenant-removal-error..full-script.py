# This script was written to check various mutli-tenant operations
#  during the documentation write up.
#
# Discovered a bug while working on the delete fucntionality. The
#  companion script, recreat-tenat-removal-error.py is a shorter
#  version to help developers reproduce the issue.


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

# Check the client connection
print(f"CHECK CLIENT: {client.is_ready()}")


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

######################################
# Confirm that the collection exists #
######################################
response = client.collections.list_all()
for r in response:
    print(f"CONFIRM COLLECTION CREATION: {r}")


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

# List the tenants
tenants = multi_tenant_collection.tenants.get()
print(f"TENANTS: {tenants}")

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

print(f"SINGLE DATA ADD: {return_value}")

##################
# Batch add data #
##################
# Some sample data
journal_entries = [
     {"text": "Loved it", "date": datetime(2024, 3, 4).replace(tzinfo=timezone.utc), "tags": ["restaurant", "experience"]},
     {"text": "Hated it", "date": datetime(2024, 4, 5).replace(tzinfo=timezone.utc), "tags": ["cafe"]},
     {"text": "Meh", "date": datetime(2024, 5, 6).replace(tzinfo=timezone.utc), "tags": ["dinner", "group"]}
    ]

return_values =[]
with tenant.batch.fixed_size(100) as batch:
    for journal_entry in journal_entries:
        return_values.append(batch.add_object(journal_entry))

print(f"BATCH DATA ADD: {return_values}")

###############################
# Check the number of objects #
###############################
response = tenant.aggregate.over_all(total_count=True)
print(f"NUM OBJECTS: {response.total_count}")

########################
# Auto create a tenant #
########################
# Specify a tenant that doesn't exist yet
new_tenant = multi_tenant_collection.with_tenant("yana42")

# Uncomment to list the number of tenants before inserting
tenants = multi_tenant_collection.tenants.get()
print(f"BEFORE: {len(tenants)}")

new_tenant.data.insert({
    "date": datetime(2024, 7, 7).replace(tzinfo=timezone.utc),
    "tags": ["events", "grand prix"],
    "text": "La nacional rocks",
})

# Uncomment to list the number of tenants after inserting
tenants = multi_tenant_collection.tenants.get()
print(f"AFTER: {len(tenants)}")

# Uncomment to list the tenants
tenants = multi_tenant_collection.tenants.get()
print(f"TENANTS: {tenants}")

###############
# Run a query #
###############
# Get the tenant
tenant = multi_tenant_collection.with_tenant("steve85")

start_date = datetime(2024, 1, 1).replace(tzinfo=timezone.utc)
end_date = datetime(2024, 4, 15).replace(tzinfo=timezone.utc)

# Find the entries between two dates
response = tenant.query.fetch_objects(
    filters=(
        Filter.by_property("date").greater_or_equal(start_date) &
        Filter.by_property("date").less_or_equal(end_date)
    ),
    limit=10
)

# Query results
for obj in response.objects:
    print(f"QUERY RESULTS: {obj.properties}")

######################
# Run a hybrid query #
######################
response = tenant.query.hybrid(
    query="great food",
    limit=2
)

for obj in response.objects:
    print(f"HYBRID QUERY RESULTS: {obj.properties}")

#######################
# Check tenant status #
#######################
tenants = multi_tenant_collection.tenants.get()

# Check all tenants
for t in tenants:
    print(f"TENANT STATUS: name: {tenants[t].name} status: {tenants[t].activityStatus}")

#######################
# Deactivate a tenant #
#######################
# Select a tenant to update
tenant_to_update = 'yana42'

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
# Remove a tenant #
#######################
# Select a tenant to remove
tenant_to_remove = 'yana42'  # auto created
# tenant_to_remove = 'steve85'  # explicitly created

# # Uncomment to recreate the example tenant
# new_tenant = multi_tenant_collection.with_tenant(tenant_to_remove)
# new_tenant.data.insert({
#     "date": datetime(2024, 7, 7).replace(tzinfo=timezone.utc),
#     "tags": ["events", "grand prix"],
#     "text": "La nacional rocks",
# })

# Check the initial status
tenants = multi_tenant_collection.tenants.get()
print(f"REMOVE BEFORE: name: {tenants[tenant_to_remove].name} status: {tenants[tenant_to_remove].activityStatus}")

# Caution - this will remove all of the associated data for the tenants
# multi_tenant_collection.tenants.remove([tenant_to_remove])
multi_tenant_collection.tenants.remove(tenant_to_remove)

print("REMOVE DONE")

# Check all tenants
tenants = multi_tenant_collection.tenants.get()
for t in tenants:
    print(f"REMOVE T CHECK: name: {tenants[t].name} status: {tenants[t].activityStatus}")

########################
# Close the connection #
########################
client.close()