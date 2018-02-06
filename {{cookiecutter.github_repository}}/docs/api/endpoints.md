For api overview and usages, check out [this page](overview.md).

[TOC]

# Authentication

## Login

```
POST /api/auth/login
```

**Example**
```json
{
    "email": "hello@example.com",
    "password": "VerySafePassword0909"
}
```
**Example**

## Register

```
POST /api/auth/register
```

**Example**
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "hello@example.com",
    "password": "VerySafePassword0909"
}
```


## Change password

```
POST /api/auth/change-password (requires authentication)
```

**Example**
```json
{
    "current_password": "NotSoSafePassword",
    "new_password": "VerySafePassword0909"
}
```

**Response**
```
Status: 204 No-Content
```


## Request password for reset

Send an email to user if the email exist.

```
POST /api/auth/password-reset
```

**Parameters**

Name  | Description
------|-------------------------------------
email | (required) valid email of an existing user.

**Example**
```json
{
    "email": "hello@example.com"
}
```

**Response**
```
Status: 200 Ok
```
