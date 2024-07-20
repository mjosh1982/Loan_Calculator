# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'

import math as m
import argparse as ap

loan_principal = 0
calculation_type_m = 'm'
calculation_type_p = 'p'
monthly_payment = 0
number_of_months = 0


# write your code here
def calculate_number_of_months(loan_principal, monthly_payment):
    '''
    This function calculates the number of months it will take to repay the loan.
    This is executed when the user selects the options as 'm' for number of months.
    :param loan_principal: The loan principal amount
    :param monthly_payment: The monthly payment amount
    :return: The number of months it will take to repay the loan
    '''
    global number_of_months
    number_of_months = loan_principal // monthly_payment
    if loan_principal % monthly_payment != 0:
        number_of_months += 1

    if number_of_months > 1:
        print(f'It will take {number_of_months} months to repay the loan')
    else:
        print(f'It will take {number_of_months} month to repay the loan')
    return number_of_months


def calculate_monthly_payment(loan_principal, number_of_months):
    '''
    This function calculates the monthly payment amount.
    :param loan_principal: The loan principal amount
    :param number_of_months: The number of months it will take to repay the loan
    :return: The monthly payment amount
    '''
    global monthly_payment
    monthly_payment = m.ceil(loan_principal / number_of_months)
    if loan_principal % number_of_months != 0:
        last_payment = loan_principal - (number_of_months - 1) * monthly_payment
        print(f'Your monthly payment = {monthly_payment} and the last payment = {last_payment}.')
    else:
        print(f'Your monthly payment = {monthly_payment}')
    return monthly_payment


def get_inputs():
    # loan_principal = int(input('Enter the loan principal:\n'))
    parser = ap.ArgumentParser()
    # write argument to take the --principal argument from command line
    parser.add_argument('--principal', type=int, default=0)
    # write argument to take the --interest argument from command line
    parser.add_argument('--interest', type=float, default=0.0)
    # write argument to take the --periods argument from command line
    parser.add_argument('--periods', type=int, default=0)
    # write argument to take the --payment argument from command line
    parser.add_argument('--payment', type=float, default=0.0)
    # write argument to take the --type argument from command line
    parser.add_argument('--type', type=str, default='None')
    # parse the arguments
    args = parser.parse_args()

    loan_principal = args.principal
    interest = args.interest
    periods = args.periods
    payment = args.payment
    nominal_interest = interest / (12 * 100)
    type = args.type
    choices = ['annuity', 'diff']

    if type not in choices:
        print('Incorrect parameters')
        exit(1)

    if loan_principal > 0 and periods > 0 and interest > 0:
        if type == 'annuity':
            payment = loan_principal * (nominal_interest * (1 + nominal_interest) ** periods) / (
                    (1 + nominal_interest) ** periods - 1)
            print(f'Your monthly payment = {m.ceil(payment)}!')
        elif type == 'diff':
            total_payment = 0
            for i in range(1, periods + 1):
                diff_payment = m.ceil(
                    loan_principal / periods + nominal_interest * (
                            loan_principal - (loan_principal * (i - 1)) / periods))
                total_payment += diff_payment
                print(f'Month {i}: payment is {diff_payment}')
            overpayment = total_payment - loan_principal
            print(f'\nOverpayment = {overpayment}')

    elif periods > 0 and payment > 0 and interest > 0:
        if type == 'annuity':
            loan_principal = payment / (
                    (nominal_interest * (1 + nominal_interest) ** periods) / ((1 + nominal_interest) ** periods - 1))
            print(f'Your loan principal = {round(loan_principal)}!')
        elif type == 'diff':
            print('Incorrect parameters')
            exit(1)
    elif loan_principal > 0 and payment > 0 and interest > 0:
        if type == 'annuity':
            periods = m.ceil(m.log(payment / (payment - nominal_interest * loan_principal), 1 + nominal_interest))
            years = periods // 12
            months = periods % 12
            if years > 0 and months > 0:
                print(f'You need {years} years and {months} months to repay this loan!')
            elif years > 0:
                print(f'You need {years} years to repay this loan!')
            elif months > 0:
                print(f'You need {months} months to repay this loan!')
            # write code to calculate the overpayment
            overpayment = periods * payment - loan_principal
            print(f'Overpayment = {overpayment}')

        elif type == 'diff':
            print('Incorrect parameters')
            exit(1)
    elif loan_principal > 0 and payment > 0 and periods > 0:
        if type == 'annuity':
            # nominal_interest = 1
            # while True:
            #     nominal_interest += 0.0001
            #     payment = loan_principal * (nominal_interest * (1 + nominal_interest) ** periods) / (
            #             (1 + nominal_interest) ** periods - 1)
            #     if m.ceil(payment) == payment:
            #         print(f'Your interest rate = {round(nominal_interest * 12 * 100, 2)}!')
            #         break
            print('Incorrect parameters')
            exit(1)
        elif type == 'diff':
            print('Incorrect parameters')
            exit(1)
    else:
        print('Incorrect parameters')
        exit(1)


def start():
    get_inputs()


start()
