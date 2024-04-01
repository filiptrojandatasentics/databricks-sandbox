import openml
from databricks.connect import DatabricksSession


spark = DatabricksSession.builder.profile("filip.trojan@datasentics.com-cluster").getOrCreate()
# https://www.openml.org/search?type=data&status=active&id=45568
dataset = openml.datasets.get_dataset(45568)
df, _, _, _ = dataset.get_data(dataset_format="dataframe")
df["tenure"] = df["tenure"].astype(int)
df.info()
result = spark.sql("create schema if not exists test.telco_customer_churn")
print(f"create schema: {result}")
spark_df = spark.createDataFrame(df)
spark_df.write.mode("overwrite").saveAsTable("test.telco_customer_churn.input_table")
