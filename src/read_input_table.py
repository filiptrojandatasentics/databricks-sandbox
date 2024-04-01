from databricks.connect import DatabricksSession


spark = DatabricksSession.builder.profile("filip.trojan@datasentics.com-cluster").getOrCreate()
spark_df = spark.sql("select * from test.telco_customer_churn.input_table")
df = spark_df.select("*").toPandas()
df.info()
x = df.drop(columns=["Churn"])
y = df["Churn"]
print(y.value_counts())
