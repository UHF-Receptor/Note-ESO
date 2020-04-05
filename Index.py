import pandas as pd

ALUMNAT = { '2s2': '2s2.csv',
              '2s4': '2s2.csv',
              '4s2': '2s2.csv' }
INTERVAL = {8,6.8,5}
def get_filters():

    print('Hello! Explorem les informacions dels alumnes')
    # TO DO: get user input for class (2s2, 2s4, 4s2, 4s4)).
    classes = set(['2s2', '2s4', '4s2', '4s4'])
    classe = 'no_class'
    while classe not in classes:
        classe = input('Quin curs vols comprobar (2s2, 2s4, 4s2, 4s4)?').lower()

    print('-'*40)
    return classe.lower()
def main():
    while True:
        classe = get_filters()    Temporalment inactiu
        classe = '2s2'
        df = load_data(classe)
        print(df.loc[:,'Nom':'P4'])
        print(df[['NOM','Prob','Prob1']])
        restart = input('\nVoleu seguir investigar informació?\n').lower()
        restart = 'no'
        if restart != 'yes':
            break

if __name__ == "__main__":
	main()
