# DP-700 — 120 Scenario and Concept Questions

120 original interview questions with concise, production-oriented answers.


## 1. Design: Fabric workspace settings

**Question:** A production Microsoft Fabric workload using **Fabric workspace settings** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Fabric workspace settings**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 2. Design: lifecycle management

**Question:** A production Microsoft Fabric workload using **lifecycle management** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **lifecycle management**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 3. Design: pipeline errors

**Question:** A production Microsoft Fabric workload using **pipeline errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **pipeline errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 4. Design: Dataflow Gen2 errors

**Question:** A production Microsoft Fabric workload using **Dataflow Gen2 errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Dataflow Gen2 errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 5. Design: notebook errors

**Question:** A production Microsoft Fabric workload using **notebook errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **notebook errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 6. Design: Eventhouse errors

**Question:** A production Microsoft Fabric workload using **Eventhouse errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Eventhouse errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 7. Design: OneLake shortcuts

**Question:** A production Microsoft Fabric workload using **OneLake shortcuts** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **OneLake shortcuts**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 8. Design: Lakehouse optimization

**Question:** A production Microsoft Fabric workload using **Lakehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Lakehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 9. Design: warehouse optimization

**Question:** A production Microsoft Fabric workload using **warehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **warehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 10. Design: Spark optimization

**Question:** A production Microsoft Fabric workload using **Spark optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Spark optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 11. Design: ingestion patterns

**Question:** A production Microsoft Fabric workload using **ingestion patterns** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **ingestion patterns**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 12. Design: transformation

**Question:** A production Microsoft Fabric workload using **transformation** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **transformation**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 13. Design: security

**Question:** A production Microsoft Fabric workload using **security** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **security**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 14. Design: monitoring

**Question:** A production Microsoft Fabric workload using **monitoring** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **monitoring**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 15. Design: KQL

**Question:** A production Microsoft Fabric workload using **KQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **KQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 16. Design: SQL

**Question:** A production Microsoft Fabric workload using **SQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **SQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 17. Design: PySpark

**Question:** A production Microsoft Fabric workload using **PySpark** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **PySpark**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 18. Troubleshoot: Fabric workspace settings

**Question:** A production Microsoft Fabric workload using **Fabric workspace settings** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Fabric workspace settings**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 19. Troubleshoot: lifecycle management

**Question:** A production Microsoft Fabric workload using **lifecycle management** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **lifecycle management**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 20. Troubleshoot: pipeline errors

**Question:** A production Microsoft Fabric workload using **pipeline errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **pipeline errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 21. Troubleshoot: Dataflow Gen2 errors

**Question:** A production Microsoft Fabric workload using **Dataflow Gen2 errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Dataflow Gen2 errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 22. Troubleshoot: notebook errors

**Question:** A production Microsoft Fabric workload using **notebook errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **notebook errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 23. Troubleshoot: Eventhouse errors

**Question:** A production Microsoft Fabric workload using **Eventhouse errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Eventhouse errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 24. Troubleshoot: OneLake shortcuts

**Question:** A production Microsoft Fabric workload using **OneLake shortcuts** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **OneLake shortcuts**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 25. Troubleshoot: Lakehouse optimization

**Question:** A production Microsoft Fabric workload using **Lakehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Lakehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 26. Troubleshoot: warehouse optimization

**Question:** A production Microsoft Fabric workload using **warehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **warehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 27. Troubleshoot: Spark optimization

**Question:** A production Microsoft Fabric workload using **Spark optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Spark optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 28. Troubleshoot: ingestion patterns

**Question:** A production Microsoft Fabric workload using **ingestion patterns** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **ingestion patterns**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 29. Troubleshoot: transformation

**Question:** A production Microsoft Fabric workload using **transformation** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **transformation**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 30. Troubleshoot: security

**Question:** A production Microsoft Fabric workload using **security** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **security**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 31. Troubleshoot: monitoring

**Question:** A production Microsoft Fabric workload using **monitoring** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **monitoring**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 32. Troubleshoot: KQL

**Question:** A production Microsoft Fabric workload using **KQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **KQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 33. Troubleshoot: SQL

**Question:** A production Microsoft Fabric workload using **SQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **SQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 34. Troubleshoot: PySpark

**Question:** A production Microsoft Fabric workload using **PySpark** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **PySpark**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 35. Optimize: Fabric workspace settings

**Question:** A production Microsoft Fabric workload using **Fabric workspace settings** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Fabric workspace settings**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 36. Optimize: lifecycle management

**Question:** A production Microsoft Fabric workload using **lifecycle management** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **lifecycle management**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 37. Optimize: pipeline errors

**Question:** A production Microsoft Fabric workload using **pipeline errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **pipeline errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 38. Optimize: Dataflow Gen2 errors

**Question:** A production Microsoft Fabric workload using **Dataflow Gen2 errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Dataflow Gen2 errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 39. Optimize: notebook errors

**Question:** A production Microsoft Fabric workload using **notebook errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **notebook errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 40. Optimize: Eventhouse errors

**Question:** A production Microsoft Fabric workload using **Eventhouse errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Eventhouse errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 41. Optimize: OneLake shortcuts

**Question:** A production Microsoft Fabric workload using **OneLake shortcuts** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **OneLake shortcuts**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 42. Optimize: Lakehouse optimization

**Question:** A production Microsoft Fabric workload using **Lakehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Lakehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 43. Optimize: warehouse optimization

**Question:** A production Microsoft Fabric workload using **warehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **warehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 44. Optimize: Spark optimization

**Question:** A production Microsoft Fabric workload using **Spark optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Spark optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 45. Optimize: ingestion patterns

**Question:** A production Microsoft Fabric workload using **ingestion patterns** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **ingestion patterns**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 46. Optimize: transformation

**Question:** A production Microsoft Fabric workload using **transformation** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **transformation**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 47. Optimize: security

**Question:** A production Microsoft Fabric workload using **security** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **security**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 48. Optimize: monitoring

**Question:** A production Microsoft Fabric workload using **monitoring** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **monitoring**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 49. Optimize: KQL

**Question:** A production Microsoft Fabric workload using **KQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **KQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 50. Optimize: SQL

**Question:** A production Microsoft Fabric workload using **SQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **SQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 51. Optimize: PySpark

**Question:** A production Microsoft Fabric workload using **PySpark** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **PySpark**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 52. Secure: Fabric workspace settings

**Question:** A production Microsoft Fabric workload using **Fabric workspace settings** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Fabric workspace settings**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 53. Secure: lifecycle management

**Question:** A production Microsoft Fabric workload using **lifecycle management** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **lifecycle management**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 54. Secure: pipeline errors

**Question:** A production Microsoft Fabric workload using **pipeline errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **pipeline errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 55. Secure: Dataflow Gen2 errors

**Question:** A production Microsoft Fabric workload using **Dataflow Gen2 errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Dataflow Gen2 errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 56. Secure: notebook errors

**Question:** A production Microsoft Fabric workload using **notebook errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **notebook errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 57. Secure: Eventhouse errors

**Question:** A production Microsoft Fabric workload using **Eventhouse errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Eventhouse errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 58. Secure: OneLake shortcuts

**Question:** A production Microsoft Fabric workload using **OneLake shortcuts** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **OneLake shortcuts**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 59. Secure: Lakehouse optimization

**Question:** A production Microsoft Fabric workload using **Lakehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Lakehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 60. Secure: warehouse optimization

**Question:** A production Microsoft Fabric workload using **warehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **warehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 61. Secure: Spark optimization

**Question:** A production Microsoft Fabric workload using **Spark optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Spark optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 62. Secure: ingestion patterns

**Question:** A production Microsoft Fabric workload using **ingestion patterns** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **ingestion patterns**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 63. Secure: transformation

**Question:** A production Microsoft Fabric workload using **transformation** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **transformation**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 64. Secure: security

**Question:** A production Microsoft Fabric workload using **security** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **security**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 65. Secure: monitoring

**Question:** A production Microsoft Fabric workload using **monitoring** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **monitoring**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 66. Secure: KQL

**Question:** A production Microsoft Fabric workload using **KQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **KQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 67. Secure: SQL

**Question:** A production Microsoft Fabric workload using **SQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **SQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 68. Secure: PySpark

**Question:** A production Microsoft Fabric workload using **PySpark** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you secure first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **PySpark**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Apply least privilege, data protection, and auditable operations. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 69. Operate: Fabric workspace settings

**Question:** A production Microsoft Fabric workload using **Fabric workspace settings** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Fabric workspace settings**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 70. Operate: lifecycle management

**Question:** A production Microsoft Fabric workload using **lifecycle management** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **lifecycle management**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 71. Operate: pipeline errors

**Question:** A production Microsoft Fabric workload using **pipeline errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **pipeline errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 72. Operate: Dataflow Gen2 errors

**Question:** A production Microsoft Fabric workload using **Dataflow Gen2 errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Dataflow Gen2 errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 73. Operate: notebook errors

**Question:** A production Microsoft Fabric workload using **notebook errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **notebook errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 74. Operate: Eventhouse errors

**Question:** A production Microsoft Fabric workload using **Eventhouse errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Eventhouse errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 75. Operate: OneLake shortcuts

**Question:** A production Microsoft Fabric workload using **OneLake shortcuts** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **OneLake shortcuts**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 76. Operate: Lakehouse optimization

**Question:** A production Microsoft Fabric workload using **Lakehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Lakehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 77. Operate: warehouse optimization

**Question:** A production Microsoft Fabric workload using **warehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **warehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 78. Operate: Spark optimization

**Question:** A production Microsoft Fabric workload using **Spark optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Spark optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 79. Operate: ingestion patterns

**Question:** A production Microsoft Fabric workload using **ingestion patterns** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **ingestion patterns**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 80. Operate: transformation

**Question:** A production Microsoft Fabric workload using **transformation** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **transformation**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 81. Operate: security

**Question:** A production Microsoft Fabric workload using **security** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **security**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 82. Operate: monitoring

**Question:** A production Microsoft Fabric workload using **monitoring** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **monitoring**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 83. Operate: KQL

**Question:** A production Microsoft Fabric workload using **KQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **KQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 84. Operate: SQL

**Question:** A production Microsoft Fabric workload using **SQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **SQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 85. Operate: PySpark

**Question:** A production Microsoft Fabric workload using **PySpark** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you operate first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **PySpark**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Define observability, retry behavior, ownership, and recovery. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 86. Design: Fabric workspace settings

**Question:** A production Microsoft Fabric workload using **Fabric workspace settings** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Fabric workspace settings**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 87. Design: lifecycle management

**Question:** A production Microsoft Fabric workload using **lifecycle management** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **lifecycle management**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 88. Design: pipeline errors

**Question:** A production Microsoft Fabric workload using **pipeline errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **pipeline errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 89. Design: Dataflow Gen2 errors

**Question:** A production Microsoft Fabric workload using **Dataflow Gen2 errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Dataflow Gen2 errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 90. Design: notebook errors

**Question:** A production Microsoft Fabric workload using **notebook errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **notebook errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 91. Design: Eventhouse errors

**Question:** A production Microsoft Fabric workload using **Eventhouse errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Eventhouse errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 92. Design: OneLake shortcuts

**Question:** A production Microsoft Fabric workload using **OneLake shortcuts** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **OneLake shortcuts**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 93. Design: Lakehouse optimization

**Question:** A production Microsoft Fabric workload using **Lakehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Lakehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 94. Design: warehouse optimization

**Question:** A production Microsoft Fabric workload using **warehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **warehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 95. Design: Spark optimization

**Question:** A production Microsoft Fabric workload using **Spark optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Spark optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 96. Design: ingestion patterns

**Question:** A production Microsoft Fabric workload using **ingestion patterns** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **ingestion patterns**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 97. Design: transformation

**Question:** A production Microsoft Fabric workload using **transformation** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **transformation**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 98. Design: security

**Question:** A production Microsoft Fabric workload using **security** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **security**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 99. Design: monitoring

**Question:** A production Microsoft Fabric workload using **monitoring** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **monitoring**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 100. Design: KQL

**Question:** A production Microsoft Fabric workload using **KQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **KQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 101. Design: SQL

**Question:** A production Microsoft Fabric workload using **SQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **SQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 102. Design: PySpark

**Question:** A production Microsoft Fabric workload using **PySpark** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **PySpark**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 103. Troubleshoot: Fabric workspace settings

**Question:** A production Microsoft Fabric workload using **Fabric workspace settings** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Fabric workspace settings**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 104. Troubleshoot: lifecycle management

**Question:** A production Microsoft Fabric workload using **lifecycle management** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **lifecycle management**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 105. Troubleshoot: pipeline errors

**Question:** A production Microsoft Fabric workload using **pipeline errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **pipeline errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 106. Troubleshoot: Dataflow Gen2 errors

**Question:** A production Microsoft Fabric workload using **Dataflow Gen2 errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Dataflow Gen2 errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 107. Troubleshoot: notebook errors

**Question:** A production Microsoft Fabric workload using **notebook errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **notebook errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 108. Troubleshoot: Eventhouse errors

**Question:** A production Microsoft Fabric workload using **Eventhouse errors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Eventhouse errors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 109. Troubleshoot: OneLake shortcuts

**Question:** A production Microsoft Fabric workload using **OneLake shortcuts** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **OneLake shortcuts**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 110. Troubleshoot: Lakehouse optimization

**Question:** A production Microsoft Fabric workload using **Lakehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Lakehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 111. Troubleshoot: warehouse optimization

**Question:** A production Microsoft Fabric workload using **warehouse optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **warehouse optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 112. Troubleshoot: Spark optimization

**Question:** A production Microsoft Fabric workload using **Spark optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Spark optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 113. Troubleshoot: ingestion patterns

**Question:** A production Microsoft Fabric workload using **ingestion patterns** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **ingestion patterns**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 114. Troubleshoot: transformation

**Question:** A production Microsoft Fabric workload using **transformation** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **transformation**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 115. Troubleshoot: security

**Question:** A production Microsoft Fabric workload using **security** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **security**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 116. Troubleshoot: monitoring

**Question:** A production Microsoft Fabric workload using **monitoring** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **monitoring**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 117. Troubleshoot: KQL

**Question:** A production Microsoft Fabric workload using **KQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **KQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 118. Troubleshoot: SQL

**Question:** A production Microsoft Fabric workload using **SQL** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **SQL**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 119. Troubleshoot: PySpark

**Question:** A production Microsoft Fabric workload using **PySpark** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **PySpark**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 120. Optimize: Fabric workspace settings

**Question:** A production Microsoft Fabric workload using **Fabric workspace settings** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you optimize first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **Fabric workspace settings**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Choose the highest-leverage optimization and explain what to measure. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.
