This describes the resources that make up the official {{ cookiecutter.project_name }} API v1.

## Authentication

For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal `Bearer`, with whitespace separating the two strings. For example:

```
Authorization: Bearer 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
Unauthenticated responses that are denied permission will result in an `HTTP 401 Unauthorized` response.

An example request:
```bash
curl -X GET http://127.0.0.1:8000/api/example/ -H `Authorization: Bearer 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`
```

## Current Version

By default, all requests receive the `1.0` version of the API. We encourage you to explicitly request this version via the Accept header.

```
Accept: application/vnd.{{ cookiecutter.main_module|replace('_', '')|replace('-', '') }}+json; version=1.0
```

__Important:__ The default version of the API may change in the future. If you're building an application and care about the stability of the API, be sure to request a specific version in the `Accept` header as shown in the examples below.

```
GET /bookings/ HTTP/1.1
Host: example.com
Accept: application/vnd.{{ cookiecutter.main_module|replace('_', '')|replace('-', '') }}+json; version=1.0
```


## Schema

All timestamps are returned in ISO 8601 format:

`YYYY-MM-DDTHH:MM:SSZ`


## HTTP Verbs

Where possible, API v1 strives to use appropriate HTTP verbs for each action.

Verb    | Description
------- | -------------
HEAD    |  Can be issued against any resource to get just the HTTP header info.
GET     | Used for retrieving resources.
POST    |  Used for creating resources, or performing custom actions (such as merging a pull request).
PATCH   | Used for updating resources with partial JSON data. For instance, an Issue resource has title and body attributes. A PATCH request may accept one or more of the attributes to update the resource. PATCH is a relatively new and uncommon HTTP verb, so resource endpoints also accept POST requests.
PUT     | Used for replacing resources or collections. For PUT requests with no body attribute, be sure to set the Content-Length header to zero.
DELETE  | Used for deleting resources.

## Pagination
{%- if cookiecutter.use_cursor_pagination.lower() == 'y' %}

Requests that return multiple items will be paginated to 30 items by default. You can specify cursor for the item with the `?cursor` parameter. For some resources, you can also set a custom page size up to 1000 with the `?per_page` parameter.

Note that offset is 1-based and that omitting the `?cursor` parameter will return results from offset 1.

By Default, the results are ordered in descending order of creation time based on field `-created_at` and it does not return `count` as part of the response.
{%- else %}

Requests that return multiple items will be paginated to 30 items by default. You can specify offset for the item with the `?offset` parameter. For some resources, you can also set a custom page size up to 1000 with the `?per_page` parameter.

Note that offset is 1-based and that omitting the `?offset` parameter will return results from offset 1.
{%- endif %}

## Rate Limit

All the unauthorized urls have a rate limit of 10,000 requests/day/IP. After exceeding the limit, you'll get `HTTP TOO MANY REQUESTS` with status code `429`. When this happens you'll also receive `X-Throttle-Wait-Seconds: <time_in_sec>` header in response header.
