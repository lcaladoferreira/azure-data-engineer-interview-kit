# HBase, Hive, Scala, Spark and Sqoop Notes

Interview-ready notes with definitions, decisions, and production cautions.



## 1. HBase row keys

**Definition:** HBase row keys is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.

## 2. HBase regions

**Definition:** HBase regions is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.

## 3. Hive metastore

**Definition:** Hive metastore is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.

## 4. Hive partitions

**Definition:** Hive partitions is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.

## 5. Scala immutability

**Definition:** Scala immutability is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.

## 6. Spark execution

**Definition:** Spark execution is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.

## 7. Sqoop import

**Definition:** Sqoop import is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.

## 8. migration to modern ingestion

**Definition:** migration to modern ingestion is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.
