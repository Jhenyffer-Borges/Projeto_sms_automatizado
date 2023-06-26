import pandas as pd
from twilio.rest import Client

account_sid = "account twilio"
auth_token = "token gerado no twilio"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'Arquivos/{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor=tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes} alguem bateu a meta. Vendedor: {vendedor}, vendas: {vendas}')

message = client.messages.create(
    to='numero de celular',
    from_='numero gerado no twilio',
    body= f'No mes de {mes} alguem bateu a meta. Vendedor: {vendedor}, vendas: {vendas}')

print(message.sid)






