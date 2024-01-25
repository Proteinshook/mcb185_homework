# 24accuracy.py by Ethan Djou Co-authored Khalid Saif


def accur(tp, fp, tn, fn):
	if (tp + fp + tn + fn) != 0:  accuracy = (tp + tn)/ (tp + fp + tn + fn)
	else:                         return 'undefined value in accuracy'                                            
	if(tp + fp) != 0:             precision = tp / (tp + fp)
	else:                         return 'undefined value in percision'
	if (tp + fn) != 0:            recall = tp / (tp + fn)
	else:                         return 'undefined value in recall'
	if (precision + recall) != 0: f1_score = 2 * (precision * recall) / (precision + recall)
	else:                         return 'undefined value in f1 score'
	return accuracy, f1_score

# Testing the formula
print(accur(2, 55, 35, 62))
print(accur(13, 89, 87, 2))
print(accur(5, 33, 78, 99))
