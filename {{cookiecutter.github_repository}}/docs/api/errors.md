# Errors

## Generic Errors

The `status_code` in response header complies with the standard http response headers. We expect developers to make use of them to display appropriate error dialogs.

For json requests, the API will return the error in the following format:

    {
        "_error_message": "short description of error message",
        "_error_type": "clustr.exceptions."
    }

## Validation Errors

For `POST`, `PATCH`, `PUT` & `DELETE` methods, validation error may be raised. 

It will return (Status: `400 Bad Request`). 

The response body will contain json in the format same as Generic Error above with `_error_message` key or the key will contain the name of __parameter__ that is invalid. For example, if you try to update `email` which exceeds it's max-length of 255 and `username` which contains invalid charaters. The error response body will of the format:
```
Status: 400 Bad Request
```
```
{
    "email": ["contains 300 characters, max. is 255."],
    "username": ["only alphanumberic charaters with '_', '-' and '.' without spaces is allowed.", "contains 300 characters, max. is 255."],
}
```

For displaying appropriate error message, the following algorithm can be used:

<pre>
# accepts optional "field" parameter
-> Check if status_code is => 400
-> If "_error_message" key is present in response, return it's value.
-> Check if key "field" is present in the response body
  -> Loop through all the array elements in it's value and construct the error message string.
</pre>

In pseudo-function form:

```python
def get_error_message(response_json, fields=[]):
    '''Converts json error response to a string.
    '''
    error_string = response_json.get('_error_message', None)

    if error_string:
        return error_string

    for field in fields:
        field_errors = response_json.get(field)
        if field_errors:
            for error_msg in field_errors:
                # modify as per requirement
                error_string += field + "- " + error_msg + '\n' 
    
    return error_string if error_string else ""
```

Example:
```python
data = {
 "email": "verylongemail234234234234234234234234234234234@asdasdf.com",
 "username": "verylongusernameagain_with_special_chars@%$"
}

response = requests.post('http://project.fueled.com/api', data).json
username_error_msgs = get_error_message(response, ['username'])

print username_error_msgs
# username - only alphanumberic charaters with '_', '-' and '.' without spaces is allowed.
# username - contains 300 characters, max. is 255.

all_errors = get_error_message(response, ['username', 'email'])

print all_errors
# username - contains 300 characters, max. is 255.
# username - only alphanumberic charaters with '_', '-' and '.' without spaces is allowed.
# email - contains 300 characters, max. is 255.
```
