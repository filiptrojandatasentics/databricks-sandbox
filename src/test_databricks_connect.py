# Include the cluster_id field in your configuration profile, and then
# just specify the configuration profile's name:
from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.profile("filip.trojan@datasentics.com-cluster").getOrCreate()
df = spark.read.table("test.default.wine_dataset_for_fe")
df.show(5)
