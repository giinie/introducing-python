def find_factorial(number):
    """
    Calculate the factorial of a given number.

    Parameters:
    number (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the given number.
    """
    if number == 0:
        return 1
    return number * find_factorial(number - 1)


def bubble_sort(arr):
    """
    버블 정렬 알고리즘을 사용하여 주어진 배열을 오름차순으로 정렬합니다.

    Parameters:
        arr (list): 정렬할 대상 리스트

    Returns:
        list: 오름차순으로 정렬된 리스트
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    """
    주어진 배열을 퀵 정렬 알고리즘을 사용하여 정렬합니다.

    Parameters:
    arr (list): 정렬할 요소가 들어 있는 리스트

    Returns:
    list: 정렬된 요소가 들어 있는 리스트
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


import re


def validate_email(email):
    """
    주어진 이메일 주소가 표준 형식을 따르는지 검증합니다.

    Parameters:
    email (str): 검증할 이메일 주소

    Returns:
    bool: 이메일 주소가 표준 형식을 따르면 True, 그렇지 않으면 False
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def tip_calculator(bill_amount, tip_percentage):
    if not isinstance(bill_amount, (int, float)) or not isinstance(tip_percentage, (int, float)):
        raise TypeError("Both bill amount and tip percentage must be numbers.")
    if bill_amount < 0 or tip_percentage < 0:
        raise ValueError("Bill amount and tip percentage must not be negative.")
    tip_amount = bill_amount * (tip_percentage / 100)
    total_amount = bill_amount + tip_amount
    return total_amount


def test_tip_calculator():
    # 일반적인 경우
    print("Testing general cases...")
    assert tip_calculator(100, 20) == 120, "Test case 1 failed"
    assert tip_calculator(50, 10) == 55, "Test case 2 failed"
    assert tip_calculator(200, 15) == 230, "Test case 3 failed"
    print("General cases passed")

    # 예외적인 경우
    print("Testing edge cases...")
    try:
        tip_calculator(-100, 20)
    except ValueError:
        print("Test case 4 passed")
    else:
        print("Test case 4 failed")

    try:
        tip_calculator(100, -20)
    except ValueError:
        print("Test case 5 passed")
    else:
        print("Test case 5 failed")

    try:
        tip_calculator(0, 20)
    except ValueError:
        print("Test case 6 failed")
    else:
        print("Test case 6 passed")

    print("Edge cases completed")

    # 잘못된 입력 확인
    print("Testing bad inputs...")
    try:
        tip_calculator('100', 20)
    except TypeError:
        print("Test case 7 passed")
    else:
        print("Test case 7 failed")

    try:
        tip_calculator(100, '20')
    except TypeError:
        print("Test case 8 passed")
    else:
        print("Test case 8 failed")

    print("Bad input cases completed")


# 단위 테스트 실행
test_tip_calculator()
