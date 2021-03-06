"""run_api_test.py is the controller and entry point for kicking off test execution"""
import csv
import os
import test_logger as tl
from test_config import TEST_OUTPUT_PATH, REST_URL, TEST_INPUT_DATA, TEST_RESULT_CSV
from requester import send_payload
from assertor import assert_response


#  setup test run timestamp and output dir
tl.test_logger.info('API endpoint POST test started...')
if not os.path.exists(TEST_OUTPUT_PATH):
    os.makedirs(TEST_OUTPUT_PATH)
   
#  loading the test input data and loop through all the test data rows to execution each test case
try:
    with open(TEST_INPUT_DATA) as input_data:
        with open(TEST_RESULT_CSV, 'w') as output_result:
            test_list = csv.DictReader(input_data)
            if not test_list:
                print('list is empty')
            csv_header = test_list.fieldnames
            csv_writer = csv.DictWriter(output_result, csv_header)
            csv_writer.writeheader()
            for test_row in test_list:
                test_flag = test_row['TEST_FLAG'].upper()
                test_id = test_row['TEST_CASE_ID']
                if test_flag == 'Y':
                    tl.test_logger.info('Executing test case: ' + test_id)
                    payload = test_row['PAYLOAD'].strip()
                    payload = payload.replace('|', ',')
                    print('payload to post: >>>> ' + payload)
                    expect_response_code = test_row['EXPECTED_RESPONSE_CODE'].strip()
                    print('Expect test response code: ' + expect_response_code)
                    # send POST request
                    expect_response = test_row['EXPECTED_RESPONSE_TEXT'].replace('"', '').split(':')
                    expect_response_text = expect_response[1].strip()
                    print('Expect test response text: ' + expect_response_text)
                    rest_response = send_payload(REST_URL, payload)
                    response_code = rest_response[0]
                    data_set = rest_response[1]
                    field_value = data_set[expect_response[0]]
                    test_row['ACTUAL_RESPONSE'] = field_value
                    test_row['ACTUAL_RESPONSE_CODE'] = response_code
                    # calling assert test
                    test_result = assert_response(expect_response_code, expect_response_text, response_code, field_value)
                    tl.test_logger.info('Test case: ' + test_id + ' ' + test_result)
                    test_row['TEST_RESULT'] = test_result  # update cell with test result
                    test_row['PAYLOAD'] = payload.replace('"', '')
                    test_row['EXPECTED_RESPONSE_TEXT'] = expect_response_text
                    csv_writer.writerow(test_row)  # write to output csv
                else:
                    tl.test_logger.info('Skipping test case ' + test_id)
except Exception:
    print('Test did NOT run as there is an Exception, check log for details!!!!')
    tl.test_logger.exception('Fail to start test execution as:')



