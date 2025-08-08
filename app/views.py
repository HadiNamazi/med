from django.shortcuts import render, redirect
from django.contrib.auth import login
from . import models
import jdatetime
from io import BytesIO
import xlsxwriter
from django.http import HttpResponse
from .gvars import form1_keys, form2_keys, form3_keys, form1_json, form2_json, form3_json
import os
from dotenv import load_dotenv

# loading .env file
load_dotenv()
PASSWORD = os.getenv('PASSWORD')

def number_to_excel_column(n):
    result = ""
    while n > 0:
        n -= 1
        result = chr(n % 26 + 65) + result
        n //= 26
    return result

#_______________________________________________________________________________________________________

def index(req):
    if not req.user.is_authenticated:
        return redirect('login-page')
    
    if not models.Form1.objects.all().exists():
        models.Form1.objects.create(data={"form_1": []}).save()
    if not models.Form2.objects.all().exists():
        models.Form2.objects.create(data={"form_2": []}).save()
    if not models.Form3.objects.all().exists():
        models.Form3.objects.create(data={"form_3": []}).save()

    return render(req, 'app/index.html', {})

def add_patient(req):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        return render(req, 'app/add_patient.html', {})

    if req.method == 'POST':
        name = req.POST['name']
        nc = req.POST['nc']
        pn = req.POST['pn']
        mpn = req.POST['mpn']
        hospital = req.POST.get('hospital')
        image = req.FILES.get('image')
        address = req.POST['address']
        patient = models.Patient.objects.create(
            name=name,
            national_code=nc,
            phone_num=pn,
            mobile_phone_num=mpn,
            hospital=hospital,
            image=image,
            address=address,
        )
        patient.save()
        return redirect('add-patient')

def patients(req):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        patients = models.Patient.objects.filter(deleted=False)

    if req.method == 'POST':
        customer_id = req.POST.get('searchinpt').split('-')[0]
        customer_id = int(customer_id[:len(customer_id)-1])
        patients = models.Patient.objects.filter(cid=customer_id, deleted=False)

    context = {
        'patients': patients,
    }
    return render(req, 'app/patients.html', context)

def edit_patient(req, cid):
    if not req.user.is_authenticated:
        return redirect('login-page')

    patient = models.Patient.objects.get(cid=cid)

    if req.method == 'GET':
        context = {
            'patient': patient,
        }
        return render(req, 'app/edit_patient.html', context)

    if req.method == 'POST':
        patient.name = req.POST['name']
        patient.national_code = req.POST['nc']
        patient.phone_num = req.POST['pn']
        patient.mobile_phone_num = req.POST['mpn']
        patient.hospital = req.POST.get('hospital')
        patient.image = req.FILES.get('image')
        patient.address = req.POST['address']
        patient.save()
        return redirect('edit-patient', patient.cid)

def delete_patient(req, cid):
    if not req.user.is_authenticated:
        return redirect('login-page')


    if req.method == 'GET':
        patient = models.Patient.objects.get(cid=cid)
        patient.deleted = True
        patient.save()
        
        return redirect('patients')

def form2(req):
    if not req.user.is_authenticated:
        return redirect('login-page')
    
    if req.method == 'GET':
        patients = models.Patient.objects.filter(deleted=False)
        context = {
            'action': 'submit',
            'patients': patients,
        }

        return render(req, 'app/form2.html', context)
    if req.method == 'POST':
        form = models.Form2.objects.get()

        if form.data['form_2'][-1]['id'] < 700:
            id = 700
        else:
            id = form.data['form_2'][-1]['id'] + 1

        customer_id = req.POST.get('searchinpt').split('-')[0]
        customer_id = int(customer_id[:len(customer_id)-1])
        date_of_submit = jdatetime.datetime.now().strftime("%Y/%m/%d")

        new_data = form2_json(req, id, customer_id, date_of_submit=date_of_submit)

        form.data['form_2'].append(new_data)
        form.save()
        return redirect('form2')

def form3(req):
    if not req.user.is_authenticated:
        return redirect('login-page')
    
    if req.method == 'GET':
        patients = models.Patient.objects.filter(deleted=False)
        context = {
            'action': 'submit',
            'patients': patients,
        }
        return render(req, 'app/form3.html', context)
    
    if req.method == 'POST':
        form = models.Form3.objects.get()

        if form.data['form_3'][-1]['id'] < 700:
            id = 700
        else:
            id = form.data['form_3'][-1]['id'] + 1

        customer_id = int(req.POST.get('searchinpt').split('-')[0])
        date_of_submit = jdatetime.datetime.now().strftime("%Y/%m/%d")

        new_data = form3_json(req, id, customer_id, date_of_submit=date_of_submit)

        form.data['form_3'].append(new_data)
        form.save()
        return redirect('form3')
    
def form1(req):
    if not req.user.is_authenticated:
        return redirect('login-page')
    
    if req.method == 'GET':
        patients = models.Patient.objects.filter(deleted=False)
        context = {
            'action': 'submit',
            'patients': patients,
        }
        return render(req, 'app/form1.html', context)
    
    if req.method == 'POST':
        form = models.Form1.objects.get()

        if form.data['form_1'][-1]['id'] < 700:
            id = 700
        else:
            id = form.data['form_1'][-1]['id'] + 1

        customer_id = req.POST.get('searchinpt').split('-')[0]
        customer_id = int(customer_id[:len(customer_id)-1])
        date_of_submit = jdatetime.datetime.now().strftime("%Y/%m/%d")

        new_data = form1_json(req, customer_id, id=id, date_of_submit=date_of_submit)

        form.data['form_1'].append(new_data)
        form.save()

        return redirect('form1')

def login_view(req):
    if req.user.is_authenticated:
        return redirect('index')

    if req.method == 'GET':
        return render(req, 'app/login_page.html', {})

    if req.method == 'POST':
        password = req.POST['password']
        user = models.CustomUser.objects.get(username='username')
        if password == PASSWORD:
            login(req, user)
            return redirect('index')
        return redirect('login-page')
    
def patient_base_report(req):
    if not req.user.is_authenticated:
        return redirect('login-page')

    patients = models.Patient.objects.filter(deleted=False)

    if req.method == 'GET':
        context = {
            'patients': patients,
        }
        return render(req, 'app/patient_base_report.html', context)

    if req.method == 'POST':
        try:
            patient = req.POST['searchinpt']
            patient_id = patient.split('-')[0]
            patient_id = int(patient_id[:len(patient_id)-1])
            patient_name = patient.split('-')[1][1:]
        except:
            return redirect('single-patient-report')
        
        form1 = models.Form1.objects.get().data['form_1']
        form2 = models.Form2.objects.get().data['form_2']
        form3 = models.Form3.objects.get().data['form_3']
        f_form1 = []
        f_form2 = []
        f_form3 = []
        
        for i in range(max(len(form1), len(form2), len(form3))):
            try:
                if form1[i]['customer_id'] == patient_id:
                    f_form1.append(form1[i])
            except:
                pass
            try:
                if form2[i]['customer_id'] == patient_id:
                    f_form2.append(form2[i])
            except:
                pass
            try:
                if form3[i]['customer_id'] == patient_id:
                    f_form3.append(form3[i])
            except:
                pass

        context = {
            'patients': patients,
            'patientname': patient_name,
            'form1': f_form1,
            'form2': f_form2, 
            'form3': f_form3,
        }
        return render(req, 'app/patient_base_report.html', context)

def show_form1(req, id):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        forms = models.Form1.objects.get().data['form_1']
        chosen_form = None

        for form in forms:
            if form['id'] == int(id):
                chosen_form = form
                break
        
        patient = models.Patient.objects.get(cid=chosen_form['customer_id'])
        context = {
            'action': 'show',
            'form' : chosen_form,
            'patient': patient,
        }
        return render(req, 'app/form1.html', context)

def show_form2(req, id):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        forms = models.Form2.objects.get().data['form_2']
        chosen_form = None

        for form in forms:
            if form['id'] == int(id):
                chosen_form = form
                break
        
        patient = models.Patient.objects.get(cid=chosen_form['customer_id'])
        context = {
            'action': 'show',
            'form' : chosen_form,
            'patient': patient,
        }
        return render(req, 'app/form2.html', context)

def show_form3(req, id):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        forms = models.Form3.objects.get().data['form_3']
        chosen_form = None

        for form in forms:
            if form['id'] == int(id):
                chosen_form = form
                break
        
        patient = models.Patient.objects.get(cid=chosen_form['customer_id'])
        context = {
            'action': 'show',
            'form' : chosen_form,
            'patient': patient,
        }
        return render(req, 'app/form3.html', context)

def edit_form1(req, id):
    if not req.user.is_authenticated:
        return redirect('login-page')

    form = models.Form1.objects.get()
    forms = form.data['form_1']
    chosen_form = None
    for f in forms:
        if f['id'] == int(id):
            chosen_form = f
            break

    if req.method == 'GET':
        patient = models.Patient.objects.get(cid=chosen_form['customer_id'])
        context = {
            'action': 'edit',
            'form' : chosen_form,
            'patient': patient,
        }
        return render(req, 'app/form1.html', context)

    elif req.method == 'POST':
        date_of_submit = chosen_form['date_of_submit']
        new_data = form1_json(req, int(chosen_form['customer_id']), id=int(id), date_of_submit=date_of_submit)
        for i in range(len(forms)):
            if forms[i]['id'] == int(id):
                forms[i] = new_data
                break
        form.data['form_1'] = forms
        form.save()
        return redirect('editform1', id)

def edit_form2(req, id):
    if not req.user.is_authenticated:
        return redirect('login-page')

    form = models.Form2.objects.get()
    forms = form.data['form_2']
    chosen_form = None
    for f in forms:
        if f['id'] == int(id):
            chosen_form = f
            break

    if req.method == 'GET':
        patient = models.Patient.objects.get(cid=chosen_form['customer_id'])
        context = {
            'action': 'edit',
            'form' : chosen_form,
            'patient': patient,
        }
        return render(req, 'app/form2.html', context)

    elif req.method == 'POST':
        date_of_submit = chosen_form['date_of_submit']
        new_data = form2_json(req, int(id), int(chosen_form['customer_id']), date_of_submit)
        for i in range(len(forms)):
            if forms[i]['id'] == int(id):
                forms[i] = new_data
                break
        form.data['form_2'] = forms
        form.save()
        return redirect('editform2', id)
    
def edit_form3(req, id):
    if not req.user.is_authenticated:
        return redirect('login-page')

    form = models.Form3.objects.get()
    forms = form.data['form_3']
    chosen_form = None
    for f in forms:
        if f['id'] == int(id):
            chosen_form = f
            break

    if req.method == 'GET':
        patient = models.Patient.objects.get(cid=chosen_form['customer_id'])
        context = {
            'action': 'edit',
            'form' : chosen_form,
            'patient': patient,
        }
        return render(req, 'app/form3.html', context)

    elif req.method == 'POST':
        date_of_submit = chosen_form['date_of_submit']
        new_data = form3_json(req, int(id), int(chosen_form['customer_id']), date_of_submit)
        for i in range(len(forms)):
            if forms[i]['id'] == int(id):
                forms[i] = new_data
                break
        form.data['form_3'] = forms
        form.save()
        return redirect('editform3', id)

def form1_base_report(req):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        patients = models.Patient.objects.filter(deleted=False)
        context = {
            'action': 'filter',
            'patients': patients,
        }
        return render(req, 'app/form1.html', context)

    elif req.method == 'POST':
        patient = req.POST['searchinpt']
        if patient:
            patient_id = patient.split('-')[0]
            patient_id = int(patient_id[:len(patient_id)-1])
        else:
            patient_id = None

        forms = models.Form1.objects.get().data['form_1']
        f_forms = []
        i_form = form1_json(req, customer_id=patient_id)

        for form in forms:
            matched = 0
            conflict = False
            for fkey, fvalue in form.items():
                for ikey, ivalue in i_form.items():
                    if fkey == ikey:
                        if fvalue == ivalue:
                            matched += 1
                        else:
                            conflict = True
                            break
                if conflict:
                    break
            if matched == len(i_form):
                try:
                    pname = models.Patient.objects.get(cid=form['customer_id']).name
                except:
                    print('a patient is deleted but its form is still there')
                form['pname'] = pname
                f_forms.append(form)

        context = {
            'f': '1',
            'forms': f_forms,
        }

        return render(req, 'app/form_base_report.html', context)

def form2_base_report(req):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        patients = models.Patient.objects.filter(deleted=False)
        context = {
            'action': 'filter',
            'patients': patients,
        }
        return render(req, 'app/form2.html', context)

    elif req.method == 'POST':
        patient = req.POST['searchinpt']
        if patient:
            patient_id = patient.split('-')[0]
            patient_id = int(patient_id[:len(patient_id)-1])
        else:
            patient_id = None

        forms = models.Form2.objects.get().data['form_2']
        f_forms = []
        i_form = form2_json(req, customer_id=patient_id)

        for form in forms:
            matched = 0
            conflict = False
            for fkey, fvalue in form.items():
                for ikey, ivalue in i_form.items():
                    if fkey == ikey:
                        if fvalue == ivalue:
                            matched += 1
                        else:
                            conflict = True
                            break
                if conflict:
                    break
            if matched == len(i_form):
                try:
                    pname = models.Patient.objects.get(cid=form['customer_id']).name
                except:
                    print('a patient is deleted but its form is still there')
                form['pname'] = pname
                f_forms.append(form)

        context = {
            'f': '2',
            'forms': f_forms,
        }
            
        return render(req, 'app/form_base_report.html', context)

def form3_base_report(req):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        patients = models.Patient.objects.filter(deleted=False)
        context = {
            'action': 'filter',
            'patients': patients,
        }
        return render(req, 'app/form3.html', context)

    elif req.method == 'POST':
        patient = req.POST['searchinpt']
        if patient:
            patient_id = patient.split('-')[0]
            patient_id = int(patient_id[:len(patient_id)-1])
        else:
            patient_id = None

        forms = models.Form3.objects.get().data['form_3']
        f_forms = []
        i_form = form3_json(req, customer_id=patient_id)

        for form in forms:
            matched = 0
            conflict = False
            for fkey, fvalue in form.items():
                for ikey, ivalue in i_form.items():
                    if fkey == ikey:
                        if fvalue == ivalue:
                            matched += 1
                        else:
                            conflict = True
                            break
                if conflict:
                    break
            if matched == len(i_form):
                try:
                    pname = ''
                    pname = models.Patient.objects.get(cid=form['customer_id']).name
                except:
                    print('a patient is deleted but its form is still there')
                form['pname'] = pname
                f_forms.append(form)

        context = {
            'f': '3',
            'forms': f_forms,
        }
            
        return render(req, 'app/form_base_report.html', context)

def delete_form1(req, id):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        forms = models.Form1.objects.get()
        form1 = forms.data['form_1']
        o_forms = []

        for form in form1:
            if form['id'] != int(id):
                o_forms.append(form)
        
        forms.data['form_1'] = o_forms
        forms.save()

        return redirect('index')
    
def delete_form2(req, id):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        forms = models.Form2.objects.get()
        form2 = forms.data['form_2']
        o_forms = []

        for form in form2:
            if form['id'] != int(id):
                o_forms.append(form)
        
        forms.data['form_2'] = o_forms
        forms.save()

        return redirect('index')
    
def delete_form3(req, id):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        forms = models.Form3.objects.get()
        form3 = forms.data['form_3']
        o_forms = []

        for form in form3:
            if form['id'] != int(id):
                o_forms.append(form)
        
        forms.data['form_3'] = o_forms
        forms.save()

        return redirect('index')

def excel_export(req, formnum, id):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        if formnum == '1':
            forms = models.Form1.objects.get().data['form_1']
        elif formnum == '2':
            forms = models.Form2.objects.get().data['form_2']
        elif formnum == '3':
            forms = models.Form3.objects.get().data['form_3']

        chosen_form = None
        for form in forms:
            try:
                cid = form['customer_id']
                patient = models.Patient.objects.get(cid=cid)
            except:
                return redirect('index')
            if form['id'] == int(id) and not patient.deleted:
                chosen_form = form
                break
        if not chosen_form:
            return redirect('index')

        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        i = 0
        for key, value in chosen_form.items():
            i += 1
            worksheet.write(f'{number_to_excel_column(i)}1', key)
            worksheet.write(f'{number_to_excel_column(i)}2', str(value))

        worksheet.autofit()
        workbook.close()
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f"attachment;filename=form{formnum} - {chosen_form['id']}.xlsx"
        response.write(output.getvalue())

        return response
    
def excel_export_all(req, formnum):
    if not req.user.is_authenticated:
        return redirect('login-page')

    if req.method == 'GET':
        ids_str = req.GET.get('ids')
        ids = list(map(int, ids_str.split(',')))

        if formnum == '1':
            forms = models.Form1.objects.get().data['form_1']
        elif formnum == '2':
            forms = models.Form2.objects.get().data['form_2']
        elif formnum == '3':
            forms = models.Form3.objects.get().data['form_3']

        chosen_forms = []
        for form in forms:
            cid = form.get('customer_id')
            fid = form.get('id')

            if cid is None or fid is None:
                continue

            if fid not in ids:
                continue

            try:
                patient = models.Patient.objects.get(cid=cid)
            except models.Patient.DoesNotExist:
                print(f"Patient with cid {cid} not found.")
                continue
            except Exception as e:
                print(f"Error fetching patient for cid {cid}:", e)
                return redirect('index')

            if not patient.deleted:
                chosen_forms.append(form)

        if chosen_forms == []:
            return redirect('index')

        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        headers = chosen_forms[0].keys()

        for col_index, key in enumerate(headers):
            worksheet.write(0, col_index, key)

        for row_index, form in enumerate(chosen_forms, start=1):
            for col_index, key in enumerate(headers):
                worksheet.write(row_index, col_index, str(form.get(key, '')))

        worksheet.autofit()
        workbook.close()
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = f"attachment; filename=form{formnum}-all.xlsx"
        response.write(output.getvalue())
        return response



def multi_patient_report(req):
    if not req.user.is_authenticated:
        return redirect('login-page')

    patients = models.Patient.objects.filter(deleted=False)

    if req.method == 'GET':
        context = {
            'patients': patients,
        }
        return render(req, 'app/multi_patient_report.html', context)

    elif req.method == 'POST':
        count = req.POST['hiddeninput']
        patientids = []

        if count == 'All':
            patients = models.Patient.objects.filter(deleted=False)
            for patient in patients:
                patientids.append(int(patient.cid))
        else:
            for i in range(int(count)):
                try:
                    patient = req.POST[f'searchinpt-{i+1}']
                    patient_id = patient.split('-')[0]
                    patient_id = int(patient_id[:len(patient_id)-1])
                    patient = models.Patient.objects.get(cid=patient_id)
                    if patient.deleted:
                        raise Exception
                except:
                    patient_id = None
                patientids.append(patient_id)

        latest_forms = []
        for patientid in patientids:
            latest_form1 = latest_form2 = latest_form3 = None
            form1 = models.Form1.objects.get().data['form_1']
            for i in reversed(range(len(form1)-1)):
                if form1[i]['customer_id'] == patientid:
                    latest_form1 = form1[i]
                    break
            form2 = models.Form2.objects.get().data['form_2']
            for i in reversed(range(len(form2)-1)):
                if form2[i]['customer_id'] == patientid:
                    latest_form2 = form2[i]
                    break
            form3 = models.Form3.objects.get().data['form_3']
            for i in reversed(range(len(form3)-1)):
                if form3[i]['customer_id'] == patientid:
                    latest_form3 = form3[i]
                    break
            latest_forms.append([latest_form1, latest_form2, latest_form3])

        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet1 = workbook.add_worksheet('Form1')
        worksheet2 = workbook.add_worksheet('Form2')
        worksheet3 = workbook.add_worksheet('Form3')
        for j in range(len(latest_forms)):
            lf1 = latest_forms[j][0]
            if lf1:
                for i in range(len(form1_keys)):
                    worksheet1.write(f'{number_to_excel_column(i+1)}1', form1_keys[i])
                i = 0
                cid = lf1['customer_id']
                pname = models.Patient.objects.get(cid=cid).name
                lf1['patient_name'] = pname
                for key, value in lf1.items():
                    i += 1
                    worksheet1.write(f'{number_to_excel_column(form1_keys.index(key)+1)}{j+2}', str(value))
            lf2 = latest_forms[j][1]
            if lf2:
                for i in range(len(form2_keys)):
                    worksheet2.write(f'{number_to_excel_column(i+1)}1', form2_keys[i])
                i = 0
                cid = lf2['customer_id']
                pname = models.Patient.objects.get(cid=cid).name
                lf2['patient_name'] = pname
                for key, value in lf2.items():
                    i += 1
                    worksheet2.write(f'{number_to_excel_column(form2_keys.index(key)+1)}{j+2}', str(value))
            lf3 = latest_forms[j][2]
            if lf3:
                for i in range(len(form3_keys)):
                    worksheet3.write(f'{number_to_excel_column(i+1)}1', form3_keys[i])
                i = 0
                cid = lf3['customer_id']
                pname = models.Patient.objects.get(cid=cid).name
                lf3['patient_name'] = pname
                for key, value in lf3.items():
                    i += 1
                    worksheet3.write(f'{number_to_excel_column(form3_keys.index(key)+1)}{j+2}', str(value))

        worksheet1.autofit()
        worksheet2.autofit()
        worksheet3.autofit()
        workbook.close()
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = "attachment;filename=formMulti patient report.xlsx"
        response.write(output.getvalue())
        return response
