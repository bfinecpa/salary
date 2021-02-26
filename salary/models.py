from django.db import models

# Create your models here.
class Salary(models.Model):
    models.IntegerField(blank=True, null=True)
    models.FloatField(blank=True, null=True)
    # 월급계산서 이름
    salary_name = models.TextField(default='', blank=True, null=False)
    # 사번
    employee_number = models.TextField(default='', blank=True, null=False)
    # 사원명
    name = models.CharField(blank=True, null=True, max_length=4)
    # 사원코드
    employee_code = models.TextField(default='', blank=True, null=False)
    # 지금액계
    total_payment = models.TextField(default='', blank=True, null=False)
    # 공제액계
    total_deduction = models.TextField(default='', blank=True, null=False)
    # 차인지급액
    actual_payment = models.TextField(default='', blank=True, null=False)
    # 입사일 호봉 직급 부서
    entered_date = models.TextField(default='', blank=True, null=False)
    salary_step = models.TextField(default='', blank=True, null=False)
    rank = models.TextField(default='', blank=True, null=False)
    department = models.TextField(default='', blank=True, null=False)

    # 기본급 , 명절 지원금 , 성과급
    normal = models.TextField(default='', blank=True, null=False)
    holiday_subsidy = models.TextField(default='', blank=True, null=False)
    incentive = models.TextField(default='', blank=True, null=False)

    # 기타급여정산분  #자녀학자금지원
    other_salary_settlement = models.TextField(default='', blank=True, null=False)
    school_expenses = models.TextField(default='', blank=True, null=False)

    # 면허수당 #시간외수당 #당직수당 #연차수당
    license_allowance = models.TextField(default='', blank=True, null=False)
    overtime_allowance = models.TextField(default='', blank=True, null=False)
    duty_allowance = models.TextField(default='', blank=True, null=False)
    annual_allowance = models.TextField(default='', blank=True, null=False)

    # 장기근속/포상금, 기타수당 , 기타1(지급) 산전휴가/육아휴직 , 식대
    long_term_reward = models.TextField(default='', blank=True, null=False)
    other_allowance = models.TextField(default='', blank=True, null=False)
    other_salary_payments = models.TextField(default='', blank=True, null=False)
    maternity_leave = models.TextField(default='', blank=True, null=False)
    meals = models.TextField(default='', blank=True, null=False)

    # 여기부터 공제
    # 국민연금 , 건강보험, 고용보험 , 장기요양보험료
    national_pension = models.TextField(default='', blank=True, null=False)
    health_insurance_premium = models.TextField(default='', blank=True, null=False)
    employment_insurance = models.TextField(default='', blank=True, null=False)
    long_term_care_premium = models.TextField(default='', blank=True, null=False)

    # 소득세, 지방소득세, 연말정산소득세, 연말정산지방소득세, 연말정산농특세
    income_tax = models.TextField(default='', blank=True, null=False)
    local_income_tax = models.TextField(default='', blank=True, null=False)
    Year_end_settlement_income_tax = models.TextField(default='', blank=True, null=False)
    local_income_tax_for_year_end_settlement = models.TextField(default='', blank=True, null=False)
    year_and_settlement_agricultural_special_tax = models.TextField(default='', blank=True, null=False)

    # 사우회비, 주택자금상환 , 기타1, 기타2, 건강보험료정산, 장기요양보험정산
    membership_fee = models.TextField(default='', blank=True, null=False)
    repayment_of_hosing_funds = models.TextField(default='', blank=True, null=False)
    other_one = models.TextField(default='', blank=True, null=False)
    other_two = models.TextField(default='', blank=True, null=False)
    health_insurance_premium_settlement = models.TextField(default='', blank=True, null=False)
    long_term_care_premium_settlement = models.TextField(default='', blank=True, null=False)

    def __str__(self):
        return self.name


class Go(models.Model):
    employee_number = models.TextField()
    name = models.CharField(max_length=4)
    Code = models.TextField()
    total_payment = models.TextField(blank=True, null=True)
    total_deduction = models.TextField(blank=True, null=True)
    actual_payment = models.TextField(blank=True, null=True)
    last_payment = models.TextField(blank=True, null=True)
    other_salary = models.TextField(blank=True, null=True)
    meals = models.TextField(blank=True, null=True)
    maternity_leave = models.TextField(blank=True, null=True)
    Incentive = models.TextField(blank=True, null=True)
    payroll = models.TextField(blank=True, null=True)
    school_expenses = models.TextField(blank=True, null=True)
    license_allowance = models.TextField(blank=True, null=True)
    overtime_allowance = models.TextField(blank=True, null=True)
    duty_allowance = models.TextField(blank=True, null=True)
    annual_allowance = models.TextField(blank=True, null=True)
    other_allowance = models.TextField(blank=True, null=True)
    long_term_reward = models.TextField(blank=True, null=True)
    RSP = models.TextField(blank=True, null=True)
    allowance = models.TextField(blank=True, null=True)
    resident_tax = models.TextField(blank=True, null=True)
    tax_meter = models.TextField(blank=True, null=True)
    health_insurance_premium = models.TextField(blank=True, null=True)
    employment_insurance_premium = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name