# 04 — Debug and extend a search index

This starter contains several bugs. Do not rewrite everything immediately.

Your goals:

1. Read the tests and reproduce the failures.
2. Identify each violated invariant before changing code.
3. Fix token normalization and AND-query semantics.
4. Preserve input document order in results.
5. Add filters written as `owner:ada` and `type:experiment`.
6. Validate duplicate/missing IDs and return defensive copies.

Treat this as a 50-minute mock: 5 minutes clarification, 10 minutes diagnosis/approach, 25 minutes implementation, and 10 minutes tests plus explanation.
