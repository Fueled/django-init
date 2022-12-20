# Authentication

!!!info
    For API overview and usages, check out [this page](0-overview.md).


## Register

__Request__
```
mutation {
    signup (
        input: {
            email: "test@example.com",
            firstName: "a",
            lastName: "b",
            password: "password"
        }
    ) {
        user {
            id
            email
        }
    }
}
```

__Response__
```json
{
  "data": {
    "signup": {
      "user": {
        "id": "f1b234c8-8bdf-4a33-bfae-a1929c2e8ca0",
        "email": "test@example.com"
      }
    }
  }
}
```


## Login
__Request__
```
mutation {
    login (
        input: {
            email: "test@example.com",
            password: "password"
        }
    ) {
        user {
            id, email, firstName, lastName, authToken
        }
    }
}
```

__Response__

```json
{
  "data": {
    "login": {
      "user": {
        "id": "f1b234c8-8bdf-4a33-bfae-a1929c2e8ca0",
        "email": "test@example.com",
        "firstName": "Dave",
        "lastName": "",
        "authToken": "eyJhbGciO..."
      }
    }
  }
}
```


## Password Change
(requires authentication)

__Request__
```
mutation PasswordChange {
    passwordChange (
        input: {
            currentPassword: "password", newPassword:"newpassword"
        }
    ) {
        user {
            email
            firstName
            lastName
            authToken
        }
    }
}
```

__Response__

```json
{
  "data": {
    "login": {
      "user": {
        "id": "f1b234c8-8bdf-4a33-bfae-a1929c2e8ca0",
        "email": "test@example.com",
        "firstName": "Dave",
        "lastName": "",
        "authToken": "eyJhbGciO..."
      }
    }
  }
}
```


## Request Password Reset

__Request__
```
mutation RequestPasswordReset {
    passwordReset (
        input: {
            email: "test@example.com"
        }
    ) {
        message
    }
}
```

__Response__

```json
{
  "data": {
    "passwordReset": {
      "message": "Further instructions will be sent to the email if it exists"
    }
  }
}
```
