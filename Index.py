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

def assoliments(df):
    # if a mark is not there, fills no marks with a 0
    df['E1-C']=df['E1-C'].fillna(0)
    df['E2-C']=df['E2-C'].fillna(0)
    df['E3-C']=df['E3-C'].fillna(0)
    df['E4-C']=df['E4-C'].fillna(0)
    # make a mean
    df['Prob']=(df['E1-P']+df['E2-P']+df['E3-P']+df['E4-P'])/4+1
    df['Raon']=(df['E1-R']+df['E2-R']+df['E3-R']+df['E4-R'])/4+1
    df['Conn']=(df['E1-C']+df['E2-C']+df['E3-C']+df['E4-C'])/4+1
    df['Repre']=(df['E1-I']+df['E2-I']+df['E3-I']+df['E4-I'])/4+1
    #put it in NA, AS, AN and AE
    df['Prob1'] = df['Prob'].apply(lambda x: 'AE' if x >= 3.5 else 'AN' if x >=2.5 else 'AS' if x>=1.75 else 'NA' )
    df['Raon1'] = df['Raon'].apply(lambda x: 'AE' if x >= 3.5 else 'AN' if x >=2.5 else 'AS' if x>=1.75 else 'NA' )
    df['Conn1'] = df['Conn'].apply(lambda x: 'AE' if x >= 3.5 else 'AN' if x >=2.5 else 'AS' if x>=1.75 else 'NA' )
    df['Repre1'] = df['Repre'].apply(lambda x: 'AE' if x >= 3.5 else 'AN' if x >=2.5 else 'AS' if x>=1.75 else 'NA' )
    return


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
