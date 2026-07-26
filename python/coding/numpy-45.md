# NumPy Coding Q&A — 45 Solved Problems

Vectorized array exercises for data engineers.



## 1. Replace Nan Values

**Problem:** Given `a`, replace NaN values without a Python row loop.

```python
result = np.nan_to_num(a, nan=0.0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 2. Standardize Columns

**Problem:** Given `a`, standardize columns without a Python row loop.

```python
result = (a - a.mean(axis=0)) / a.std(axis=0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 3. Filter Positive Rows

**Problem:** Given `a`, filter positive rows without a Python row loop.

```python
result = a[(a > 0).all(axis=1)]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 4. Compute Pairwise Differences

**Problem:** Given `a`, compute pairwise differences without a Python row loop.

```python
result = a[:, None] - a[None, :]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 5. Find Unique Rows

**Problem:** Given `a`, find unique rows without a Python row loop.

```python
result = np.unique(a, axis=0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 6. Clip Outliers

**Problem:** Given `a`, clip outliers without a Python row loop.

```python
result = np.clip(a, lower, upper)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 7. Aggregate By Key

**Problem:** Given `a`, aggregate by key without a Python row loop.

```python
result = np.bincount(keys, weights=values)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 8. Sort By A Column

**Problem:** Given `a`, sort by a column without a Python row loop.

```python
result = a[np.argsort(a[:, column])]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 9. Reshape A Batch

**Problem:** Given `a`, reshape a batch without a Python row loop.

```python
result = a.reshape(batch_size, -1)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 10. Replace Nan Values

**Problem:** Given `a`, replace NaN values without a Python row loop.

```python
result = np.nan_to_num(a, nan=0.0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 11. Standardize Columns

**Problem:** Given `a`, standardize columns without a Python row loop.

```python
result = (a - a.mean(axis=0)) / a.std(axis=0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 12. Filter Positive Rows

**Problem:** Given `a`, filter positive rows without a Python row loop.

```python
result = a[(a > 0).all(axis=1)]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 13. Compute Pairwise Differences

**Problem:** Given `a`, compute pairwise differences without a Python row loop.

```python
result = a[:, None] - a[None, :]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 14. Find Unique Rows

**Problem:** Given `a`, find unique rows without a Python row loop.

```python
result = np.unique(a, axis=0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 15. Clip Outliers

**Problem:** Given `a`, clip outliers without a Python row loop.

```python
result = np.clip(a, lower, upper)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 16. Aggregate By Key

**Problem:** Given `a`, aggregate by key without a Python row loop.

```python
result = np.bincount(keys, weights=values)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 17. Sort By A Column

**Problem:** Given `a`, sort by a column without a Python row loop.

```python
result = a[np.argsort(a[:, column])]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 18. Reshape A Batch

**Problem:** Given `a`, reshape a batch without a Python row loop.

```python
result = a.reshape(batch_size, -1)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 19. Replace Nan Values

**Problem:** Given `a`, replace NaN values without a Python row loop.

```python
result = np.nan_to_num(a, nan=0.0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 20. Standardize Columns

**Problem:** Given `a`, standardize columns without a Python row loop.

```python
result = (a - a.mean(axis=0)) / a.std(axis=0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 21. Filter Positive Rows

**Problem:** Given `a`, filter positive rows without a Python row loop.

```python
result = a[(a > 0).all(axis=1)]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 22. Compute Pairwise Differences

**Problem:** Given `a`, compute pairwise differences without a Python row loop.

```python
result = a[:, None] - a[None, :]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 23. Find Unique Rows

**Problem:** Given `a`, find unique rows without a Python row loop.

```python
result = np.unique(a, axis=0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 24. Clip Outliers

**Problem:** Given `a`, clip outliers without a Python row loop.

```python
result = np.clip(a, lower, upper)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 25. Aggregate By Key

**Problem:** Given `a`, aggregate by key without a Python row loop.

```python
result = np.bincount(keys, weights=values)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 26. Sort By A Column

**Problem:** Given `a`, sort by a column without a Python row loop.

```python
result = a[np.argsort(a[:, column])]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 27. Reshape A Batch

**Problem:** Given `a`, reshape a batch without a Python row loop.

```python
result = a.reshape(batch_size, -1)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 28. Replace Nan Values

**Problem:** Given `a`, replace NaN values without a Python row loop.

```python
result = np.nan_to_num(a, nan=0.0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 29. Standardize Columns

**Problem:** Given `a`, standardize columns without a Python row loop.

```python
result = (a - a.mean(axis=0)) / a.std(axis=0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 30. Filter Positive Rows

**Problem:** Given `a`, filter positive rows without a Python row loop.

```python
result = a[(a > 0).all(axis=1)]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 31. Compute Pairwise Differences

**Problem:** Given `a`, compute pairwise differences without a Python row loop.

```python
result = a[:, None] - a[None, :]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 32. Find Unique Rows

**Problem:** Given `a`, find unique rows without a Python row loop.

```python
result = np.unique(a, axis=0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 33. Clip Outliers

**Problem:** Given `a`, clip outliers without a Python row loop.

```python
result = np.clip(a, lower, upper)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 34. Aggregate By Key

**Problem:** Given `a`, aggregate by key without a Python row loop.

```python
result = np.bincount(keys, weights=values)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 35. Sort By A Column

**Problem:** Given `a`, sort by a column without a Python row loop.

```python
result = a[np.argsort(a[:, column])]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 36. Reshape A Batch

**Problem:** Given `a`, reshape a batch without a Python row loop.

```python
result = a.reshape(batch_size, -1)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 37. Replace Nan Values

**Problem:** Given `a`, replace NaN values without a Python row loop.

```python
result = np.nan_to_num(a, nan=0.0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 38. Standardize Columns

**Problem:** Given `a`, standardize columns without a Python row loop.

```python
result = (a - a.mean(axis=0)) / a.std(axis=0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 39. Filter Positive Rows

**Problem:** Given `a`, filter positive rows without a Python row loop.

```python
result = a[(a > 0).all(axis=1)]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 40. Compute Pairwise Differences

**Problem:** Given `a`, compute pairwise differences without a Python row loop.

```python
result = a[:, None] - a[None, :]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 41. Find Unique Rows

**Problem:** Given `a`, find unique rows without a Python row loop.

```python
result = np.unique(a, axis=0)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 42. Clip Outliers

**Problem:** Given `a`, clip outliers without a Python row loop.

```python
result = np.clip(a, lower, upper)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 43. Aggregate By Key

**Problem:** Given `a`, aggregate by key without a Python row loop.

```python
result = np.bincount(keys, weights=values)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 44. Sort By A Column

**Problem:** Given `a`, sort by a column without a Python row loop.

```python
result = a[np.argsort(a[:, column])]
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.

## 45. Reshape A Batch

**Problem:** Given `a`, reshape a batch without a Python row loop.

```python
result = a.reshape(batch_size, -1)
```

**Note:** Check dtype, shape, broadcasting and zero-division behavior; benchmark representative arrays rather than assuming vectorization always wins.
