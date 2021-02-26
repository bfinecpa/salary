from django.shortcuts import render
from .models import Salary
from openpyxl import load_workbook

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'common/login.html')

def salary(request):
    """
    pybo 답변등록
    """
    if request.user.get_username()=="admin":
        return render(request, 'salary/excel.html')

    memo_name = request.user.get_username()

    # salary = get_object_or_404( Salary, username=Salary.name)\
    try:
        salary = Salary.objects.get(employee_number=memo_name)
    except:
        return render(request, 'salary/error.html')
    # salary = Salary.objects_or_404(name=memo_name)
    # for key in list(salary.objects()):
    #     if key.value ==None: key.value =''
    # for k,v in salary.items():
    #     if v is None: salary[k]=''
    context = {'salary': salary, 'name': memo_name}
    return render(request, 'salary/salary.html', context)


def excelIndex(request):
    if "GET" == request.method:
        """
               pybo 목록 출력
               """
        return render(request, 'salary/excel.html')


    else:
        excel_file = request.FILES["excel_file"]

        # data_only=Ture로 해줘야 수식이 아닌 값으로 받아온다.
        load_wb = load_workbook(excel_file, data_only=True)

        # 시트 이름으로 불러오기
        load_ws = load_wb['급여보고']
        dict = {}
        dict['salary_name'] = load_ws['H1'].value.split('급')[0].strip()

        # 셀 주소로 값 출력
        # print(load_ws['A1'].value)

        Salary.objects.all().delete()
        rows = load_ws.rows
        for idx,r in enumerate(rows) :
            if idx<3:
                continue
            if r[2].value == None: break
            dict['employee_number'] = r[1].value
            dict['name'] = r[5].value.split()[0]
            dict['employee_code'] = r[6].value
            if r[8].value :dict['total_payment'] = f'{r[8].value:,}'
            if r[9].value :dict['total_deduction'] =f'{r[9].value:,}'
            if r[10].value:dict['actual_payment'] = f'{r[10].value:,}'
            if r[11].value:dict['normal'] = f'{r[11].value:,}'
            if r[34].value:dict['other_one'] = f'{r[34].value:,}' #not change
            if r[13].value:dict['meals'] =f'{r[13].value:,}'
            if r[21].value :dict['maternity_leave'] = f'{r[21].value:,}'
            # if r[23].value :dict['incentive'] = f'{r[23].value:,}' 성과급 없음
            if r[16].value :dict['license_allowance'] = f'{r[16].value:,}'
            if r[17].value :dict['overtime_allowance'] = f'{r[17].value:,}'
            if r[18].value :dict['duty_allowance'] = f'{r[18].value:,}'
            if r[19].value :dict['annual_allowance'] = f'{r[19].value:,}'
            if r[20].value :dict['other_allowance'] = f'{r[20].value:,}'
            if r[22].value :dict['long_term_reward'] = f'{r[22].value:,}'
            if r[15].value :dict['school_expenses'] = f'{r[15].value:,}'
            if r[25].value :dict['income_tax'] = f'{r[25].value:,}'
            if r[32].value :dict['national_pension'] = f'{r[32].value:,}'
            if r[31].value :dict['employment_insurance'] = f'{r[31].value:,}'
            if r[30].value :dict['health_insurance_premium'] = f'{r[30].value:,}'
            if r[26].value :dict['local_income_tax'] = f'{r[26].value:,}'
            # if r[34].value :dict['long_term_care_premium'] = f'{r[34].value:,}' 장기요양보험료
            if r[33].value :dict['membership_fee'] = f'{r[33].value:,}'
            # if r[29].value :dict['repayment_of_hosing_funds'] = f'{r[29].value:,}'
            if r[27].value: dict['Year_end_settlement_income_tax'] = f'{r[27].value:,}'
            if r[28].value: dict['local_income_tax_for_year_end_settlement'] = f'{r[28].value:,}'
            if r[20].value: dict['other_allowance'] = f'{r[20].value:,}'
            # if r[35].value :dict['health_insurance_premium_settlement'] = f'{r[35].value:,}'
            # if r[36].value :dict['long_term_care_premium_settlement'] = f'{r[36].value:,}'
            # dict['department'] = r[40].value 부서
            # dict['entered_date'] = r[47].value 입사일 안됨
            dict['rank'] = r[7].value
            Salary(**dict).save()

        return render(request, 'salary/excel.html', {})