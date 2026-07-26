# ADF Notes 5

Interview-ready notes with definitions, decisions, and production cautions.



## 1. managed identity

**Definition:** managed identity is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.

## 2. private endpoints

**Definition:** private endpoints is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.

## 3. incremental loads

**Definition:** incremental loads is useful only when tied to an explicit data contract and workload requirement.

**Decision rule:** choose it when it reduces the dominant risk—correctness, latency, scale, operability or cost—and verify the assumption with a representative benchmark.

**Common trap:** adopting it as a fashionable default without considering skew, schema evolution, retries, access controls, lineage and recovery.
