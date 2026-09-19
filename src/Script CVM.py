# Brazilian Securities and Exchange Commission (CVM) Dataset
# Source: https://dados.cvm.gov.br/dataset/cia_aberta-doc-dfp
# Analysis of annual variation in sales and profits of public companies

#%% Loading packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#%% Importing databases
# The files have a specific encoding, we will adjust it during import
cvm_data = pd.read_csv('data/CVM Result.csv',
                       sep=';',
                       encoding='latin1')

registration_data = pd.read_csv('data/CVM registration data.csv',
                                sep=';',
                                encoding='latin1')

#%% Unique account records
accounts = cvm_data['DS_CONTA'].unique()
print(accounts)

#%% Filter observations of interest
# See the CD_CONTA column in the cvm_data dataset
# CD_CONTA is the code for each DS_CONTA 
#                               DS_CONTA represents: "account description"
# CD_CONTA= 3.01 are types of REVENUE
# CD_CONTA= 3.11 are types of PROFIT AND/OR LOSS
selected_data = cvm_data.query(' CD_CONTA=="3.01" | CD_CONTA=="3.11" ')

#%% Date variable adjustment (currently as text)
year_data = pd.to_datetime(selected_data['DT_FIM_EXERC']).dt.year #*
selected_data.insert(5, 'YEAR', year_data) #*  .insert(position, 'NEW_column_name', values)
selected_data.info()

#%% Organizing observations
# We have information from 2021 and 2022, let's keep them together for each company
# We will separate revenue and profit accounts
# CD_CVM represents: "Company identification code"
selected_data = selected_data.sort_values(by=['CD_CONTA','CD_CVM'], ascending=True)
# Shows all types of revenue for all companies, then shows all types of profit/loss

#%% Observation duplication analysis
duplicates_count = selected_data.groupby(['CD_CVM','CD_CONTA'])['VL_CONTA'].count()
# There is a residue in the dataset, company CD_CVM=26077 has duplicates

#%% Residue exclusion
# There are report versions
# We will keep only the latest available version (VERSAO = 3), note: there are only versions 1 and 3
selected_data.query('~(CD_CVM==26077 & VERSAO==1)', inplace=True) # The change is made in selected_data and nothing is returned

#%% Now let's use the "registration_data" dataset
# We will add the company sectors to perform specific analyses
# The registration_data dataset has the columns CD_CVM and SETOR_ATIV
registration_subset = registration_data[['CD_CVM','SETOR_ATIV']].copy()
# ** new_table = original_table.loc[row_condition, ['column1', 'column2']].copy()

# Eliminate missings
registration_subset = registration_subset[registration_subset['SETOR_ATIV'].notnull()]
# We will keep only unique records, avoiding duplication in the merge
registration_subset.drop_duplicates(inplace=True)

# Performing the merge
selected_data = pd.merge(selected_data, registration_subset, how='left', on='CD_CVM')

#%% Cleaning: let's select only the variables of interest
selected_data = selected_data[['CD_CVM','DENOM_CIA','SETOR_ATIV','CD_CONTA','YEAR','VL_CONTA']]
# Already repositioning in the desired order

#%% To make the information easier to read, let's replace the labels *
labels = {'3.01':'Revenue', '3.11':'Result'}
selected_data = selected_data.assign(CD_CONTA=selected_data.CD_CONTA.map(labels))#*

#%% Percentage variation calculation
# CREATING a variable with the lagged value, this variable will be called 'LAG_VALUE' *
selected_data['LAG_VALUE'] = selected_data.groupby(['CD_CVM','CD_CONTA'])['VL_CONTA'].shift(1)

# CREATING a variable with the variation result
selected_data['VARIATION'] = ((selected_data['VL_CONTA']-selected_data['LAG_VALUE'])/selected_data['LAG_VALUE'])

# Rounding
selected_data['VARIATION'] = round(selected_data['VARIATION'], 3) #*

#%% Descriptive statistics of the VARIATION
# There are very extreme values that influence the descriptives
# Observation cleaning *
selected_data = selected_data[~selected_data['VARIATION'].isin([np.nan, np.inf, -np.inf])]
# Descriptive statistics table of the VARIATION
selected_data['VARIATION'].describe()

#%% Exclusion of large variations
# Example: let's exclude variations greater than 200% and less than -200%
# They are indications of significant variations in the company's fundamentals
selected_data = selected_data[selected_data['VARIATION'].between(-2, 2, inclusive='both')]

#%% New descriptive statistics
selected_data['VARIATION'].describe()

#%% More detailed information by account type (revenue and result)
selected_data.groupby(['CD_CONTA'])['VARIATION'].describe().T

#%% Detailing by sector
# By sector
sector_summary = selected_data.groupby(['CD_CONTA','SETOR_ATIV']).agg({'VARIATION':'mean'})
sector_summary = sector_summary.reset_index()

# Sectoral numbers indicate that there are more specific analyses to do
# For example, some sectors may have few observations (biased mean)

# Count of information by sector
# Chosen criterion: let's keep only sectors with at least 6 observations
sector_count = selected_data[['SETOR_ATIV', 'VARIATION']].groupby('SETOR_ATIV').count()

selected_sector_count = (sector_count
                     .query('VARIATION >= 6')
                     .rename(columns={'VARIATION':'COUNT'})).reset_index()

# Database adjustment
sector_summary = (sector_summary
.merge(selected_sector_count, how='left', on='SETOR_ATIV')
.query('~COUNT.isna()'))

#-------------------Teste 1

# Visualização gráfica
plt.figure(figsize=(18,12), dpi=600)
sns.barplot(data=sector_summary, y='SETOR_ATIV', x='VARIATION', hue='CD_CONTA')

# 1. Guarda o gráfico em ficheiro na raiz do projeto
image_path = 'cvm_sector_analysis.png'
plt.savefig(image_path, bbox_inches='tight', dpi=300)

# 2. Tenta abrir a imagem automaticamente no ecrã
import os, platform

try:
    if 'microsoft' in platform.release().lower():  # WSL (Windows)
        os.system(f'cmd.exe /c start {image_path} 2>/dev/null')
    elif platform.system() == 'Windows':
        os.system(f'start {image_path}')
    elif platform.system() == 'Darwin':  # macOS
        os.system(f'open {image_path}')
    else:
        plt.show()  # Linux nativo com GUI
except Exception:
    plt.show()

# %% END