"""assertor.py is the module to assert test result"""
import test_logger as tl


#  define assertion method
def assert_response(expected_code, expected_text, code, data_field):

    print('actual code: ' + str(code))
    print('actual text: ' + data_field)
    tl.test_logger.info('actual: ' + data_field)
    if str(code) == expected_code:
        # test_row['ACTUAL_RESPONSE'] = response_text
        if data_field == expected_text:
            test_result = 'Passed'
        else:
            test_result = 'Failed'
    else:
        test_result = 'Failed'
    print(test_result)
    return test_result
