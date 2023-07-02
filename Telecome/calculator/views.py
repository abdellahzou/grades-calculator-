# views.py
from django.shortcuts import render
def home_page(request):
    return render(request, 'calculator/home_page.html')
def home_page_ar(request):
    return render(request, 'calculator/home_page_ar.html')

def mi(request):
    return render(request, 'calculator/mi.html')
def mis1(request):
    if request.method == 'POST':
        ana1 = float(request.POST.get('ana1'))
        alg1 = float(request.POST.get('alg1'))
        algo1 = float(request.POST.get('algo1'))
        sm1 = float(request.POST.get('sm1'))
        phy1 = float(request.POST.get('phy1'))
        tseee = float(request.POST.get('tseee'))
        le = float(request.POST.get('le'))
        
        # Perform calculations or any desired actions
        total = ana1*4 + alg1*3 + algo1*4 + sm1*3 + phy1*2 + tseee + le
        average = total / 18
        average = round(average, 2)

        # Render the result page or pass the average to the template context
        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/mis1.html')

def mis2(request):
    if request.method == 'POST':
        ana2 = float(request.POST.get('ana2'))
        alg2 = float(request.POST.get('alg2'))
        algo2 = float(request.POST.get('algo2'))
        sm2 = float(request.POST.get('sm2'))
        phy2 = float(request.POST.get('phy2'))
        tic = float(request.POST.get('tic'))
        ipsd = float(request.POST.get('ipsd'))
        oppm = float(request.POST.get('oppm'))
        
        # Perform calculations or any desired actions
        total = ana2*4 + alg2*2 + algo2*2 + sm2*2 + phy2*2 + tic + ipsd*2 + oppm
        average = total / 18
        average = round(average, 2)

        # Render the result page or pass the average to the template context
        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/mis2.html')

def st(request):
    return render(request, 'calculator/st.html')

def st1er(request):
    return render(request, 'calculator/st1er.html')


def sts1(request):
    if request.method == 'POST':
        # Retrieve the values from the form
        exam_math1 = float(request.POST.get('exam-math1'))
        exam_physique1 = float(request.POST.get('exam-physique1'))
        exam_sdm = float(request.POST.get('exam-sdm'))
        exam_info = float(request.POST.get('exam-info'))
        td_math1 = float(request.POST.get('TD-math1'))
        td_physique1 = float(request.POST.get('TD-phy1'))
        td_sdm = float(request.POST.get('TD-sdm'))
        td_informatique = float(request.POST.get('TD-informatique'))
        tp_physique1 = float(request.POST.get('TP-phy'))
        tp_chimie1 = float(request.POST.get('TD-chimie'))
        exam_metho = float(request.POST.get('exam-metho'))
        exam_lang = float(request.POST.get('exam-lang'))
        les_metier = float(request.POST.get('Les metier'))

        math1 = (exam_math1*0.6 + td_math1*0.4)*3
        physique1 = (exam_physique1*0.6 + td_physique1*0.4)*3
        sdm = (exam_sdm*0.6 + td_sdm*0.4)*3
        info = (exam_info*0.6 + td_informatique*0.4)*2
        meth = (exam_metho)*1
        metier = (les_metier)*1
        tpchimie = (tp_chimie1)*1
        tpphys = tp_physique1*1
        langues = exam_lang*2
        

        # Perform calculations or any desired actions
        total = math1 + physique1 + sdm + info + meth + metier + tpchimie + tpphys +langues
        average = total / 17
        average = round(average, 2)

        # Render the result page or pass the average to the template context
        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/sts1.html')


def sts2(request):
    if request.method == 'POST':
        exam_math2 = float(request.POST.get('exam-math2'))
        exam_physique2 = float(request.POST.get('exam-physique2'))
        exam_thermo = float(request.POST.get('exam-thermo'))
        exam_info = float(request.POST.get('exam-info'))
        td_math2 = float(request.POST.get('TD-math2'))
        td_physique2 = float(request.POST.get('TD-phy2'))
        td_thermo = float(request.POST.get('TD-thermo'))
        td_informatique = float(request.POST.get('TD-informatique'))
        tp_physique2 = float(request.POST.get('TP-phy'))
        tp_chimie2 = float(request.POST.get('TD-chimie'))
        exam_metho = float(request.POST.get('exam-metho'))
        exam_lang = float(request.POST.get('exam-lang'))
        les_metier = float(request.POST.get('Les metier'))

        math2 = (exam_math2 * 0.6 + td_math2 * 0.4) * 3
        physique2 = (exam_physique2 * 0.6 + td_physique2 * 0.4) * 3
        thermo = (exam_thermo * 0.6 + td_thermo * 0.4) * 3
        info2 = (exam_info * 0.6 + td_informatique * 0.4) * 2
        meth = exam_metho * 1
        metier = les_metier * 1
        tpchimie2 = tp_chimie2 * 1
        tpphys2 = tp_physique2 * 1
        langues = exam_lang * 2

        # Perform calculations or any desired actions
        total = math2 + physique2 + thermo + info2 + meth + metier + tpchimie2 + tpphys2 + langues
        average = total / 17
        average = round(average, 2)

        # Render the result page or pass the average to the template context
        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/sts2.html')

def Telecome(request):
    # Logic for the bar page
    # You can perform any necessary operations or retrieve data for this page
    return render(request, 'calculator/Telecome.html')


def TelecomeM1S2(request):
    if request.method == 'POST':
        exam_adm = float(request.POST.get('exam-adm'))
        TD_adm = float(request.POST.get('test-adm'))
        exam_caneau = float(request.POST.get('exam-Caneau'))
        TD_caneau = float(request.POST.get('test-Caneau'))
        exam_fpga = float(request.POST.get('exam-FPGA'))
        TD_fpga = float(request.POST.get('test-FPGA'))
        exam_codage = float(request.POST.get('exam-codage'))
        TD_codage = float(request.POST.get('test-codage'))
        exam_sql = float(request.POST.get('exam-SQL'))
        TP_codage = float(request.POST.get('TP-codage'))
        exam_rhd = float(request.POST.get('exam-RHD'))
        TP_rhd= float(request.POST.get('test-RHD'))
        exam_ro = float(request.POST.get('exam-RO'))
        TP_fpga = float(request.POST.get('TP-FPGA'))
        exam_ethique = float(request.POST.get('exam-ethique'))
        TP_adm = float(request.POST.get('TP-ADM'))
        # Process the notes or perform any desired action
        # Redirect to a success page or render a response
        
        ADM=(exam_adm*0.6 + TD_adm*0.4)*3
        caneau=(exam_caneau*0.6 + TD_caneau*0.4)*2
        fpga=(exam_fpga*0.6 + TD_fpga*0.4)*2
        codage=(exam_codage*0.6 + TD_codage*0.4)*2
        rhd=(exam_rhd*0.6 + TP_rhd*0.4)*2
        sql=(exam_sql)*1
        ro=(exam_ro)*1
        ethique=(exam_ethique)*1
        tpadm=(TP_adm)*1
        tpcodage=(TP_codage)*1
        tpfpga=(TP_fpga)*1
        total = ADM+caneau+fpga+codage+sql+rhd+ro+ethique+tpadm+tpcodage+tpfpga
        average = total / 17
        # You can round the average to a desired number of decimal places
        average = round(average, 2)  # Rounds to 2 decimal places

        # Render the result page or pass the average to the template context
        return render(request, 'calculator/result_page.html', {'average': average})
    return render(request, 'calculator/TelecomeM1S2.html')

def TelecomeM1S1(request):
    if request.method == 'POST':
       python_exam = float(request.POST.get('exam-python'))
       python_TP = float(request.POST.get('TP-python'))
       linux_exam = float(request.POST.get('exam-linux'))
       CNA_exam = float(request.POST.get('exam-CNA'))
       CNA_TP = float(request.POST.get('TP-CNA'))
       CNA_TD = float(request.POST.get('TD-CNA'))
       TAS_exam = float(request.POST.get('exam-TAS'))
       TAS_TD = float(request.POST.get('TD-TAS'))
       TAS_TP = float(request.POST.get('TP-TAS'))
       routage_exam = float(request.POST.get('exam-routage'))
       routage_TP = float(request.POST.get('TP-routage'))
       routage_TD = float(request.POST.get('TD-routage'))
       PA_exam = float(request.POST.get('exam-PA'))
       PA_TD = float(request.POST.get('TD-PA'))
       anglais = float(request.POST.get('anglais'))
       NP_exam = float(request.POST.get('exam-NP'))

       total = (python_exam * 0.6 + python_TP * 0.4) * 2 + linux_exam * 1 + (CNA_exam * 0.6 + CNA_TD * 0.4) * 3 + CNA_TP * 1 + (TAS_exam * 0.6 + TAS_TD * 0.4) * 2 + TAS_TP * 1 + (routage_exam*0.6 + routage_TD*0.4) * 2 + routage_TP * 1 + (PA_exam*0.6 + PA_TD*0.4) * 2 + anglais * 1 + NP_exam * 1
       average = total / 17
        # You can round the average to a desired number of decimal places
       average = round(average, 2)  # Rounds to 2 decimal places

        # Render the result page or pass the average to the template context
       return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/TelecomeM1S1.html')



def bac_page(request):
    # Logic for the bar page
    # You can perform any necessary operations or retrieve data for this page
    return render(request, 'calculator/bac_page.html')
def bac_page_ar(request):
    # Logic for the bar page
    # You can perform any necessary operations or retrieve data for this page
    return render(request, 'calculator/bac_page_ar.html')


def calculate_average(request, subject_weights, template_name):
    if request.method == 'POST':
        notes = {}
        total_weight = sum(subject_weights.values())

        for subject, weight in subject_weights.items():
            note = float(request.POST.get(subject))
            notes[subject] = note * weight
            
        if notes['Sport'] == 0:
            total = sum(notes.values())
            average = total / (total_weight - 1)
        else:
            total = sum(notes.values())
            average = total / total_weight

        # You can round the average to a desired number of decimal places
        average = round(average, 2)  # Rounds to 2 decimal places

        # Render the result page or pass the average to the template context
        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, template_name)

def Math(request):
    subject_weights = {
        'Arabe': 3,
        'Anglais': 2,
        'Français': 2,
        'Math': 7,
        'Sciences': 2,
        'Physiques': 6,
        'Histoire Geo': 2,
        'Sciences Islamiques': 2,
        'Philo': 2,
        'Sport': 1,
        # Add more subjects and their weights here
    }
    template_name = 'calculator/math.html'
    return calculate_average(request, subject_weights, template_name)

def Math_Technique(request):
    subject_weights = {
        'Arabe': 3,
        'Anglais': 2,
        'Français': 2,
        'Math': 6,
        'Technologie': 7,
        'Physiques': 6,
        'Histoire Geo': 2,
        'Sciences Islamiques': 2,
        'Philo': 2,
        'Sport': 1,
        # Add more subjects and their weights here
    }
    template_name = 'calculator/math_technique.html'
    return calculate_average(request, subject_weights, template_name)


def Gestion(request):
    subject_weights = {
        'Arabe': 3,
        'Anglais': 2,
        'Français': 2,
        'Math': 5,
        'Loi': 2,
        'Gestion': 6,
        'Economie et Management': 5,
        'Histoire Geo': 4,
        'Sciences Islamiques': 2,
        'Philo': 2,
        'Sport': 1,
        # Add more subjects and their weights here
    }
    template_name = 'calculator/gestion.html'
    return calculate_average(request, subject_weights, template_name)


def science(request):
    subject_weights = {
        'Arabe': 3,
        'Anglais': 2,
        'Français': 2,
        'Math': 5,
        'Science': 6,
        'Physiques': 5,
        'Histoire Geo': 2,
        'Sciences Islamiques': 2,
        'Philo': 2,
        'Sport': 1,
        # Add more subjects and their weights here
    }
    template_name = 'calculator/science.html'
    return calculate_average(request, subject_weights, template_name)


def les_langues(request):
    subject_weights = {
        'Arabe': 5,
        'Anglais': 5,
        'Français': 5,
        'Math': 2,
        'Deutsch/Espagnol': 4,
        'Histoire Geo': 2,
        'Sciences Islamiques': 2,
        'Philo': 2,
        'Sport': 1,
        # Add more subjects and their weights here
    }
    template_name = 'calculator/les_langues.html'
    return calculate_average(request, subject_weights, template_name)


def philo(request):
    subject_weights = {
        'Arabe': 6,
        'Anglais': 3,
        'Français': 3,
        'Math': 2,
        'Histoire Geo': 4,
        'Sciences Islamiques': 2,
        'Philo': 6,
        'Sport': 1,
        # Add more subjects and their weights here
    }
    template_name = 'calculator/philo.html'
    return calculate_average(request, subject_weights, template_name)


def droitl1(request):
    return render(request, 'calculator/droitl1.html')

def droitl1s1(request):
    if request.method == 'POST':
        PL = float(request.POST.get('PL'))
        IC = float(request.POST.get('IC'))
        HS = float(request.POST.get('HS'))
        LA = float(request.POST.get('LA'))
        LAN = float(request.POST.get('LAN'))
        LC = float(request.POST.get('LC'))
        SC = float(request.POST.get('SC'))
        LATD = float(request.POST.get('LATD'))
        LCTD = float(request.POST.get('LCTD'))
        SCTD = float(request.POST.get('SCTD'))
        total = ((LA*3 + LATD*2)/5)*1 +((LC*3+LCTD*2)/5)*2 + ((SC*3+SCTD*2)/5)*2 + IC + HS + PL + LAN 

        average = total / 9
        average = round(average, 2)

        # Render the result page or pass the average to the template context
        return render(request, 'calculator/result_page.html', {'average': average})
    return render(request, 'calculator/droitl1s1.html')
def droitl1s2(request):
    if request.method == 'POST':
        SM = float(request.POST.get('SM'))
        EP = float(request.POST.get('EP'))
        IS = float(request.POST.get('IS'))
        LA2 = float(request.POST.get('LA2'))
        LAN2 = float(request.POST.get('LAN2'))
        LC2 = float(request.POST.get('LC2'))
        SC2 = float(request.POST.get('SC2'))
        LATD2 = float(request.POST.get('LATD2'))
        LCTD2 = float(request.POST.get('LCTD2'))
        SCTD2 = float(request.POST.get('SCTD2'))
        total = ((LA2*3 + LATD2*2)/5)*1 +((LC2*3+LCTD2*2)/5)*2 + ((SC2*3+SCTD2*2)/5)*2 + EP + IS + SM + LAN2 

        average = total / 9
        average = round(average, 2)

        # Render the result page or pass the average to the template context
        return render(request, 'calculator/result_page.html', {'average': average})
    return render(request, 'calculator/droitl1s2.html')
    