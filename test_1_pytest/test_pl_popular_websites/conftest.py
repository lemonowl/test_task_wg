
def pytest_assertrepr_compare(op, left, right):
    """Переопределение вывода ошибки
    """
    if isinstance(left, list) and isinstance(right, list) and op == "==":
        error = ["В таблице не должно быть строк со значением меньше ожидаемого. Строки с ошибками:"]
        error.extend(left)
        return error
