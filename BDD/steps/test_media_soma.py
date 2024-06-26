from behave import given, when, then

@given('eu tenho dois números: {num1:d} e {num2:d}')
def step_impl(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('eu somo os dois números e divido por 2')
def step_impl(context):
    context.result = (context.num1 + context.num2) / 2

@then('o resultado deve ser {resultado:d}')
def step_impl(context, resultado):
    assert context.result == resultado, f"O resultado foi {context.result} e deveria ser {resultado}"
