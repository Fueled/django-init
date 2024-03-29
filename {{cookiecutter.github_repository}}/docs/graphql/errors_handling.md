# Error Handling

There are several error types in the GraphQL API, and you may come across different ones depending on the operations you are trying to perform.

The GraphQL API handles the following three types of errors:

## Query-level errors

This error occurs if you provide wrong or unrecognized input data while performing a specified operation. GraphQL checks the syntax as you write, and if you are trying to execute an unknown operation, the editor you are using will notify you. If you proceed with sending the request, you will get a syntax error.

Below is an example of an error triggered by the wrong syntax. The following query tries to fetch the fullName field, which doesn't exist on the User type:


```
query {
  me {
    fullName
  }
}
```

Sending this query to the server would result in the following syntax error:

```json
{
  "error": {
    "errors": [
      {
        "message": "Cannot query field \"fullName\" on type \"User\". Did you mean \"firstName\" or \"lastName\"?",
        "locations": [
          {
            "line": 3,
            "column": 5
          }
        ]
      }
    ]
  }
}
```

## Data-level errors

This error occurs when the user passes invalid data as the mutation input. For example, using an email address that is associated with a user account to create a secondary account will throw a validation error since the email should be unique within a user account.

Validation errors are part of the schema, meaning we need to include them in the query to get them explicitly. In all mutations, for example, you can obtain them through the `errors` field.

Below is an example of an error triggered by validation issues:

```
mutation {
  accountRegister(
    input: {
      email: "customer@example.com"
      password: ""
      redirectUrl: "http://example.com/reset-password/"
    }
  ) {
    user {
      email
    }
    errors {
      field
      code
    }
  }
}
```

Validation errors are returned in a dedicated error field inside mutation results:

```json
{
  "data": {
    "accountRegister": {
      "user": null,
      "errors": [
        {
          "field": "email",
          "code": "UNIQUE"
        }
      ]
    }
  }
}
```

## Permission errors

This error occurs when you are trying to perform a specific operation but are not authorized to do so; in other words, you have no sufficient permissions assigned.

Below is an example of an error triggered by insufficient authorization. The `users` query requires appropriate admin permissions:

```
query {
  users(first: 20) {
    edges {
      node {
        id
      }
    }
  }
}
```

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
  ],
  "data": {
    "users": null
  }
}
```
