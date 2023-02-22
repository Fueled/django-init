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
      "id": "Q3VycmVudFVzZXI6M2MzYjVhMmUtMWM0MC00MTQzLTk1N2ItYjVlYTAzOWU0NzVi",
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
        totalCount,
        edgeCount, 
        edges {
            node {
                id,
                firstName,
                lastName
            }
        }
    }
}
```

__Response__

```json
{
    "data": {
        "users": {
            "totalCount": 2,
            "edgeCount": 2,
            "edges": [
                {
                    "node": {
                        "id": "VXNlckNvbm5lY3Rpb246M2MzYjVhMmUtMWM0MC00MTQzLTk1N2ItYjVlYTAzOWU0NzVi",
                        "firstName": "first name",
                        "lastName": "last name"
                    }
                },
                {
                    "node": {
                        "id": "VXNlckNvbm5lY3Rpb246ZjU4N2IyY2EtNThmMS00NTE3LTgyMTEtYzczODA3YTI1ZTU1",
                        "firstName": "fueled",
                        "lastName": "user"
                    }
                }
            ]
        }
    }
}
```
