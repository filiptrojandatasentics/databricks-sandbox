# Databricks notebook source
df = spark.read.table("test.default.wine_dataset_for_fe")
df.show(3)
