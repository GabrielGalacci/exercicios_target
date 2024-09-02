import json

with open('revenue.json', 'r') as file:
    data = json.load(file)

revenues = [entry['revenue'] for entry in data['daily_revenue']
            if entry['revenue'] != 0.00]

sum_of_revenues = 0
for revenue in revenues:
    sum_of_revenues += revenue
med_revenues = sum_of_revenues / len(revenues)

days_sup_med_revenue = 0
for revenue in revenues:
    if revenue > med_revenues:
        days_sup_med_revenue += 1

print(f'O menor valor de faturamento foi: {min(revenues)}')
print(f'O maior valor de faturamento foi: {max(revenues)}')
print(f'A média de faturamento foi: {med_revenues:.2f}')
print(f'A quantidade de dias que foram superior a média foi: '
      f'{days_sup_med_revenue}')
