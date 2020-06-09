import math
import sys
import argparse
# Add optional parameters to the console
parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, choices=['annuity', 'diff'], help='annuity or diff')
parser.add_argument('--payment', type=int, help='this is a static monthly payment')
parser.add_argument('--principal', type=int, help='this is the main complete payment')
parser.add_argument('--periods', type=int, help='the number of periods')
parser.add_argument('--interest', type=float, help='the interest rate')
args = parser.parse_args()


# Functions to calculate diverse options
def calculate_count_of_months(credit_principal, monthly_payment, credit_interest):
    i = credit_interest / (12 * 100)
    n = math.ceil(math.log((monthly_payment / (monthly_payment - i * credit_principal)), 1 + i))
    years_with_month = n / 12
    years = math.floor(years_with_month)
    months = math.ceil(n % 12)
    if months == 0:
        print(f'You need {years} years to repay this credit!')
    else:
        print(f'You need {years} years and {months} months to repay this credit!')
    overpayment = (n * monthly_payment) - credit_principal
    print_overpayment(overpayment)


def calculate_annuity_monthly_payment(credit_principal, count_periods, credit_interest):
    i = credit_interest / (12 * 100)
    a = math.ceil(credit_principal * ((i * math.pow(1+i, count_periods)) / (math.pow(1 + i, count_periods) - 1)))
    print(f'Your annuity payment = {a}!')
    overpayment = (a * count_periods) - credit_principal
    print_overpayment(overpayment)


def calculate_credit_principal(monthly_payment, count_periods, credit_interest):
    i = credit_interest / (12 * 100)
    a = monthly_payment
    p = round(a / ((i * math.pow(1 + i, count_periods)) / (math.pow(1 + i, count_periods) - 1)))
    print(f'Your credit principal = {p}!')
    overpayment = (monthly_payment * count_periods) - p
    print_overpayment(overpayment)


def print_differentiated_payment(list_payments):
    print(list_payments)
    for index, payment in enumerate(list_payments):
        print(f'Month {index + 1}: paid out {payment}')
    print()


def print_overpayment(overpayment):
    print(f'Overpayment = {overpayment}')


def calculate_differentiated_payment(credit_principal, count_periods, credit_interest):
    i = credit_interest / (12 * 100)
    monthly_payments = []
    for m in range(1, count_periods + 1):
        payment = credit_principal / count_periods + i * (credit_principal - (credit_principal * (m - 1) / count_periods))
        monthly_payments.append(math.ceil(payment))
    total_payment = sum(monthly_payments)
    overpayment = total_payment - credit_principal
    print_differentiated_payment(monthly_payments)
    print_overpayment(overpayment)


# Helper constrains
inadequate_length = len(sys.argv) < 5
negative_parameters = (args.payment and args.payment < 0) or (args.principal and int(args.principal) < 0) \
                                       or (args.periods and int(args.periods) < 0) \
                                       or (args.interest and float(args.interest) < 0)
undefined_type = args.type is False and args.type != 'annuity' and args.type != 'diff'
wrong_diff_structure = args.type == 'diff' and args.payment


# Main console program
if inadequate_length or negative_parameters or undefined_type or wrong_diff_structure:
    print('Incorrect parameters')
else:
    if (args.type and args.type == 'diff') and args.principal and args.periods and args.interest:
        calculate_differentiated_payment(args.principal, args.periods, args.interest)
    elif (args.type and args.type == 'annuity') and args.principal and args.periods and args.interest:
        calculate_annuity_monthly_payment(args.principal, args.periods, args.interest)
    elif (args.type and args.type == 'annuity') and args.payment and args.periods and args.interest:
        calculate_credit_principal(args.payment, args.periods, args.interest)
    elif (args.type and args.type == 'annuity') and args.principal and args.payment and args.interest:
        calculate_count_of_months(args.principal, args.payment, args.interest)