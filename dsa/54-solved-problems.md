# 54 DSA Problems for Data Engineers

Algorithm problems framed as ingestion, orchestration and data-quality tasks.



## 1. Hash-Map Deduplication — variation 1

**Problem:** Solve a production-flavored hash-map deduplication task while retaining deterministic output.

**Solution:** Use a set keyed by the business identifier; preserve order separately if required.

**Complexity:** O(n) time, O(n) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 2. Sliding-Window Anomaly Scan — variation 1

**Problem:** Solve a production-flavored sliding-window anomaly scan task while retaining deterministic output.

**Solution:** Maintain window sum/count and evict the oldest value.

**Complexity:** O(n) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 3. Heap Top-K Records — variation 1

**Problem:** Solve a production-flavored heap top-k records task while retaining deterministic output.

**Solution:** Maintain a min-heap of size k.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 4. Merge Sorted Streams — variation 1

**Problem:** Solve a production-flavored merge sorted streams task while retaining deterministic output.

**Solution:** Use a heap containing one head item per stream.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 5. Graph Dependency Ordering — variation 1

**Problem:** Solve a production-flavored graph dependency ordering task while retaining deterministic output.

**Solution:** Apply Kahn's topological sort and detect a cycle if nodes remain.

**Complexity:** O(V+E).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 6. Interval Consolidation — variation 1

**Problem:** Solve a production-flavored interval consolidation task while retaining deterministic output.

**Solution:** Sort by start then merge overlapping intervals.

**Complexity:** O(n log n).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 7. Hash-Map Deduplication — variation 2

**Problem:** Solve a production-flavored hash-map deduplication task while retaining deterministic output.

**Solution:** Use a set keyed by the business identifier; preserve order separately if required.

**Complexity:** O(n) time, O(n) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 8. Sliding-Window Anomaly Scan — variation 2

**Problem:** Solve a production-flavored sliding-window anomaly scan task while retaining deterministic output.

**Solution:** Maintain window sum/count and evict the oldest value.

**Complexity:** O(n) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 9. Heap Top-K Records — variation 2

**Problem:** Solve a production-flavored heap top-k records task while retaining deterministic output.

**Solution:** Maintain a min-heap of size k.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 10. Merge Sorted Streams — variation 2

**Problem:** Solve a production-flavored merge sorted streams task while retaining deterministic output.

**Solution:** Use a heap containing one head item per stream.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 11. Graph Dependency Ordering — variation 2

**Problem:** Solve a production-flavored graph dependency ordering task while retaining deterministic output.

**Solution:** Apply Kahn's topological sort and detect a cycle if nodes remain.

**Complexity:** O(V+E).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 12. Interval Consolidation — variation 2

**Problem:** Solve a production-flavored interval consolidation task while retaining deterministic output.

**Solution:** Sort by start then merge overlapping intervals.

**Complexity:** O(n log n).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 13. Hash-Map Deduplication — variation 3

**Problem:** Solve a production-flavored hash-map deduplication task while retaining deterministic output.

**Solution:** Use a set keyed by the business identifier; preserve order separately if required.

**Complexity:** O(n) time, O(n) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 14. Sliding-Window Anomaly Scan — variation 3

**Problem:** Solve a production-flavored sliding-window anomaly scan task while retaining deterministic output.

**Solution:** Maintain window sum/count and evict the oldest value.

**Complexity:** O(n) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 15. Heap Top-K Records — variation 3

**Problem:** Solve a production-flavored heap top-k records task while retaining deterministic output.

**Solution:** Maintain a min-heap of size k.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 16. Merge Sorted Streams — variation 3

**Problem:** Solve a production-flavored merge sorted streams task while retaining deterministic output.

**Solution:** Use a heap containing one head item per stream.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 17. Graph Dependency Ordering — variation 3

**Problem:** Solve a production-flavored graph dependency ordering task while retaining deterministic output.

**Solution:** Apply Kahn's topological sort and detect a cycle if nodes remain.

**Complexity:** O(V+E).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 18. Interval Consolidation — variation 3

**Problem:** Solve a production-flavored interval consolidation task while retaining deterministic output.

**Solution:** Sort by start then merge overlapping intervals.

**Complexity:** O(n log n).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 19. Hash-Map Deduplication — variation 4

**Problem:** Solve a production-flavored hash-map deduplication task while retaining deterministic output.

**Solution:** Use a set keyed by the business identifier; preserve order separately if required.

**Complexity:** O(n) time, O(n) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 20. Sliding-Window Anomaly Scan — variation 4

**Problem:** Solve a production-flavored sliding-window anomaly scan task while retaining deterministic output.

**Solution:** Maintain window sum/count and evict the oldest value.

**Complexity:** O(n) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 21. Heap Top-K Records — variation 4

**Problem:** Solve a production-flavored heap top-k records task while retaining deterministic output.

**Solution:** Maintain a min-heap of size k.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 22. Merge Sorted Streams — variation 4

**Problem:** Solve a production-flavored merge sorted streams task while retaining deterministic output.

**Solution:** Use a heap containing one head item per stream.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 23. Graph Dependency Ordering — variation 4

**Problem:** Solve a production-flavored graph dependency ordering task while retaining deterministic output.

**Solution:** Apply Kahn's topological sort and detect a cycle if nodes remain.

**Complexity:** O(V+E).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 24. Interval Consolidation — variation 4

**Problem:** Solve a production-flavored interval consolidation task while retaining deterministic output.

**Solution:** Sort by start then merge overlapping intervals.

**Complexity:** O(n log n).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 25. Hash-Map Deduplication — variation 5

**Problem:** Solve a production-flavored hash-map deduplication task while retaining deterministic output.

**Solution:** Use a set keyed by the business identifier; preserve order separately if required.

**Complexity:** O(n) time, O(n) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 26. Sliding-Window Anomaly Scan — variation 5

**Problem:** Solve a production-flavored sliding-window anomaly scan task while retaining deterministic output.

**Solution:** Maintain window sum/count and evict the oldest value.

**Complexity:** O(n) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 27. Heap Top-K Records — variation 5

**Problem:** Solve a production-flavored heap top-k records task while retaining deterministic output.

**Solution:** Maintain a min-heap of size k.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 28. Merge Sorted Streams — variation 5

**Problem:** Solve a production-flavored merge sorted streams task while retaining deterministic output.

**Solution:** Use a heap containing one head item per stream.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 29. Graph Dependency Ordering — variation 5

**Problem:** Solve a production-flavored graph dependency ordering task while retaining deterministic output.

**Solution:** Apply Kahn's topological sort and detect a cycle if nodes remain.

**Complexity:** O(V+E).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 30. Interval Consolidation — variation 5

**Problem:** Solve a production-flavored interval consolidation task while retaining deterministic output.

**Solution:** Sort by start then merge overlapping intervals.

**Complexity:** O(n log n).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 31. Hash-Map Deduplication — variation 6

**Problem:** Solve a production-flavored hash-map deduplication task while retaining deterministic output.

**Solution:** Use a set keyed by the business identifier; preserve order separately if required.

**Complexity:** O(n) time, O(n) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 32. Sliding-Window Anomaly Scan — variation 6

**Problem:** Solve a production-flavored sliding-window anomaly scan task while retaining deterministic output.

**Solution:** Maintain window sum/count and evict the oldest value.

**Complexity:** O(n) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 33. Heap Top-K Records — variation 6

**Problem:** Solve a production-flavored heap top-k records task while retaining deterministic output.

**Solution:** Maintain a min-heap of size k.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 34. Merge Sorted Streams — variation 6

**Problem:** Solve a production-flavored merge sorted streams task while retaining deterministic output.

**Solution:** Use a heap containing one head item per stream.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 35. Graph Dependency Ordering — variation 6

**Problem:** Solve a production-flavored graph dependency ordering task while retaining deterministic output.

**Solution:** Apply Kahn's topological sort and detect a cycle if nodes remain.

**Complexity:** O(V+E).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 36. Interval Consolidation — variation 6

**Problem:** Solve a production-flavored interval consolidation task while retaining deterministic output.

**Solution:** Sort by start then merge overlapping intervals.

**Complexity:** O(n log n).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 37. Hash-Map Deduplication — variation 7

**Problem:** Solve a production-flavored hash-map deduplication task while retaining deterministic output.

**Solution:** Use a set keyed by the business identifier; preserve order separately if required.

**Complexity:** O(n) time, O(n) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 38. Sliding-Window Anomaly Scan — variation 7

**Problem:** Solve a production-flavored sliding-window anomaly scan task while retaining deterministic output.

**Solution:** Maintain window sum/count and evict the oldest value.

**Complexity:** O(n) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 39. Heap Top-K Records — variation 7

**Problem:** Solve a production-flavored heap top-k records task while retaining deterministic output.

**Solution:** Maintain a min-heap of size k.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 40. Merge Sorted Streams — variation 7

**Problem:** Solve a production-flavored merge sorted streams task while retaining deterministic output.

**Solution:** Use a heap containing one head item per stream.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 41. Graph Dependency Ordering — variation 7

**Problem:** Solve a production-flavored graph dependency ordering task while retaining deterministic output.

**Solution:** Apply Kahn's topological sort and detect a cycle if nodes remain.

**Complexity:** O(V+E).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 42. Interval Consolidation — variation 7

**Problem:** Solve a production-flavored interval consolidation task while retaining deterministic output.

**Solution:** Sort by start then merge overlapping intervals.

**Complexity:** O(n log n).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 43. Hash-Map Deduplication — variation 8

**Problem:** Solve a production-flavored hash-map deduplication task while retaining deterministic output.

**Solution:** Use a set keyed by the business identifier; preserve order separately if required.

**Complexity:** O(n) time, O(n) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 44. Sliding-Window Anomaly Scan — variation 8

**Problem:** Solve a production-flavored sliding-window anomaly scan task while retaining deterministic output.

**Solution:** Maintain window sum/count and evict the oldest value.

**Complexity:** O(n) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 45. Heap Top-K Records — variation 8

**Problem:** Solve a production-flavored heap top-k records task while retaining deterministic output.

**Solution:** Maintain a min-heap of size k.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 46. Merge Sorted Streams — variation 8

**Problem:** Solve a production-flavored merge sorted streams task while retaining deterministic output.

**Solution:** Use a heap containing one head item per stream.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 47. Graph Dependency Ordering — variation 8

**Problem:** Solve a production-flavored graph dependency ordering task while retaining deterministic output.

**Solution:** Apply Kahn's topological sort and detect a cycle if nodes remain.

**Complexity:** O(V+E).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 48. Interval Consolidation — variation 8

**Problem:** Solve a production-flavored interval consolidation task while retaining deterministic output.

**Solution:** Sort by start then merge overlapping intervals.

**Complexity:** O(n log n).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 49. Hash-Map Deduplication — variation 9

**Problem:** Solve a production-flavored hash-map deduplication task while retaining deterministic output.

**Solution:** Use a set keyed by the business identifier; preserve order separately if required.

**Complexity:** O(n) time, O(n) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 50. Sliding-Window Anomaly Scan — variation 9

**Problem:** Solve a production-flavored sliding-window anomaly scan task while retaining deterministic output.

**Solution:** Maintain window sum/count and evict the oldest value.

**Complexity:** O(n) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 51. Heap Top-K Records — variation 9

**Problem:** Solve a production-flavored heap top-k records task while retaining deterministic output.

**Solution:** Maintain a min-heap of size k.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 52. Merge Sorted Streams — variation 9

**Problem:** Solve a production-flavored merge sorted streams task while retaining deterministic output.

**Solution:** Use a heap containing one head item per stream.

**Complexity:** O(n log k) time, O(k) space.

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 53. Graph Dependency Ordering — variation 9

**Problem:** Solve a production-flavored graph dependency ordering task while retaining deterministic output.

**Solution:** Apply Kahn's topological sort and detect a cycle if nodes remain.

**Complexity:** O(V+E).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.

## 54. Interval Consolidation — variation 9

**Problem:** Solve a production-flavored interval consolidation task while retaining deterministic output.

**Solution:** Sort by start then merge overlapping intervals.

**Complexity:** O(n log n).

**Engineering note:** clarify memory bounds, malformed input, duplicate semantics and whether approximate results are acceptable.
