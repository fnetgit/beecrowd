# Idade em Dias

total_days = int(input())
year = total_days // 365
remaining_days = total_days % 365
month = remaining_days // 30
days = remaining_days % 30
print(year,month,days)
