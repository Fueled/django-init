# Errors

## Generic Errors

The `status_code` in response header complies with the standard http response headers. We expect developers to make use of them to display appropriate error dialogs.

For json requests, the API will return the error in the following format:

```json
{
  "error_type": "WrongArguments",
  "errors": [
    {
      "message": "Unable to login with provided credentials."
    }
  ]
}
```

## Validation Errors

For `POST`, `PATCH`, `PUT` & `DELETE` methods, validation error may be raised. 

It will return (Status: `400 Bad Request`). 

The response body will contain json in the format same as Generic Error with `field` key. For example, if you try to register with `email` which already exists. The error response body will be of the format:

```json
{
  "error_type": "ValidationError",
  "errors": [
    {
      "field": "email",
      "message": "User with this email address already exists."
    },
    {
      "field": "email",
      "message": "Some other error related to email."
    }
  ]
}
```

For nested errors:

The response body will contain json in the format same as Validation error with `errors` as key. For example:

```json
{
  "error_type": "ValidationError",
  "errors": [
    {
      "field": "profile",
      "message": null,
      "errors": [
        {
          "field": "email",
          "message": "User with this email address already exists."
        },
        {
          "field": "custom_data",
          "message": null,
          "errors": [
            {
              "field": "age",
              "message": "Person too young. Age should be more than 18 years."
            }
          ]
        }
      ]
    }
  ]
}
```

__NOTE__: The copy for most of these error messages can be changed by backend developers.
