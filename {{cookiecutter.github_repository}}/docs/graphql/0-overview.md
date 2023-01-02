# GraphQL

## Authentication

For all auth related requests (login, register etc), clients need to refer to [docs mentioned here](1-auth.md).
For clients to make authenticated requests, the auth_token value (received from login endpoint) should be included in the Authorization HTTP header. The value should be prefixed by the string literal `Bearer`, with whitespace separating the two strings.

## API Endpoint

```
POST /graphql
```

All the queries and mutations will be a POST request to the above endpoint. We've documented a sample header and payload to be sent with the request.

__Headers__

```json
{
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2F1dGhlbnRpY2F0aW9uX2lkIjoiNzY1MjE3YTgtNzU5OS00ZTI1LTljMjQtYjdjOTJlODc4MjAxIn0.972Irua8Ql0NRf_KxgYI7q1imPBkf2XJG25L94JM8Hw"
}
```

__Payload__

```json
{
  "query": "query MyInfo { me { id firstName lastName email } }",
  "variables":null,
  "operationName":"MyInfo"
}
```

## Pagination

Pagination is required in most queries that return lists of items in the GraphQL API. It limits the number of results returned by the server to a more manageable size and avoids data flow disruptions.

There are two types of lists in GraphQL:

- `[Foo]` is a simple list. It is used to query a list containing several items. An excellent example of a simple list could be a query for product variants which returns a list with a manageable number of results.
- `FooConnection` represents a more complex list. When queried, it will return an unknown or large number of results.

Pagination is used to help you handle large amounts of items returned by the connection list type.

Pagination model is based on the [GraphQL Connection Specification](https://relay.dev/graphql/connections.htm). Its schema looks like this:

```
type FooConnection {
  pageInfo: PageInfo!
  edges: [FooEdge!]!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

type FooEdge {
  node: Foo!
  cursor: String!
}
```
