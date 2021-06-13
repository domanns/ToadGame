import pandas
import datetime

def save_score(score):
    """ take a score and save it in best scores if it's better than any on the list

    :param score: score to check and save
    :return: None
    """

    no, scores, dates = read_csv()
    today = datetime.date.today()

    i = 0
    while i<len(scores):

        if scores[i]<score:

            j = len(scores) - 2

            while j>=i:
                scores[j+1] = scores[j]
                dates[j+1] = dates[j]
                j -= 1

            scores[i] = score
            dates[i] = today
            break
        if scores[i] == score:
            break
        i += 1

    dict = {'no': no, 'scores': scores, 'dates': dates}
    data = pandas.DataFrame(dict)
    data.to_csv('best_scores.csv')


def read_csv():
    """ read "best_scores.csv" file and unpack its content to three lists

    :return: no (list), scores (list), dates (list) - lists with number of scores, scores and dates.
    """

    file = "best_scores.csv"
    content = pandas.read_csv(file)
    dict = content.to_dict()

    no = []
    scores = []
    dates = []

    for i in dict['no']:
        no.append( dict['no'][i] )
    for i in dict['scores']:
        scores.append( dict['scores'][i] )
    for i in dict['dates']:
        dates.append( dict['dates'][i] )

    return no, scores, dates



def init_csv():
    """ initialize an empty .csv file
    :return: None
    """

    no = [i+1 for i in range(3)]
    scores = [ 0 for i in range(len(no)) ]
    dates = [ 0 for i in range(len(no)) ]

    dict = {'no': no, 'scores': scores, 'dates': dates}

    data = pandas.DataFrame(dict)
    data.to_csv('best_scores.csv')


#init_csv()




