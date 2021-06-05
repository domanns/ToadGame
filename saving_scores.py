import pandas
import datetime
from pandas import DataFrame

def save_score(score):

    dict = read_csv()

    today = datetime.date.today()

    i = 0
    while i < len(dict['no']):

        if dict['scores'][i] < score:

            if i < len( dict['no']) - 1 :      # are we NOT on the last score?

                if dict['scores'][i + 1] == 0:

                    # If the next score is equal 0 push the currently checked score to the next one and overwrite the current score
                    dict['scores'][i+1] = dict['scores'][i]
                    dict['dates'][i+1] = dict['dates'][i]
                    dict['scores'][i] = score
                    dict['dates'][i] = today


                elif i < len(dict['no']) - 2:       # are we NOT on the one-before-last score?

                    dict['scores'][i + 2] = dict['scores'][i + 1]
                    dict['dates'][i + 2] = dict['dates'][i + 1]

                    dict['scores'][i + 1] = dict['scores'][i]
                    dict['dates'][i + 1] = dict['dates'][i]

                    dict['scores'][i] = score
                    dict['dates'][i] = today

            elif i == len(dict['no'])-1:

                dict['scores'][i] = score
                dict['dates'][i] = today

            break

        elif dict['scores'][i] == score:

            if dict['scores'][0] == dict['scores'][1] and dict['scores'][1] == dict['scores'][2]:
                dict['scores'][0] = score
                dict['dates'][0] = today
                dict['scores'][0] = 0
                dict['dates'][0] = 0

            if dict['scores'][1] == dict['scores'][2] and dict['scores'][0] != dict['scores'][1]:
                dict['scores'][1] = score
                dict['dates'][1] = today
                dict['scores'][2] = 0
                dict['dates'][2] = 0
            i += 1
        else:
            i += 1

    data = pandas.DataFrame(dict)
    data.to_csv('best_scores.csv')


    return dict


def read_csv():

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

    dict = {'no': no, 'scores': scores, 'dates': dates}

    return dict



def init_csv():

    no = [i+1 for i in range(3)]
    scores = [ 0 for i in range(len(no)) ]
    dates = [ 0 for i in range(len(no)) ]

    dict = {'no': no, 'scores': scores, 'dates': dates}

    data = pandas.DataFrame(dict)
    data.to_csv('best_scores.csv')


#init_csv()


