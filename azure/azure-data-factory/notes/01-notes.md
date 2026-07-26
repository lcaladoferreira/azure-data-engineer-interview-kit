# ADF Notes 1

Interview-ready notes with definitions, decisions, and production cautions.



## 1. linked services

**Definition:** linked services is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.

## 2. datasets

**Definition:** datasets is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.

## 3. pipelines

**Definition:** pipelines is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.
