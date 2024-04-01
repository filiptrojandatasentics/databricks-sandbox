# Databricks notebook source
df = spark.read.table("test.telco_customer_churn.input_table")
df.show(3)
