This describes the resources that make up the official {{ cookiecutter.project_name }} API v1.

[TOC]

## Current Version

By default, all requests receive the `1.0` version of the API. We encourage you to explicitly request this version via the Accept header.

```
Accept: application/json; version=1.0
```

__Important:__ The default version of the API may change in the future. If you're building an application and care about the stability of the API, be sure to request a specific version in the `Accept` header as shown in the examples below.

```
GET /bookings/ HTTP/1.1
Host: example.com
Accept: application/json; version=1.0
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

Requests that return multiple items will be paginated to 30 items by default. You can specify further pages with the `?page` parameter. For some resources, you can also set a custom page size up to 1000 with the `?per_page` parameter.

Note that page numbering is 1-based and that omitting the `?page` parameter will return the first page.


## Authorization

TODO
