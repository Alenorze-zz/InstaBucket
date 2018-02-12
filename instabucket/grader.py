import csv

class InputFormatError(Exception):
    """Exception raised for errors in the input.
    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg


validator_file = 'gold.csv'

def createValidator(validator_file):
    valid_map = dict()
    with open(validator_file, 'rb') as csvfile:
        gold = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for row in gold:
            valid_map[row['locu_id']] = row['foursquare_id']
    return valid_map

def grader_csvFile(submission_file, validator):
    correct_predictions = 0.0
    total_predictions = 0.0

    with open(submission_file, 'rb') as csvfile:
        matches = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for row in matches:
            total_predictions += 1
            correct_predictions += 1 if validator[row['locu_id']] == row['foursquare_id'] else 0

    precision = correct_predictions / total_predictions * 100
    recall = correct_predictions / len(validator) * 100
    F1 = 2.0 * (precision * recall) / (precision + recall)

    return (precision, recall, F1)

def grader_text(submission, validator):
    correct_predictions = 0.0
    total_predictions = 0.0
    rows = submission.strip().split('\n')

    if len(rows) == 0:
        raise InputFormatError('Cannot make empty submission.')


    headers = rows[0].split(',')

    if len(headers) != 2:
        raise InputFormatError('Incorrect number of fields. Only 2 fields required.')
    if headers[0].strip() != 'locu_id' or headers[1].strip() != 'foursquare_id':
        raise InputFormatError('Incorrect fields. Need "locu_id" and "foursquare_id".')
    if len(rows[1:]) == 0:
        raise InputFormatError('Empty Submission.')

    for row in rows[1:]:
        entry = row.split(',')
        locu_id = entry[0].strip()
        foursquare_id = entry[1].strip()
        total_predictions += 1
        correct_predictions += 1 if validator[locu_id] == foursquare_id else 0

    precision = correct_predictions / total_predictions * 100
    recall = correct_predictions / len(validator) * 100
    F1 = 2.0 * (precision * recall) / (precision + recall)

    return dict({
        'precision': precision,
        'recall': recall,
        'F1': F1
    })
    