def apply_semi_annual_raise(annual_salary, semi_annual_raise, months):
    if months % 6 == 0:
        # Para calcular o salario anual, considera que o aumento semestral impacta apenas metade dos salários do ano
        annual_salary = ((annual_salary / 12) * 6) + (((annual_salary / 12) * 6) * (1 + semi_annual_raise))
    return annual_salary

portion_down_payment = 0.25
current_savings = 0
annual_income = 0.04
months = 0

annual_salary = float(input("Qual seu salário?"))
semi_annual_raise = float(input("Qual o percentual de aumento salarial semestral?"))
portion_saved = float(input("Quanto do seu salário será poupado?"))
total_cost = float(input("Qual o valor do imóvel?"))

# Valor da entrada
down_payment = total_cost * portion_down_payment
first_payment = 0

# Primeiro economiza o valor para dar entrada
while first_payment < down_payment:
    # Função que aplica o aumento salarial semestral
    annual_salary = apply_semi_annual_raise(annual_salary, semi_annual_raise, months)
    months += 1
    first_payment += first_payment * (annual_income / 12) + (annual_salary / 12) * portion_saved

print(f"Em {months} meses você terá o valor de R${first_payment} para pagar a entrada de R${down_payment}.")

# Zera a variável para calcular quantos meses serão necessários para quitar o imóvel
months = 0

# Desconta o valor dado de entrada do valor total do imóvel
total_cost = total_cost - first_payment

while current_savings < total_cost:
    # Função que aplica o aumento salarial semestral
    annual_salary = apply_semi_annual_raise(annual_salary, semi_annual_raise, months)
    months += 1
    current_savings += (current_savings * annual_income / 12) + (annual_salary * portion_saved / 12)

print(f"Número de meses para quitar o financiamento do imóvel: {months}")