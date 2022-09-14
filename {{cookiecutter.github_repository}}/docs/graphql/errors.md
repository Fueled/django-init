# Errors

## Generic Errors


For /graphql requests, the API will return the error in the following format:

```json
{
  "errors": [
    {
      "message": "You do not have permission to perform this action",
      "locations": [
        {
          "line": 33,
          "column": 3
        }
      ],
      "path": [
        "users"
      ]
    }
  ]
}
```

__NOTE__: The copy for most of these error messages can be changed by backend developers.
