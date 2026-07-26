# Logic Apps Scenario Q&A — 42

42 original interview questions with concise, production-oriented answers.


## 1. Design: workflows

**Question:** A production Logic Apps workload using **workflows** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **workflows**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 2. Design: connectors

**Question:** A production Logic Apps workload using **connectors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **connectors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 3. Design: triggers

**Question:** A production Logic Apps workload using **triggers** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **triggers**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 4. Design: actions

**Question:** A production Logic Apps workload using **actions** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **actions**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 5. Design: control flow

**Question:** A production Logic Apps workload using **control flow** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **control flow**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 6. Design: stateful

**Question:** A production Logic Apps workload using **stateful** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **stateful**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 7. Design: stateless

**Question:** A production Logic Apps workload using **stateless** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **stateless**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 8. Design: integration account

**Question:** A production Logic Apps workload using **integration account** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **integration account**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 9. Design: managed identity

**Question:** A production Logic Apps workload using **managed identity** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **managed identity**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 10. Design: retry policies

**Question:** A production Logic Apps workload using **retry policies** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **retry policies**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 11. Design: grain and data contracts

**Question:** A production Logic Apps workload using **grain and data contracts** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **grain and data contracts**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 12. Design: idempotency

**Question:** A production Logic Apps workload using **idempotency** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **idempotency**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 13. Design: partitioning

**Question:** A production Logic Apps workload using **partitioning** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **partitioning**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 14. Design: schema evolution

**Question:** A production Logic Apps workload using **schema evolution** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **schema evolution**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 15. Design: watermarks

**Question:** A production Logic Apps workload using **watermarks** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **watermarks**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 16. Design: late-arriving data

**Question:** A production Logic Apps workload using **late-arriving data** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **late-arriving data**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 17. Design: deduplication

**Question:** A production Logic Apps workload using **deduplication** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **deduplication**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 18. Design: observability

**Question:** A production Logic Apps workload using **observability** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **observability**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 19. Design: data quality

**Question:** A production Logic Apps workload using **data quality** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **data quality**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 20. Design: least privilege

**Question:** A production Logic Apps workload using **least privilege** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **least privilege**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 21. Design: encryption

**Question:** A production Logic Apps workload using **encryption** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **encryption**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 22. Design: cost optimization

**Question:** A production Logic Apps workload using **cost optimization** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **cost optimization**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 23. Design: RPO and RTO

**Question:** A production Logic Apps workload using **RPO and RTO** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **RPO and RTO**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 24. Design: backfill and replay

**Question:** A production Logic Apps workload using **backfill and replay** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **backfill and replay**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 25. Design: lineage

**Question:** A production Logic Apps workload using **lineage** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **lineage**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 26. Design: testing

**Question:** A production Logic Apps workload using **testing** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **testing**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 27. Design: deployment

**Question:** A production Logic Apps workload using **deployment** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **deployment**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 28. Design: performance tuning

**Question:** A production Logic Apps workload using **performance tuning** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **performance tuning**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 29. Design: skew

**Question:** A production Logic Apps workload using **skew** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **skew**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 30. Design: small files

**Question:** A production Logic Apps workload using **small files** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you design first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **small files**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Explain the design choice, trade-off, and operational consequence. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 31. Troubleshoot: workflows

**Question:** A production Logic Apps workload using **workflows** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **workflows**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 32. Troubleshoot: connectors

**Question:** A production Logic Apps workload using **connectors** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **connectors**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 33. Troubleshoot: triggers

**Question:** A production Logic Apps workload using **triggers** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **triggers**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 34. Troubleshoot: actions

**Question:** A production Logic Apps workload using **actions** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **actions**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 35. Troubleshoot: control flow

**Question:** A production Logic Apps workload using **control flow** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **control flow**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 36. Troubleshoot: stateful

**Question:** A production Logic Apps workload using **stateful** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **stateful**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 37. Troubleshoot: stateless

**Question:** A production Logic Apps workload using **stateless** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **stateless**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 38. Troubleshoot: integration account

**Question:** A production Logic Apps workload using **integration account** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **integration account**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 39. Troubleshoot: managed identity

**Question:** A production Logic Apps workload using **managed identity** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **managed identity**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 40. Troubleshoot: retry policies

**Question:** A production Logic Apps workload using **retry policies** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **retry policies**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 41. Troubleshoot: grain and data contracts

**Question:** A production Logic Apps workload using **grain and data contracts** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **grain and data contracts**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.

## 42. Troubleshoot: idempotency

**Question:** A production Logic Apps workload using **idempotency** has rising latency, intermittent retries, and a strict recovery SLA. As the on-call data engineer, what would you troubleshoot first?

**Answer:** Start by making the requirement measurable: throughput, latency, freshness, correctness, cost, RPO and RTO. For **idempotency**, separate control-plane configuration from data-plane behavior, reproduce the issue with the smallest representative workload, and compare current telemetry with a known-good baseline. Identify the likely failure mode, evidence to inspect, and safe remediation. Prefer an idempotent change, test it outside production, deploy progressively, and keep a rollback path. Validate the result with service metrics plus a business-level data-quality check; a technically successful run that publishes incomplete or duplicated data is still a failure.

**Strong interview signal:** state assumptions; name the metric that would confirm the diagnosis; discuss security, cost and failure recovery; and explain why the rejected alternative is weaker.
