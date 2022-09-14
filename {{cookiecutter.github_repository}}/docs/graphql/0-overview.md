# Graphql API

## Endpoint
```
/graphql
```


## Authentication
For all auth related requests (login, register etc), clients need to use REST endpoints [mentioned here](../api/1-auth.md).
For clients to make authenticated requests, the auth_token value (received from login endpoint) should be included in the Authorization HTTP header. The value should be prefixed by the string literal `Bearer`, with whitespace separating the two strings. For example:


```json
{
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2F1dGhlbnRpY2F0aW9uX2lkIjoiNzY1MjE3YTgtNzU5OS00ZTI1LTljMjQtYjdjOTJlODc4MjAxIn0.972Irua8Ql0NRf_KxgYI7q1imPBkf2XJG25L94JM8Hw"
}
```
