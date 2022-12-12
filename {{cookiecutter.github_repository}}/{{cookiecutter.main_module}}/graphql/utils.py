import graphene
from graphene import relay
from graphql.error import GraphQLError
from django.core.exceptions import ValidationError


class CountableConnectionBase(relay.Connection):
    """
        Extend connection class to display
        total count and edges count in paginated results
    """
    class Meta:
        abstract = True

    total_count = graphene.Int()
    edge_count = graphene.Int()

    @classmethod
    def resolve_total_count(cls, root, info, **kwargs):
        return root.length

    @classmethod
    def resolve_edge_count(cls, root, info, **kwargs):
        return len(root.edges)


def validate_one_of_args_is_in_query(*args):
    # split args into a list with 2-element tuples:
    # [(arg1_name, arg1_value), (arg2_name, arg2_value), ...]
    splitted_args = [args[i : i + 2] for i in range(0, len(args), 2)]  # noqa: E203
    # filter trueish values from each tuple
    filter_args = list(filter(lambda item: bool(item[1]) is True, splitted_args))

    if len(filter_args) > 1:
        rest_args = ", ".join([f"'{item[0]}'" for item in filter_args[1:]])
        raise GraphQLError(
            f"Argument '{filter_args[0][0]}' cannot be combined with {rest_args}"
        )

    if not filter_args:
        required_args = ", ".join([f"'{item[0]}'" for item in splitted_args])
        raise GraphQLError(f"At least one of arguments is required: {required_args}.")


def validate_one_of_args_is_in_mutation(error_class, *args):
    try:
        validate_one_of_args_is_in_query(*args)
    except GraphQLError as e:
        raise ValidationError(str(e), code=error_class.GRAPHQL_ERROR)
