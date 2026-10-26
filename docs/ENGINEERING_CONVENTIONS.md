# Engineering conventions for additions to this service

Read the existing code before changing its behavior. Legacy endpoints may not follow these conventions.

- Actor-sensitive **new actions** must use the `X-Actor-Id` request header (temporary interview identity convention), not trust an approver ID sent in a query string. Production systems use a verified identity provider.
- Return structured error responses with meaningful messages; map missing records to `404`, invalid transitions to `409`, bad input to `422`, and unauthorized actors to `403`.
- Store business timestamps as UTC.
- For state-changing behavior, test that a *new database session* sees the result. In-memory object assertions are insufficient.
- Do not put database entities directly in public API responses.
