#! /usr/bin/python3.11
# -*- coding: utf-8 -*-

import pymilvus
from pymilvus import (
    connections,
    db,
    Collection
)
from pymilvus import utility
from sklearn.metrics.pairwise import cosine_similarity

from Milvus import createCollection, createPartition, createIndex, dropCollection



# ------------------------连接数据库----------------------------
# conn = connections.connect(db_name="Paper", host="127.0.0.1", port=19530)
# -------------------------创建集合-----------------------
# createCollection("default", "AI_paper")
# -------------------------连接集合-----------------------
# collection = Collection("AI_paper")
# --------------------------创建分区----------------------
# createPartition("AI_paper", "shards_MachineLearning")
# createPartition("AI_paper", "shards_DeepLearning")
# createPartition("AI_paper", "shards_SwarmIntelligence")
# createPartition("AI_paper", "shards_DataIntelligence")
# createPartition("AI_paper", "shards_ComputerVision")
# createPartition("AI_paper", "shards_FuzzyTheory")
# createPartition("AI_paper", "shards_HumanMachineIntelligence")
# createPartition("AI_paper", "shards_ImageProcessing")
# createPartition("AI_paper", "shards_ControlSystem")
# createPartition("AI_paper", "shards_SmartSystem")
# --------------------------创建索引-------------------
# createIndex(collection, "vector")
# ------------------------导入数据----------------------
# insert()




