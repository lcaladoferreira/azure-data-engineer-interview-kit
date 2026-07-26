# Azure Functions Scenario Q&A — 30

30 original interview questions with concise, production-oriented answers.


## 1. Design: triggers

**Question:** A production Azure Functions workload using **triggers** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **triggers**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 2. Design: bindings

**Question:** A production Azure Functions workload using **bindings** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **bindings**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 3. Design: hosting plans

**Question:** A production Azure Functions workload using **hosting plans** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **hosting plans**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 4. Design: managed identity

**Question:** A production Azure Functions workload using **managed identity** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **managed identity**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 5. Design: durable functions

**Question:** A production Azure Functions workload using **durable functions** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **durable functions**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 6. Design: retries

**Question:** A production Azure Functions workload using **retries** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **retries**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 7. Design: scale

**Question:** A production Azure Functions workload using **scale** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **scale**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 8. Design: cold start

**Question:** A production Azure Functions workload using **cold start** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **cold start**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 9. Design: monitoring

**Question:** A production Azure Functions workload using **monitoring** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **monitoring**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 10. Design: grain and data contracts

**Question:** A production Azure Functions workload using **grain and data contracts** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **grain and data contracts**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 11. Design: idempotency

**Question:** A production Azure Functions workload using **idempotency** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **idempotency**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 12. Design: partitioning

**Question:** A production Azure Functions workload using **partitioning** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **partitioning**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 13. Design: schema evolution

**Question:** A production Azure Functions workload using **schema evolution** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **schema evolution**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 14. Design: watermarks

**Question:** A production Azure Functions workload using **watermarks** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **watermarks**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 15. Design: late-arriving data

**Question:** A production Azure Functions workload using **late-arriving data** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **late-arriving data**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 16. Design: deduplication

**Question:** A production Azure Functions workload using **deduplication** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **deduplication**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 17. Design: observability

**Question:** A production Azure Functions workload using **observability** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **observability**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 18. Design: data quality

**Question:** A production Azure Functions workload using **data quality** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **data quality**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 19. Design: least privilege

**Question:** A production Azure Functions workload using **least privilege** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **least privilege**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 20. Design: encryption

**Question:** A production Azure Functions workload using **encryption** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **encryption**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 21. Design: cost optimization

**Question:** A production Azure Functions workload using **cost optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **cost optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 22. Design: RPO and RTO

**Question:** A production Azure Functions workload using **RPO and RTO** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **RPO and RTO**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 23. Design: backfill and replay

**Question:** A production Azure Functions workload using **backfill and replay** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **backfill and replay**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 24. Design: lineage

**Question:** A production Azure Functions workload using **lineage** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **lineage**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 25. Design: testing

**Question:** A production Azure Functions workload using **testing** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **testing**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 26. Design: deployment

**Question:** A production Azure Functions workload using **deployment** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **deployment**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 27. Design: performance tuning

**Question:** A production Azure Functions workload using **performance tuning** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **performance tuning**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 28. Design: skew

**Question:** A production Azure Functions workload using **skew** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **skew**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 29. Design: small files

**Question:** A production Azure Functions workload using **small files** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **small files**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 30. Troubleshoot: triggers

**Question:** A production Azure Functions workload using **triggers** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **triggers**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.
