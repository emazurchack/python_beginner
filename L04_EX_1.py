import sys
def get_employee_payroll(production_in_hours, rate_per_hour, premium):
    # (выработка в часах * ставка в час) + премия
    return (production_in_hours * rate_per_hour) + premium

if __name__ == '__main__':
    print(get_employee_payroll(sys.argv[1], sys.argv[2], sys.argv[3]))