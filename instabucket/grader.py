import csv

validator_file = 'gold.csv'


def createValidator(validator_file):
    valid_map = dict()
    with open(validator_file, 'rb') as csvfile:
        gold = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for row in gold: 
            valid_map[row['locu_id']] = row['foursquare_id']
    return valid_map

def grader(submission_file, validator):
    correct_predictions = 0.0
    total_predictions = 0.0

    with open(submission_file, 'rb') as csvfile:
        matches = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for row in matches:
            total_predictions += 1
            correct_predictions += 1 if validator[row['locu_id']] == row['foursquare_id'] else 0

    
    precision = correct_predictions / total_predictions * 100
    recall = correct_predictions / len(validator) * 100
    F1 = 2.0 * (precision * recall ) / (precision + recall)

    return (precision, recall, F1)
