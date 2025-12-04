"""
ESQB - Elasticsearch Query Builder
----------------------------------

Usage:

    from esqb import QueryBuilder, Match, Term, Range, Bool

    query = QueryBuilder.boolean(
        must=[Match("title", "python")],
        filter=[Term("status", "active")]
    )
    print(query.to_dict())
"""

# Import main classes from query_builder
from .query_builder import QueryBuilder, Match, Term, Range, Bool

# Define public API
__all__ = ["QueryBuilder", "Match", "Term", "Range", "Bool"]
