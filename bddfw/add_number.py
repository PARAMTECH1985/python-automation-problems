from behave import *
from calculator import add


@given('Calculator app is run')
def step_impl(context):
    print('Step: Given Calculator app is run')


@when('I input "{num1}" and "{num2}" to calculator')
def step_impl(context, num1, num2):
    context.num1 = int(num1)
    context.num2 = int(num2)


@then('I get result "{expected_result}"')
def step_impl(context, expected_result):
    result = add(context.num1, context.num2)
    assert str(result) == expected_result
