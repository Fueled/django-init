## Current User
(requires authentication)

__Request__
```
query {
    me {
        id
        firstName
        lastName
        email
    }
}
```

__Response__

```json
{
  "data": {
    "me": {
      "id": "629b1e03-53f0-43ef-9a03-17164cf782ac",
      "first_name": "John",
      "last_name": "Hawley",
      "email": "john@localhost.com"
    }
  }
}
```


## All Users
(requires authentication and superuser privilege)

__Request__
```
query {
    users {
        id
        firstName
        lastName
        email
    }
}
```

__Response__

```json
{
  "data": {
    "users": [
      {
        "id": "c3fd5929-65c0-4971-8323-083435cf8bba",
        "firstName": "first name",
        "lastName": "last name",
        "email": "suneet@xyz.com"
      },
      {
        "id": "765217a8-7599-4e25-9c24-b7c92e878201",
        "firstName": "fueled",
        "lastName": "user",
        "email": "user@fueled.com"
      }
    ]
  }
}
```
