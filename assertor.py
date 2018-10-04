"""assertor.py is the module to assert test result"""
import test_logger as tl


#  define assertion method
def assert_response(expected_code, expected_text, actual):
    response_code = str(actual[0])
    response_text = str(actual[1])
    print('actual code: ' + response_code)
    print('actual text: ' + response_text)
    tl.test_logger.info('actual: ' + response_text)
    if response_code == expected_code:
        # test_row['ACTUAL_RESPONSE'] = response_text
        if response_text == expected_text:
            test_result = 'Passed'
        else:
            test_result = 'Failed'
    else:
        test_result = 'Failed'
    print(test_result)
    return test_result
