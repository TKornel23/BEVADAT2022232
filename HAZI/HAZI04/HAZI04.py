# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
from itertools import chain

# %%
# '''
# FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
# A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
# '''

# %%
# '''
# Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

# Egy példa a bemenetre: 'test_data.csv'
# Egy példa a kimenetre: df_data
# return type: pandas.core.frame.DataFrame
# függvény neve: csv_to_df
# '''

# %%
def csv_to_df(path):
    df = pd.read_csv(path)
    return df

# %%
# '''
# Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
# és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

# Egy példa a bemenetre: df_data
# Egy példa a kimenetre: df_data_capitalized
# return type: pandas.core.frame.DataFrame
# függvény neve: capitalize_columns
# '''

# %%
def capitalize_columns(df_data):
    new_df = df_data.copy()
    new_df.columns = map(lambda x: x.upper() if 'e' in x else x, new_df.columns)
    return new_df


# %%
# '''
# Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
# (legyen az átmenő ponthatár 50).

# Egy példa a bemenetre: df_data
# Egy példa a kimenetre: 5
# return type: int
# függvény neve: math_passed_count
# '''

# %%

def math_passed_count(df_data):
    new_df = df_data.copy()
    return len(new_df[new_df['math score'] > 50])

# %%
# '''
# Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

# Egy példa a bemenetre: df_data
# Egy példa a kimenetre: df_did_pre_course
# return type: pandas.core.frame.DataFrame
# függvény neve: did_pre_course
# '''

# %%
def did_pre_course(df_data):
    new_df = df_data.copy()
    df_did_pre_course = new_df[new_df['test preparation course'] == 'completed']
    return df_did_pre_course

# %%
# '''
# Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
# majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

# Egy példa a bemenetre: df_data
# Egy példa a kimenetre: df_average_scores
# return type: pandas.core.frame.DataFrame
# függvény neve: average_scores
# '''

# %%

def average_scores(df_data):
    new_df = df_data.copy()
    return new_df.groupby(by='parental level of education').mean()
# %%
# '''
# Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
# A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

# Egy példa a bemenetre: df_data
# Egy példa a kimenetre: df_data_with_age
# return type: pandas.core.frame.DataFrame
# függvény neve: add_age
# '''

# %%
def add_age(df_data):
    new_df = df_data.copy()
    random.seed(42)
    new_df['age'] = random.randint(18, 67)
    return new_df


# %%

# %%
# '''
# Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

# Egy példa a bemenetre: df_data
# Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
# return type: tuple
# függvény neve: female_top_score
# '''

# %%
def female_top_score(df_data):
    new_df = df_data.copy()
    columns = ['math score','reading score', 'writing score']
    new_df['total score'] = new_df[columns].sum(axis=1)
    res = new_df[new_df['gender'] == 'female'].nlargest(1, 'total score', keep='first')
    tup = tuple(chain.from_iterable(res[columns].values))
    return tup

# %%
# '''
# Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
# Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

# 90-100%: A
# 80-90%: B
# 70-80%: C
# 60-70%: D
# <60%: F

# Egy példa a bemenetre: df_data
# Egy példa a kimenetre: df_data_with_grade
# return type: pandas.core.frame.DataFrame
# függvény neve: add_grade
# '''
def add_grades(df):
    new_df = df.copy()
    new_df['percentage'] = (new_df['math score'] + new_df['reading score'] + new_df['writing score']) / 300
    
   
    def get_grade(score):
        if score >= 0.9:
            return 'A'
        elif score >= 0.8:
            return 'B'
        elif score >= 0.7:
            return 'C'
        elif score >= 0.6:
            return 'D'
        else:
            return 'F'
        
    new_df['grade'] = new_df['percentage'].apply(get_grade)

    return new_df
# %%

# %%
# '''
# Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
# ami vizualizálja a nemek által elért átlagos matek pontszámot.

# Oszlopdiagram címe legyen: 'Average Math Score by Gender'
# Az x tengely címe legyen: 'Gender'
# Az y tengely címe legyen: 'Math Score'

# Egy példa a bemenetre: df_data
# Egy példa a kimenetre: fig
# return type: matplotlib.figure.Figure
# függvény neve: math_bar_plot
# '''

# %%
def math_bar_plot(df):
    avg_math_by_gender = df.groupby('gender')['math score'].mean()

    fig, axes = plt.subplots(ncols=1, nrows=1, figsize=(10,10))
    axes.bar(avg_math_by_gender.index, avg_math_by_gender.values)

    axes.set_title('Average Math Score by Gender')
    axes.set_xlabel('Gender')
    axes.set_ylabel('Math Score')

    return fig
# %%
# ''' 
# Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
# ami vizualizálja az elért írásbeli pontszámokat.

# A histogram címe legyen: 'Distribution of Writing Scores'
# Az x tengely címe legyen: 'Writing Score'
# Az y tengely címe legyen: 'Number of Students'

# Egy példa a bemenetre: df_data
# Egy példa a kimenetre: fig
# return type: matplotlib.figure.Figure
# függvény neve: writing_hist
# '''

# %%
def writing_hist(df):

    fig, axes = plt.subplots(ncols=1, nrows=1, figsize=(10,10))
    axes.hist(df['writing score'], bins=10)
    

    axes.set_title('Distribution of Writing Scores')
    axes.set_xlabel('Writing Score')
    axes.set_ylabel('Number of Students')

    return fig

# %%
# ''' 
# Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
# ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

# Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
# Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
# A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

# Egy példa a bemenetre: df_data
# Egy példa a kimenetre: fig
# return type: matplotlib.figure.Figure
# függvény neve: ethnicity_pie_chart
# '''

# %%
def ethnicity_pie_chart(df):

    student_count = df['race/ethnicity'].value_counts()
    fig, axes = plt.subplots(ncols=1, nrows=1, figsize=(10,10))

    axes.pie(student_count, labels=student_count.index, autopct='%1.1f%%')

    axes.set_title('Proportion of Students by Race/Ethnicity')
    axes.legend(student_count.index, loc='best')
    
    return fig

df = csv_to_df("C:\\Users\\tkorn\\Downloads\\StudentsPerformance.csv")
ethnicity_pie_chart(df)