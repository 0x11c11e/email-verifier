from verify_email import verify_email
import pandas as pd
import csv


df = pd.read_csv('not_verified_email.csv')
df = df.dropna(subset=['email'])
df_verified_email = pd.DataFrame(columns=['name', 'email'])

with open('verified_email.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'email'])
    for name, email in df.values:
        if verify_email(email):
                writer.writerow([name, email])

