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
        TDana1 = float(request.POST.get('TDana1'))
        alg1 = float(request.POST.get('alg1'))
        TDalg1 = float(request.POST.get('TDalg1'))
        algo1 = float(request.POST.get('algo1'))
        TDalgo1 = float(request.POST.get('TDalgo1'))
        TPalgo1 = float(request.POST.get('TPalgo1'))
        sm1 = float(request.POST.get('sm1'))
        TDsm1 = float(request.POST.get('TDsm1'))
        phy1 = float(request.POST.get('phy1'))
        TDphy1 = float(request.POST.get('TDphy1'))
        tseee = float(request.POST.get('tseee'))
        le = float(request.POST.get('le'))
        
        # Perform calculations or any desired actions
        total = ((ana1*0.6)+(TDana1*0.4))*4 + ((alg1*0.6)+(TDalg1*0.4))*3 + ((algo1*0.6)+(TDalgo1*0.2)+(TPalgo1*0.2))*4 + ((sm1*0.6)+(TDsm1*0.4))*3 + ((phy1*0.6)+(TDphy1*0.4))*2 + tseee + le
        average = total / 18
        average = round(average, 2)

        # Render the result page or pass the average to the template context
        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/mis1.html')

def mis2(request):
    if request.method == 'POST':
        ana2 = float(request.POST.get('ana2'))
        TDana2 = float(request.POST.get('TDana2'))
        alg2 = float(request.POST.get('alg2'))
        TDalg2 = float(request.POST.get('TDalg2'))
        algo2 = float(request.POST.get('algo2'))
        TDalgo2 = float(request.POST.get('TDalgo2'))
        TPalgo2 = float(request.POST.get('TPalgo2'))
        sm2 = float(request.POST.get('sm2'))
        TDsm2 = float(request.POST.get('TDsm2'))
        phy2 = float(request.POST.get('phy2'))
        TDphy2 = float(request.POST.get('TDphy2'))
        tic = float(request.POST.get('tic'))
        ipsd = float(request.POST.get('ipsd'))
        TDipsd = float(request.POST.get('TDipsd'))
        oppm = float(request.POST.get('oppm'))
        TPoppm = float(request.POST.get('TPoppm'))
        
        # Perform calculations or any desired actions
        total = ((ana2*0.6)+(TDana2*0.4))*4 + ((alg2*0.6)+(TDalg2*0.4))*2 + ((algo2*0.6)+(TDalgo2*0.2)+(TPalgo2*0.2))*2 + ((sm2*0.6)+(TDsm2*0.4))*2 + ((phy2*0.6)+(TDphy2*0.4))*2 + tic + ((ipsd*0.6)+(TDipsd*0.4))*2 + ((oppm*0.6)+(TPoppm*0.4))*1
        average = total / 16
        average = round(average, 2)

        # Render the result page or pass the average to the template context
        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/mis2.html')

def universite(request):
    return render(request, 'calculator/universite.html')
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
        les_metier = float(request.POST.get('exam-metier'))

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
        les_metier = float(request.POST.get('exam-metier'))

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


def RTelecomeM(request):
    # Logic for the bar page
    # You can perform any necessary operations or retrieve data for this page
    return render(request, 'calculator/RTelecomeM.html')


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

def RTelecomeM2(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-reseaux'))
        td_module1 = float(request.POST.get('TD-reseaux'))
        exam_module2 = float(request.POST.get('exam-cryptographie'))
        td_module2 = float(request.POST.get('TD-cryptographie'))
        exam_module3 = float(request.POST.get('exam-video'))
        td_module3 = float(request.POST.get('TD-video'))
        exam_module4 = float(request.POST.get('exam-technologies'))
        td_module4 = float(request.POST.get('TD-technologies'))
        tp_module1 = float(request.POST.get('TP-reseaux'))
        tp_module2 = float(request.POST.get('TP-cryptographie'))
        tp_module3 = float(request.POST.get('TP-technologies'))
        exam_module5 = float(request.POST.get('exam-television'))
        td_module5 = float(request.POST.get('TD-television'))
        exam_module6 = float(request.POST.get('exam-panier1'))
        exam_module7 = float(request.POST.get('exam-panier2'))
        exam_module8 = float(request.POST.get('exam-recherche'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Réseaux sans fils et réseaux mobiles
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Cryptographie et Sécurité Réseaux
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Vidéo et Audio sur IP
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Technologies du Web
        module5 = (exam_module5 * 0.6 + td_module5 * 0.4) * 2  # Calculation for Télévision numérique
        module6 = exam_module6 * 1  # Calculation for Panier au choix
        module7 = exam_module7 * 1  # Calculation for Panier au choix
        module8 = exam_module8 * 1  # Calculation for Recherche documentaire et conception de mémoire

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module3
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/RTelecomeM2.html')


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

def GE(request):
    return render(request, 'calculator/GE.html')
def auto(request):
    return render(request, 'calculator/auto.html')
def autol2(request):
    return render(request, 'calculator/autol2.html')

def autol2s1(request):
    if request.method== 'POST':
        exam_math3 = float(request.POST.get('exam-math3'))
        td_math3 = float(request.POST.get('TD-math3'))
        exam_onde=float(request.POST.get('exam-onde'))
        td_onde=float(request.POST.get('TD-onde'))
        exam_ele=float(request.POST.get('exam-ele'))
        td_ele=float(request.POST.get('TD-ele'))
        exam_eleth=float(request.POST.get('exam-eleth'))
        td_eleth=float(request.POST.get('TD-eleth'))
        exam_proba=float(request.POST.get('exam-proba'))
        td_proba=float(request.POST.get('TD-proba'))
        exam_info3=float(request.POST.get('exam-info3'))
        tp_ele=float(request.POST.get('TP-ele'))
        tp_onde=float(request.POST.get('TP-onde'))
        exam_etat=float(request.POST.get('exam-etat'))
        exam_energie=float(request.POST.get('exam-energie'))
        exam_anglais=float(request.POST.get('exam-anglais'))   

        math3 = (exam_math3 * 0.6 + td_math3 * 0.4)*3 # Calculation for math3 field
        onde = (exam_onde * 0.6 + td_onde * 0.4)*2  # Calculation for onde field
        ele = (exam_ele * 0.6 + td_ele * 0.4)*2  # Calculation for ele field
        eleth = (exam_eleth * 0.6 + td_eleth * 0.4)*2  # Calculation for eleth field
        proba = (exam_proba * 0.6 + td_proba * 0.4)*2  # Calculation for proba field
        info3 = exam_info3 * 1  # Calculation for info3 field
        tpele = tp_ele * 1  # Calculation for tpele field
        tponde = tp_onde * 1  # Calculation for tponde field
        etat = exam_etat * 1  # Calculation for etat field
        energie = exam_energie * 1  # Calculation for energie field
        anglais = exam_anglais * 1  # Calculation for anglais field

        # Perform further calculations based on the retrieved values
        total = math3 + onde + ele + eleth + proba + info3 + tpele + tponde + etat + energie + anglais
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/autol2s1.html')

def autol2s2(request):
    if request.method== 'POST':
        exam_systemes = float(request.POST.get('exam-systemes'))
        td_systemes = float(request.POST.get('TD-systemes'))
        exam_logique=float(request.POST.get('exam-logique'))
        td_logique=float(request.POST.get('TD-logique'))
        exam_methodes=float(request.POST.get('exam-methodes'))
        td_methodes=float(request.POST.get('TD-methodes'))
        exam_theorie=float(request.POST.get('exam-theorie'))
        td_theorie=float(request.POST.get('TD-theorie'))
        exam_mesures=float(request.POST.get('exam-mesures'))
        td_mesures=float(request.POST.get('TD-mesures'))
        exam_architecture=float(request.POST.get('exam-architecture'))
        tp_systemes=float(request.POST.get('TP-systemes'))
        tp_logique=float(request.POST.get('TP-logique'))
        tp_methodes=float(request.POST.get('TP-methodes'))
        exam_securite=float(request.POST.get('exam-securite'))
        exam_techniques=float(request.POST.get('exam-techniques'))   

        math3 = (exam_systemes * 0.6 + td_systemes * 0.4)*3 # Calculation for math3 field
        onde = (exam_logique * 0.6 + td_logique * 0.4)*2  # Calculation for onde field
        ele = (exam_methodes * 0.6 + td_methodes * 0.4)*2  # Calculation for ele field
        eleth = (exam_theorie * 0.6 + td_theorie * 0.4)*2  # Calculation for eleth field
        proba = (exam_mesures * 0.6 + td_mesures * 0.4)*2  # Calculation for proba field
        info3 = exam_architecture * 1  # Calculation for info3 field
        tpele = tp_systemes * 1  # Calculation for tpele field
        tponde = tp_logique * 1  # Calculation for tponde field
        etat = tp_methodes * 1  # Calculation for etat field
        energie = exam_securite * 1  # Calculation for energie field
        anglais = exam_techniques * 1  # Calculation for anglais field

        # Perform further calculations based on the retrieved values
        total = math3 + onde + ele + eleth + proba + info3 + tpele + tponde + etat + energie + anglais
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/autol2s2.html')
def autol3(request):
    return render(request, 'calculator/autol3.html')

def autol3s1(request):
    if request.method== 'POST':
        exam_commande = float(request.POST.get('exam-commande'))
        td_commande = float(request.POST.get('TD-commande'))
        exam_electronique=float(request.POST.get('exam-electronique'))
        td_electronique=float(request.POST.get('TD-electronique'))
        exam_microprocesseurs=float(request.POST.get('exam-microprocesseurs'))
        td_microprocesseurs=float(request.POST.get('TD-microprocesseurs'))
        exam_programmation=float(request.POST.get('exam-programmation'))
        tp_commande=float(request.POST.get('TP-commande'))
        tp_electronique=float(request.POST.get('TP-electronique'))
        tp_modelisation=float(request.POST.get('TP-modelisation'))
        tp_microprocesseurs=float(request.POST.get('TP-microprocesseurs'))
        tp_programmation=float(request.POST.get('TP-programmation'))
        exam_modelisation=float(request.POST.get('exam-modelisation'))
        exam_normes=float(request.POST.get('exam-normes'))
        exam_securite=float(request.POST.get('exam-energie'))
        exam_anglais=float(request.POST.get('exam-anglais'))   

        math3 = (exam_commande * 0.6 + td_commande * 0.4)*2 # Calculation for math3 field
        onde = (exam_electronique * 0.6 + td_electronique * 0.4)*2  # Calculation for onde field
        ele = (exam_microprocesseurs * 0.6 + td_microprocesseurs * 0.4)*3  # Calculation for ele field
        eleth = (exam_programmation) *1 # Calculation for eleth field
        proba = (tp_commande )*1  # Calculation for proba field
        info3 = tp_electronique * 1  # Calculation for info3 field
        tpele = tp_modelisation * 1  # Calculation for tpele field
        tponde = tp_microprocesseurs * 1  # Calculation for tponde field
        etat = tp_programmation * 1  # Calculation for etat field
        energie = exam_securite * 1  # Calculation for energie field
        anglais = exam_anglais * 1  # Calculation for anglais field
        normes = exam_normes * 1 
        modelisation  = exam_modelisation * 1 
        # Perform further calculations based on the retrieved values
        total = math3 + onde + ele + eleth + proba + info3 + tpele + tponde + etat + energie + anglais + normes + modelisation
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/autol3s1.html')

def autol3s2(request):
    if request.method== 'POST':
        exam_module1 = float(request.POST.get('exam-systemes'))
        td_module1 = float(request.POST.get('TD-systemes'))
        exam_module2=float(request.POST.get('exam-actionneurs'))
        td_module2=float(request.POST.get('TD-actionneurs'))
        exam_module3=float(request.POST.get('exam-automates'))
        td_module3=float(request.POST.get('TD-automates'))
        exam_module4=float(request.POST.get('exam-bus'))
        tp_module1=float(request.POST.get('TP-captures'))
        tp_module2=float(request.POST.get('TP-automates'))
        tp_module3=float(request.POST.get('TP-bus'))
        exam_module9=float(request.POST.get('exam-professionnel'))
        exam_module5=float(request.POST.get('exam-projet'))
        exam_module6=float(request.POST.get('exam-captures'))
        exam_module7=float(request.POST.get('exam-installation'))
        exam_module8=float(request.POST.get('exam-maintenance'))   

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4)*2 # Calculation for math3 field
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4)*2  # Calculation for onde field
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4)*3  # Calculation for ele field
        module4 = (exam_module4) *1 # Calculation for eleth field
        module5 = (exam_module5 )*2  # Calculation for proba field
        module6 = exam_module6 * 1  # Calculation for info3 field
        module7 = exam_module7 * 1  # Calculation for tpele field
        module8 = exam_module8 * 1  # Calculation for tponde field
        module9 = exam_module9 * 1  # Calculation for etat field
        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + module9 + tp_module1 + tp_module2 + tp_module3 
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/autol3s2.html')

def electronique(request):
    return render(request, 'calculator/electronique.html')
def electroniquel2(request):
    return render(request, 'calculator/electroniquel2.html')

def electroniquel2s2(request):
    if request.method== 'POST':
        exam_systemes = float(request.POST.get('exam-systemes'))
        td_systemes = float(request.POST.get('TD-systemes'))
        exam_logique=float(request.POST.get('exam-logique'))
        td_logique=float(request.POST.get('TD-logique'))
        exam_methodes=float(request.POST.get('exam-methodes'))
        td_methodes=float(request.POST.get('TD-methodes'))
        exam_theorie=float(request.POST.get('exam-theorie'))
        td_theorie=float(request.POST.get('TD-theorie'))
        exam_mesures=float(request.POST.get('exam-mesures'))
        td_mesures=float(request.POST.get('TD-mesures'))
        exam_architecture=float(request.POST.get('exam-architecture'))
        tp_systemes=float(request.POST.get('TP-systemes'))
        tp_logique=float(request.POST.get('TP-logique'))
        tp_methodes=float(request.POST.get('TP-methodes'))
        exam_securite=float(request.POST.get('exam-securite'))
        exam_techniques=float(request.POST.get('exam-techniques'))   

        math3 = (exam_systemes * 0.6 + td_systemes * 0.4)*3 # Calculation for math3 field
        onde = (exam_logique * 0.6 + td_logique * 0.4)*2  # Calculation for onde field
        ele = (exam_methodes * 0.6 + td_methodes * 0.4)*2  # Calculation for ele field
        eleth = (exam_theorie * 0.6 + td_theorie * 0.4)*2  # Calculation for eleth field
        proba = (exam_mesures * 0.6 + td_mesures * 0.4)*2  # Calculation for proba field
        info3 = exam_architecture * 1  # Calculation for info3 field
        tpele = tp_systemes * 1  # Calculation for tpele field
        tponde = tp_logique * 1  # Calculation for tponde field
        etat = tp_methodes * 1  # Calculation for etat field
        energie = exam_securite * 1  # Calculation for energie field
        anglais = exam_techniques * 1  # Calculation for anglais field

        # Perform further calculations based on the retrieved values
        total = math3 + onde + ele + eleth + proba + info3 + tpele + tponde + etat + energie + anglais
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/electroniquel2s2.html')

def electroniquel3(request):
    return render(request, 'calculator/electroniquel3.html')

def electroniquel3s1(request):
    if request.method== 'POST':
        exam_fonctions = float(request.POST.get('exam-fonctions'))
        td_fonctions = float(request.POST.get('TD-fonctions'))
        exam_traitement=float(request.POST.get('exam-traitement'))
        td_traitement=float(request.POST.get('TD-traitement'))
        exam_systemes=float(request.POST.get('exam-systemes'))
        td_systemes=float(request.POST.get('TD-systemes'))
        exam_reseaux=float(request.POST.get('exam-reseaux'))
        td_reseaux=float(request.POST.get('TD-reseaux'))
        tp_electronique=float(request.POST.get('TP-travaux'))
        tp_modelisation=float(request.POST.get('TP-systemes'))
        tp_microprocesseurs=float(request.POST.get('TP-fonctions'))
        tp_programmation=float(request.POST.get('TP-signal'))
        exam_travaux=float(request.POST.get('exam-travaux'))
        exam_technologie=float(request.POST.get('exam-technologie'))
        exam_fabrication=float(request.POST.get('exam-fabrication'))
        exam_probagation=float(request.POST.get('exam-probagation'))   

        math3 = (exam_fonctions * 0.6 + td_fonctions * 0.4)*2 # Calculation for math3 field
        onde = (exam_traitement * 0.6 + td_traitement * 0.4)*2  # Calculation for onde field
        ele = (exam_systemes * 0.6 + td_systemes * 0.4)*3  # Calculation for ele field
        eleth = (exam_reseaux *0.6 + td_reseaux *0.4) *2 # Calculation for eleth field
         # Calculation for proba field
          # Calculation for info3 field
        tpele = tp_modelisation * 1  # Calculation for tpele field
        tponde = tp_microprocesseurs * 1  # Calculation for tponde field
        etat = tp_programmation * 1  # Calculation for etat field
        energie = (exam_travaux * 0.6 + tp_electronique * 0.4) * 2  # Calculation for energie field
        anglais = exam_technologie * 1  # Calculation for anglais field
        normes = exam_fabrication * 1 
        modelisation  = exam_probagation * 1 
        # Perform further calculations based on the retrieved values
        total = math3 + onde + ele + eleth  + tpele + tponde + etat + energie + anglais + normes + modelisation
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/electroniquel3s1.html')



def electroniquel3s2(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-captures'))
        td_module1 = float(request.POST.get('TD-captures'))
        exam_module2 = float(request.POST.get('exam-electronique'))
        td_module2 = float(request.POST.get('TD-electronique'))
        exam_module3 = float(request.POST.get('exam-asservissement'))
        td_module3 = float(request.POST.get('TD-asservissement'))
        exam_module4 = float(request.POST.get('exam-impulsions'))
        td_module4 = float(request.POST.get('TD-impulsions'))
        tp_module1 = float(request.POST.get('TP-Asservissements'))
        tp_module2 = float(request.POST.get('TP-Capteurs'))
        tp_module3 = float(request.POST.get('TP-impulsions'))
        exam_module9 = float(request.POST.get('exam-professionnel'))
        exam_module5 = float(request.POST.get('exam-projet'))
        exam_module6 = float(request.POST.get('exam-Dispositifs'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 2  # Calculation for Capteurs et Instrumentation
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Electronique de puissance
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 3  # Calculation for Asservissements continus et Régulation
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Electronique des impulsions
        module5 = exam_module5 * 2  # Calculation for Projet de Fin de Cycle
        module6 = exam_module6 * 2  # Calculation for Dispositifs Optoélectroniques
        module9 = exam_module9 * 1  # 
        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + tp_module1 + tp_module2 + tp_module3 + exam_module9
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/electroniquel3s2.html')

def telecome(request):
    return render(request, 'calculator/telecome.html')

def telecomel2(request):
    return render(request, 'calculator/telecomel2.html')
from django.shortcuts import render

def telecomel2s2(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-telecom'))
        td_module1 = float(request.POST.get('TD-telecom'))
        exam_module2 = float(request.POST.get('exam-logique'))
        td_module2 = float(request.POST.get('TD-logique'))
        exam_module3 = float(request.POST.get('exam-methodes'))
        td_module3 = float(request.POST.get('TD-methodes'))
        exam_module4 = float(request.POST.get('exam-signal'))
        td_module4 = float(request.POST.get('TD-signal'))
        exam_module5 = float(request.POST.get('exam-mesures'))
        td_module5 = float(request.POST.get('TD-mesures'))
        tp_module1 = float(request.POST.get('TP-telecom'))
        tp_module2 = float(request.POST.get('TP-logique'))
        tp_module3 = float(request.POST.get('TP-methodes'))
        exam_module6 = float(request.POST.get('exam-applications'))
        exam_module7 = float(request.POST.get('exam-droit'))
        exam_module8 = float(request.POST.get('exam-techniques'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Télécommunications fondamentale
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Logique combinatoire et séquentielle
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Méthodes numériques
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Théorie du signal
        module5 = (exam_module5 * 0.6 + td_module5 * 0.4) * 2  # Calculation for Mesures électriques et électroniques
        module6 = exam_module6 * 1  # Calculation for Télécommunications et applications
        module7 = exam_module7 * 1  # Calculation for Droit des Télécommunications
        module8 = exam_module8 * 1  # Calculation for Techniques d'expression et de communication

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module3
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/telecomel2s2.html')

def telecomel3(request):
    return render(request, 'calculator/telecomel3.html')


def telecomel3s1(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-analogiques'))
        td_module1 = float(request.POST.get('TD-analogiques'))
        exam_module2 = float(request.POST.get('exam-signal'))
        td_module2 = float(request.POST.get('TD-signal'))
        exam_module3 = float(request.POST.get('exam-ondes'))
        td_module3 = float(request.POST.get('TD-ondes'))
        exam_module4 = float(request.POST.get('exam-systemes'))
        td_module4 = float(request.POST.get('TD-systemes'))
        exam_module5 = float(request.POST.get('exam-calculateurs'))
        tp_module1 = float(request.POST.get('TP-calculateurs'))
        tp_module2 = float(request.POST.get('TP-ondes'))
        tp_module3 = float(request.POST.get('TP-signal'))
        tp_module4 = float(request.POST.get('TP-analogiques'))
        exam_module6 = float(request.POST.get('exam-telephonie'))
        exam_module7 = float(request.POST.get('exam-transmission'))
        exam_module8 = float(request.POST.get('exam-capteurs'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Communications analogiques
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Traitement du signal
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Ondes et Propagation
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Systèmes et réseaux de télécommunication
        module5 = (exam_module5 * 0.6 + tp_module1 * 0.4) * 2  # Calculation for Calculateurs et interfaçage
        module6 = exam_module6 * 1  # Calculation for Téléphonie
        module7 = exam_module7 * 1  # Calculation for Supports de transmission
        module8 = exam_module8 * 1  # Calculation for Capteurs et mesures en télécommunications

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 +  tp_module2 + tp_module3 + tp_module4
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/telecomel3s1.html')



def telecomel3s2(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-numeriques'))
        td_module1 = float(request.POST.get('TD-numeriques'))
        exam_module2 = float(request.POST.get('exam-antennes'))
        td_module2 = float(request.POST.get('TD-antennes'))
        exam_module3 = float(request.POST.get('exam-reseaux'))
        td_module3 = float(request.POST.get('TD-reseaux'))
        exam_module4 = float(request.POST.get('exam-codage'))
        td_module4 = float(request.POST.get('TD-codage'))
        exam_module5 = float(request.POST.get('projet-fin'))
        tp_module1 = float(request.POST.get('TP-numeriques'))
        tp_module2 = float(request.POST.get('TP-antennes'))
        tp_module3 = float(request.POST.get('TP-reseaux'))
        exam_module6 = float(request.POST.get('exam-optoelectronique'))
        exam_module7 = float(request.POST.get('exam-securite'))
        exam_module8 = float(request.POST.get('exam-projetpro'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Communications numériques
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Antennes et Lignes de transmissions
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Réseaux informatiques locaux
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Codage et Théorie de l'information
        module5 = exam_module5 * 2  # Calculation for Projet de Fin de Cycle
        module6 = exam_module6 * 1  # Calculation for Optoélectronique
        module7 = exam_module7 * 1  # Calculation for Sécurité de l'information
        module8 = exam_module8 * 1  # Calculation for Projet professionnel et gestion d'entreprise

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module3
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/telecomel3s2.html')

def biomedical(request):
    return render(request, 'calculator/biomedical.html')

def biomedicall2(request):
    return render(request, 'calculator/biomedicall2.html')


def biomedicall2s2(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-capturs'))
        td_module1 = float(request.POST.get('TD-capturs'))
        exam_module2 = float(request.POST.get('exam-logique'))
        td_module2 = float(request.POST.get('TD-logique'))
        exam_module3 = float(request.POST.get('exam-methodes'))
        td_module3 = float(request.POST.get('TD-methodes'))
        exam_module4 = float(request.POST.get('exam-signal'))
        td_module4 = float(request.POST.get('TD-signal'))
        exam_module5 = float(request.POST.get('exam-mesures'))
        tp_module1 = float(request.POST.get('TP-mesures'))
        tp_module2 = float(request.POST.get('TP-capturs'))
        tp_module3 = float(request.POST.get('TP-logique'))
        tp_module4 = float(request.POST.get('TP-methodes'))
        exam_module6 = float(request.POST.get('exam-anatomie'))
        exam_module7 = float(request.POST.get('exam-imagerie'))
        exam_module8 = float(request.POST.get('exam-techniques'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Capturs de grandeurs physiques
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Logique combinatoire et séquentielle
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Méthodes numériques
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Théorie du signal
        module5 = (exam_module5 )  # Calculation for Mesures électriques et électroniques
        module6 = exam_module6 * 1  # Calculation for anatomie et physiologie
        module7 = exam_module7 * 1  # Calculation for imagerie medicale
        module8 = exam_module8 * 1  # Calculation for Techniques d'expression et de communication

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module3 + tp_module4
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/biomedicall2s2.html')



def biomedicall3(request):
    return render(request, 'calculator/biomedicall3.html')

def biomedicall3s1(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-asservissements'))
        td_module1 = float(request.POST.get('TD-asservissements'))
        exam_module2 = float(request.POST.get('exam-electronique'))
        td_module2 = float(request.POST.get('TD-electronique'))
        exam_module3 = float(request.POST.get('exam-signal'))
        td_module3 = float(request.POST.get('TD-signal'))
        exam_module4 = float(request.POST.get('exam-biophysique'))
        td_module4 = float(request.POST.get('TD-biophysique'))
        tp_module1 = float(request.POST.get('TP-asservissements'))
        tp_module2 = float(request.POST.get('TP-electronique'))
        exam_module5 = float(request.POST.get('exam-informatique'))
        tp_module3 = float(request.POST.get('TP-informatique'))
        tp_module4 = float(request.POST.get('TP-biophysique'))
        exam_module6 = float(request.POST.get('exam-ondes'))
        exam_module7 = float(request.POST.get('exam-terminologie'))
        exam_module8 = float(request.POST.get('exam-maintenance'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Asservissements continus et Régulation
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Electronique générale
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Traitement du signal
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Biophysique
        module5 = (exam_module5 * 0.6 + tp_module3 * 0.4) * 2  # Calculation for Informatique médicale
        module6 = exam_module6 * 1  # Calculation for Ondes et applications en Médical
        module7 = exam_module7 * 1  # Calculation for Terminologie et normes dans le biomédical
        module8 = exam_module8 * 1  # Calculation for Maintenance assistée par ordinateur

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module4
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/biomedicall3s1.html')


def biomedicall3s2(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-acquisition'))
        td_module1 = float(request.POST.get('TD-acquisition'))
        exam_module2 = float(request.POST.get('exam-biomateriaux'))
        td_module2 = float(request.POST.get('TD-biomateriaux'))
        exam_module3 = float(request.POST.get('exam-instrumentation'))
        td_module3 = float(request.POST.get('TD-instrumentation'))
        exam_module4 = float(request.POST.get('exam-traitement'))
        td_module4 = float(request.POST.get('TD-traitement'))
        tp_module1 = float(request.POST.get('TP-acquisition'))
        tp_module2 = float(request.POST.get('TP-instrumentation'))
        exam_module5 = float(request.POST.get('exam-maquettes'))
        exam_module6 = float(request.POST.get('exam-securite'))
        exam_module7 = float(request.POST.get('exam-elements'))
        exam_module8 = float(request.POST.get('exam-projetpro'))
        exam_module9 = float(request.POST.get('projet-fin'))
        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Chaîne d'acquisition numérique
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Biomatériaux
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Instrumentation médicale
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Traitement des signaux physiologiques
        module5 = (exam_module5) * 1  # Calculation for Maquettes
        module6 = exam_module6 * 1  # Calculation for Sécurité des appareils en Biomédical
        module7 = exam_module7 * 1  # Calculation for Éléments des systèmes robotisés
        module8 = exam_module8 * 1  # Calculation for Projet professionnel et gestion d'entreprise
        module9= exam_module9 * 2 # Calculation
        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + module9 + tp_module1 + tp_module2
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/biomedicall3s2.html')


def electrotechnique(request):
    return render(request, 'calculator/electrotechnique.html')

def electrotechniquel2(request):
    return render(request, 'calculator/electrotechniquel2.html')

def electrotechniquel2s2(request):
    if request.method== 'POST':
        exam_systemes = float(request.POST.get('exam-systemes'))
        td_systemes = float(request.POST.get('TD-systemes'))
        exam_logique=float(request.POST.get('exam-logique'))
        td_logique=float(request.POST.get('TD-logique'))
        exam_methodes=float(request.POST.get('exam-methodes'))
        td_methodes=float(request.POST.get('TD-methodes'))
        exam_theorie=float(request.POST.get('exam-theorie'))
        td_theorie=float(request.POST.get('TD-theorie'))
        exam_mesures=float(request.POST.get('exam-mesures'))
        td_mesures=float(request.POST.get('TD-mesures'))
        exam_architecture=float(request.POST.get('exam-architecture'))
        tp_systemes=float(request.POST.get('TP-systemes'))
        tp_logique=float(request.POST.get('TP-logique'))
        tp_methodes=float(request.POST.get('TP-methodes'))
        exam_securite=float(request.POST.get('exam-securite'))
        exam_techniques=float(request.POST.get('exam-techniques'))   

        math3 = (exam_systemes * 0.6 + td_systemes * 0.4)*3 # Calculation for math3 field
        onde = (exam_logique * 0.6 + td_logique * 0.4)*2  # Calculation for onde field
        ele = (exam_methodes * 0.6 + td_methodes * 0.4)*2  # Calculation for ele field
        eleth = (exam_theorie * 0.6 + td_theorie * 0.4)*2  # Calculation for eleth field
        proba = (exam_mesures * 0.6 + td_mesures * 0.4)*2  # Calculation for proba field
        info3 = exam_architecture * 1  # Calculation for info3 field
        tpele = tp_systemes * 1  # Calculation for tpele field
        tponde = tp_logique * 1  # Calculation for tponde field
        etat = tp_methodes * 1  # Calculation for etat field
        energie = exam_securite * 1  # Calculation for energie field
        anglais = exam_techniques * 1  # Calculation for anglais field

        # Perform further calculations based on the retrieved values
        total = math3 + onde + ele + eleth + proba + info3 + tpele + tponde + etat + energie + anglais
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/electrotechniquel2s2.html')
def electrotechniquel3(request):
    return render(request, 'calculator/electrotechniquel3.html')

def electrotechniquel3s1(request):
    if request.method== 'POST':
        exam_fonctions = float(request.POST.get('exam-fonctions'))
        td_fonctions = float(request.POST.get('TD-fonctions'))
        exam_traitement=float(request.POST.get('exam-traitement'))
        td_traitement=float(request.POST.get('TD-traitement'))
        exam_systemes=float(request.POST.get('exam-systemes'))
        td_systemes=float(request.POST.get('TD-systemes'))
        exam_reseaux=float(request.POST.get('exam-reseaux'))
        td_reseaux=float(request.POST.get('TD-reseaux'))
        tp_electronique=float(request.POST.get('TP-travaux'))
        tp_modelisation=float(request.POST.get('TP-systemes'))
        tp_microprocesseurs=float(request.POST.get('TP-fonctions'))
        tp_programmation=float(request.POST.get('TP-signal'))
        exam_travaux=float(request.POST.get('exam-travaux'))
        exam_technologie=float(request.POST.get('exam-technologie'))
        exam_fabrication=float(request.POST.get('exam-fabrication'))
        exam_probagation=float(request.POST.get('exam-probagation'))   

        math3 = (exam_fonctions * 0.6 + td_fonctions * 0.4)*2 # Calculation for math3 field
        onde = (exam_traitement * 0.6 + td_traitement * 0.4)*2  # Calculation for onde field
        ele = (exam_systemes * 0.6 + td_systemes * 0.4)*3  # Calculation for ele field
        eleth = (exam_reseaux *0.6 + td_reseaux *0.4) *2 # Calculation for eleth field
         # Calculation for proba field
          # Calculation for info3 field
        tpele = tp_modelisation * 1  # Calculation for tpele field
        tponde = tp_microprocesseurs * 1  # Calculation for tponde field
        etat = tp_programmation * 1  # Calculation for etat field
        energie = ( exam_travaux  * 0.6 + tp_electronique*0.4) * 2  # Calculation for energie field
        anglais = exam_technologie * 1  # Calculation for anglais field
        normes = exam_fabrication * 1 
        modelisation  = exam_probagation * 1 
        # Perform further calculations based on the retrieved values
        total = math3 + onde + ele + eleth  + tpele + tponde + etat + energie + anglais + normes + modelisation
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/electrotechniquel3s1.html')
def electrotechniquel3s2(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-captures'))
        td_module1 = float(request.POST.get('TD-captures'))
        exam_module2 = float(request.POST.get('exam-electronique'))
        td_module2 = float(request.POST.get('TD-electronique'))
        exam_module3 = float(request.POST.get('exam-asservissement'))
        td_module3 = float(request.POST.get('TD-asservissement'))
        exam_module4 = float(request.POST.get('exam-impulsions'))
        td_module4 = float(request.POST.get('TD-impulsions'))
        tp_module1 = float(request.POST.get('TP-Asservissements'))
        tp_module2 = float(request.POST.get('TP-Capteurs'))
        tp_module3 = float(request.POST.get('TP-impulsions'))
        exam_module7 = float(request.POST.get('exam-professionnel'))
        exam_module5 = float(request.POST.get('exam-projet'))
        exam_module6 = float(request.POST.get('exam-Dispositifs'))
        exam_module8 = float(request.POST.get('exam-maintenance'))
        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 2  # Calculation for Capteurs et Instrumentation
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Electronique de puissance
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 3  # Calculation for Asservissements continus et Régulation
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Electronique des impulsions
        module5 = exam_module5 * 2  # Calculation for Projet de Fin de Cycle
        module6 = exam_module6 * 1  # Calculation for Dispositifs Optoélectroniques
        module7 = exam_module7 * 1 
        module8 = exam_module8 * 1
        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + tp_module1 + tp_module2 + tp_module3 + module7 + module8
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/electrotechniquel3s2.html')

def systemeEmbarquesm(request):
    return render(request, 'calculator/SystemeEmbarquesm.html')

def SysEmbarquesm1s1(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-conception'))
        td_module1 = float(request.POST.get('TD-conception'))
        exam_module2 = float(request.POST.get('exam-electronique'))
        td_module2 = float(request.POST.get('TD-electronique'))
        exam_module3 = float(request.POST.get('exam-traitement'))
        td_module3 = float(request.POST.get('TD-traitement'))
        exam_module4 = float(request.POST.get('exam-systemes'))
        td_module4 = float(request.POST.get('TD-systemes'))
        tp_module1 = float(request.POST.get('TP-electronique'))
        tp_module2 = float(request.POST.get('TP-conception'))
        tp_module3 = float(request.POST.get('TP-traitement'))
        exam_module5 = float(request.POST.get('exam-programmation'))
        td_module5 = float(request.POST.get('TP-programmation'))
        exam_module6 = float(request.POST.get('exam-choix1'))
        exam_module7 = float(request.POST.get('exam-choix2'))
        exam_module8 = float(request.POST.get('exam-angalais'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Réseaux sans fils et réseaux mobiles
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Cryptographie et Sécurité Réseaux
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Vidéo et Audio sur IP
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Technologies du Web
        module5 = (exam_module5 * 0.6 + td_module5 * 0.4) * 2  # Calculation for Télévision numérique
        module6 = exam_module6 * 1  # Calculation for Panier au choix
        module7 = exam_module7 * 1  # Calculation for Panier au choix
        module8 = exam_module8 * 1  # Calculation for Recherche documentaire et conception de mémoire

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module3
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/systemeEmbarquesm1s1.html')


def SysEmbarquesm1s2(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-dsp'))
        td_module1 = float(request.POST.get('TD-dsp'))
        exam_module2 = float(request.POST.get('exam-capteurs'))
        td_module2 = float(request.POST.get('TD-capteurs'))
        exam_module3 = float(request.POST.get('exam-microcontroleurs'))
        td_module3 = float(request.POST.get('TD-microcontroleurs'))
        exam_module4 = float(request.POST.get('exam-reseaux'))
        td_module4 = float(request.POST.get('TD-reseaux'))
        tp_module1 = float(request.POST.get('TP-dsp'))
        tp_module2 = float(request.POST.get('TP-microcontroleurs'))
        tp_module3 = float(request.POST.get('TP-capteurs-reseaux'))
        exam_module5 = float(request.POST.get('exam-etude'))
        td_module5 = float(request.POST.get('TD-etude'))
        exam_module6 = float(request.POST.get('exam-matiere1'))
        exam_module7 = float(request.POST.get('exam-matiere2'))
        exam_module8 = float(request.POST.get('exam-ethique'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Processeurs des signaux numériques (DSP)
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Capteurs intelligents et MEMS
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Systèmes à microcontrôleurs
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Réseaux et communications industriels
        module5 = (exam_module5 * 0.6 + td_module5 * 0.4) * 2  # Calculation for Etude et Réalisation des projets
        module6 = exam_module6 * 1  # Calculation for Matière au choix 1
        module7 = exam_module7 * 1  # Calculation for Matière au choix 2
        module8 = exam_module8 * 1  # Calculation for Ethique, déontologie et propriété intellectuelle

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module3
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/systemeEmbarquesm1s2.html')

from django.shortcuts import render

from django.shortcuts import render

def SysEmbarquesm2s1(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-embarques'))
        td_module1 = float(request.POST.get('TD-embarques'))
        exam_module2 = float(request.POST.get('exam-tempsreel'))
        td_module2 = float(request.POST.get('TD-tempsreel'))
        exam_module3 = float(request.POST.get('exam-automates'))
        td_module3 = float(request.POST.get('TD-automates'))
        exam_module4 = float(request.POST.get('exam-vision'))
        td_module4 = float(request.POST.get('TD-vision'))
        tp_module1 = float(request.POST.get('TP-embarques-tempsreel'))
        tp_module2 = float(request.POST.get('TP-automates'))
        tp_module3 = float(request.POST.get('TP-vision'))
        exam_module5 = float(request.POST.get('exam-java'))
        td_module5 = float(request.POST.get('TD-java'))
        exam_module6 = float(request.POST.get('exam-matiere5'))
        exam_module7 = float(request.POST.get('exam-matiere6'))
        exam_module8 = float(request.POST.get('exam-recherche'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Systèmes embarqués
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Systèmes Temps Réel
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Automates programmables industriels
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Vision artificielle
        module5 = (exam_module5 * 0.6 + td_module5 * 0.4) * 2  # Calculation for Langage JAVA
        module6 = exam_module6 * 1  # Calculation for Matière au choix 5
        module7 = exam_module7 * 1  # Calculation for Matière au choix 6
        module8 = exam_module8 * 1  # Calculation for Recherche documentaire et conception de mémoire

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module3
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/systemeEmbarquesm2s1.html')

def autoinfoindu(request):
    return render(request, 'calculator/autoinfoindu.html')


def autoinfoindum1s1(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-systemes'))
        td_module1 = float(request.POST.get('TD-systemes'))
        exam_module2 = float(request.POST.get('exam-signal'))
        td_module2 = float(request.POST.get('TD-signal'))
        exam_module3 = float(request.POST.get('exam-association'))
        td_module3 = float(request.POST.get('TD-association'))
        exam_module4 = float(request.POST.get('exam-optimisation'))
        td_module4 = float(request.POST.get('TD-optimisation'))
        exam_module5 = float(request.POST.get('exam-reseaux'))
        td_module5 = float(request.POST.get('TD-reseaux'))
        tp_module1 = float(request.POST.get('TP-systemes'))
        tp_module2 = float(request.POST.get('TP-signal-optimisation'))
        tp_module3 = float(request.POST.get('TP-association'))
        exam_module6 = float(request.POST.get('exam-choix1'))
        exam_module7 = float(request.POST.get('exam-choix2'))
        exam_module8 = float(request.POST.get('exam-anglais'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Systèmes Linéaires Multivariables
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Traitement du signal
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Association convertisseurs-machines
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Optimisation
        module5 = (exam_module5 * 0.6 + td_module5 * 0.4) * 2  # Calculation for Réseaux et protocoles de communication industrielle
        module6 = exam_module6 * 1  # Calculation for Panier au choix 1
        module7 = exam_module7 * 1  # Calculation for Panier au choix 2
        module8 = exam_module8 * 1  # Calculation for Anglais technique et terminologie

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module3
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/autoinfoindum1s1.html')


def autoinfoindum1s2(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-non-lineaires'))
        td_module1 = float(request.POST.get('TD-non-lineaires'))
        exam_module2 = float(request.POST.get('exam-embarques'))
        td_module2 = float(request.POST.get('TD-embarques'))
        exam_module3 = float(request.POST.get('exam-api'))
        td_module3 = float(request.POST.get('TD-api'))
        exam_module4 = float(request.POST.get('exam-electronique'))
        td_module4 = float(request.POST.get('TD-electronique'))
        exam_module5 = float(request.POST.get('exam-conception'))
        td_module5 = float(request.POST.get('TD-conception'))
        tp_module1 = float(request.POST.get('TP-non-lineaires'))
        tp_module2 = float(request.POST.get('TP-embarques'))
        tp_module3 = float(request.POST.get('TP-api-electronique'))
        exam_module6 = float(request.POST.get('exam-choix1'))
        exam_module7 = float(request.POST.get('exam-choix2'))
        exam_module8 = float(request.POST.get('exam-ethique'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Systèmes non linéaires
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Systèmes Embarqués et systèmes temps réels
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Programmation avancée des API
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Electronique Appliquée
        module5 = (exam_module5 * 0.6 + td_module5 * 0.4) * 2  # Calculation for Conception orientée objet
        module6 = exam_module6 * 1  # Calculation for Matiere au choix 1
        module7 = exam_module7 * 1  # Calculation for Matiere au choix 2
        module8 = exam_module8 * 1  # Calculation for Ethique, déontologie et propriété intellectuelle

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module3
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/autoinfoindum1s2.html')


def autoinfoindum2s1(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-commande-avancee'))
        td_module1 = float(request.POST.get('TD-commande-avancee'))
        exam_module2 = float(request.POST.get('exam-commande-robots'))
        td_module2 = float(request.POST.get('TD-commande-robots'))
        exam_module3 = float(request.POST.get('exam-evenement-discrets'))
        td_module3 = float(request.POST.get('TD-evenement-discrets'))
        exam_module4 = float(request.POST.get('exam-fpga'))
        td_module4 = float(request.POST.get('TD-fpga'))
        exam_module5 = float(request.POST.get('exam-supervision'))
        td_module5 = float(request.POST.get('TD-supervision'))
        tp_module1 = float(request.POST.get('TP-commande-avancee'))
        tp_module2 = float(request.POST.get('TP-commande-robots'))
        tp_module3 = float(request.POST.get('TP-fpga'))
        exam_module6 = float(request.POST.get('exam-choix1'))
        exam_module7 = float(request.POST.get('exam-choix2'))
        exam_module8 = float(request.POST.get('exam-recherche-documentaire'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Commande avancée
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Commande de robots de manipulation
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Systèmes à évènement discrets
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for FPGA et programmation VHDL
        module5 = (exam_module5 * 0.6 + td_module5 * 0.4) * 2  # Calculation for Supervision industrielle
        module6 = exam_module6 * 1  # Calculation for Matiere au choix 1
        module7 = exam_module7 * 1  # Calculation for Matiere au choix 2
        module8 = exam_module8 * 1  # Calculation for Recherche documentaire et conception de mémoire

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module3
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/autoinfoindum2s1.html')

def machineselectriques(request):
    return render(request, 'calculator/machineselectriques.html')
def machineselectriquesm1s1(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-reseaux-energie'))
        td_module1 = float(request.POST.get('TD-reseaux-energie'))
        exam_module2 = float(request.POST.get('exam-electronique-puissance'))
        td_module2 = float(request.POST.get('TD-electronique-puissance'))
        exam_module3 = float(request.POST.get('exam-machines-electriques'))
        td_module3 = float(request.POST.get('TD-machines-electriques'))
        exam_module4 = float(request.POST.get('exam-methodes-numeriques'))
        td_module4 = float(request.POST.get('TD-methodes-numeriques'))
        tp_module1 = float(request.POST.get('TP-processeurs-controleurs'))
        tp_module2 = float(request.POST.get('TP-reseaux-energie'))
        tp_module3 = float(request.POST.get('TP-electronique-puissance'))
        tp_module4 = float(request.POST.get('TP-methodes-numeriques'))
        tp_module5 = float(request.POST.get('TP-machines-electriques'))
        exam_module5 = float(request.POST.get('exam-choix1'))
        exam_module6 = float(request.POST.get('exam-choix2'))
        exam_module7 = float(request.POST.get('exam-anglais-technique'))
        exam_module8 = float(request.POST.get('processeurs-controleurs'))
        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 2  # Calculation for Réseaux de transport et de distribution d'énergie électrique
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Electronique de puissance avancée
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Machines électriques approfondies
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Méthodes numériques appliquées et optimisation
        module5 = exam_module5 * 1  # Calculation for Matiere au choix 1
        module6 = exam_module6 * 1  # Calculation for Matiere au choix 2
        module7 = exam_module7 * 1  # Calculation for Anglais technique et terminologie
        module8 = exam_module8 * 1  # Calculation for processeurs-controleurs
        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module3 + tp_module4 + tp_module5
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/machineselectriquesm1s1.html')


def machineselectriquesm1s2(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-modelisation-machines'))
        td_module1 = float(request.POST.get('TD-modelisation-machines'))
        exam_module2 = float(request.POST.get('exam-champ-magnetique'))
        td_module2 = float(request.POST.get('TD-champ-magnetique'))
        exam_module3 = float(request.POST.get('exam-asservissements'))
        td_module3 = float(request.POST.get('TD-asservissements'))
        exam_module4 = float(request.POST.get('exam-construction-machines'))
        td_module4 = float(request.POST.get('TD-construction-machines'))
        materiaux_module = float(request.POST.get('materiaux-haute-tension'))
        tp_module1 = float(request.POST.get('TP-modelisation-machines'))
        tp_module2 = float(request.POST.get('TP-asservissements'))
        tp_module3 = float(request.POST.get('TP-champ-magnetique'))
        exam_module5 = float(request.POST.get('exam-association-machines'))
        td_module5 = float(request.POST.get('TD-association-machines'))
        exam_module6 = float(request.POST.get('exam-choix1'))
        exam_module7 = float(request.POST.get('exam-choix2'))
        exam_module8 = float(request.POST.get('exam-ethique'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 2  # Calculation for Modélisation des machines électriques
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Champ magnétique dans les machines électriques
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Asservissements échantillonnés et Régulation numérique
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Construction des machines électriques
        module5 = (exam_module5 * 0.6 + td_module5 * 0.4) * 2  # Calculation for Association machines-convertisseurs
        module6 = exam_module6 * 1  # Calculation for Matiere au choix 1
        module7 = exam_module7 * 1  # Calculation for Matiere au choix 2
        module8 = exam_module8 * 1  # Calculation for Ethique, déontologie et propriété intellectuelle

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + materiaux_module + tp_module1 + tp_module2 + tp_module3
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/machineselectriquesm1s2.html')


def machineselectriquesm2s1(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-machines-speciales'))
        td_module1 = float(request.POST.get('TD-machines-speciales'))
        exam_module2 = float(request.POST.get('exam-regimes-transitoires'))
        td_module2 = float(request.POST.get('TD-regimes-transitoires'))
        conception_module = float(request.POST.get('conception-assistee'))
        identification_module = float(request.POST.get('identification-diagnostic'))
        echauffement_module = float(request.POST.get('echauffement-refroidissement'))
        exam_module3 = float(request.POST.get('exam-commande'))
        td_module3 = float(request.POST.get('TD-commande'))
        tp_module1 = float(request.POST.get('TP-machines-speciales'))
        tp_module2 = float(request.POST.get('TP-regimes-transitoires'))
        tp_module3 = float(request.POST.get('TP-identification-diagnostic'))
        tp_module4 = float(request.POST.get('TP-conception-assistee'))
        tp_module5 = float(request.POST.get('TP-commande'))
        exam_module4 = float(request.POST.get('exam-choix1'))
        exam_module5 = float(request.POST.get('exam-choix2'))
        exam_module6 = float(request.POST.get('exam-recherche-documentaire'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 2  # Calculation for Machines électriques spéciales
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Régimes transitoires des machines électriques
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Commande des machines électriques
        module4 = exam_module4 * 1  # Calculation for Matiere au choix 1
        module5 = exam_module5 * 1  # Calculation for Matiere au choix 2
        module6 = exam_module6 * 1  # Calculation for Recherche documentaire et conception de mémoire

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + conception_module + identification_module + echauffement_module + tp_module1 + tp_module2 + tp_module3 + tp_module4 + tp_module5
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/machineselectriquesm2s1.html')

def instrubiomedical(request):
    return render(request, 'calculator/instrubiomedicalm.html')


def instrubiomedicalm1s1(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-radiobiologie'))
        td_module1 = float(request.POST.get('TD-radiobiologie'))
        exam_module2 = float(request.POST.get('exam-traitement-signaux'))
        td_module2 = float(request.POST.get('TD-traitement-signaux'))
        exam_module3 = float(request.POST.get('exam-fonctions-electronique'))
        td_module3 = float(request.POST.get('TD-fonctions-electronique'))
        exam_module4 = float(request.POST.get('exam-circuits-conditionnement'))
        td_module4 = float(request.POST.get('TD-circuits-conditionnement'))
        exam_module5 = float(request.POST.get('exam-electronique-puissance'))
        td_module5 = float(request.POST.get('TD-electronique-puissance'))
        tp_module1 = float(request.POST.get('TP-fonctions-electronique'))
        tp_module2 = float(request.POST.get('TP-circuits-electronique'))
        tp_module3 = float(request.POST.get('TP-traitement-radiobiologie'))
        exam_module6 = float(request.POST.get('exam-biomateriaux'))
        td_module6 = float(request.POST.get('TP-biomateriaux'))
        exam_module7 = float(request.POST.get('exam-choix1'))
        exam_module8 = float(request.POST.get('exam-choix2'))
        exam_module9 = float(request.POST.get('exam-anglais-technique'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 2  # Calculation for Radiobiologie et radioprotection
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Traitement avancé des signaux physiologiques
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Fonctions principales de l'électronique
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Circuits de conditionnement
        module5 = exam_module5 * 1  # Calculation for Electronique de puissance
        module6 = (exam_module6* 0.6 + td_module6 * 0.4) * 2  # Calculation for Technologies des biomatériaux pour prothèses
        module7 = exam_module7 * 1  # Calculation for Matière au choix 1
        module8 = exam_module8 * 1  # Calculation for Matière au choix 2
        module9 = exam_module9 * 1  # Calculation for Anglais technique et terminologie

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + module9 + tp_module1 + tp_module2 + tp_module3 
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/instrubiomedicalm1s1.html')


def instrubiomedicalm1s2(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-traitement-image-medicale'))
        td_module1 = float(request.POST.get('TD-traitement-image-medicale'))
        exam_module2 = float(request.POST.get('exam-dispositifs-speciaux'))
        td_module2 = float(request.POST.get('TD-dispositifs-speciaux'))
        exam_module3 = float(request.POST.get('exam-rayonnements'))
        td_module3 = float(request.POST.get('TD-rayonnements'))
        exam_module4 = float(request.POST.get('exam-systemes-microcontroleurs'))
        td_module4 = float(request.POST.get('TD-systemes-microcontroleurs'))
        tp_module1 = float(request.POST.get('TP-traitement-image-medicale'))
        tp_module2 = float(request.POST.get('TP-dispositifs-rayonnements'))
        tp_module3 = float(request.POST.get('TP-systemes-microcontroleurs'))
        exam_module5 = float(request.POST.get('exam-langage-programmation'))
        td_module5 = float(request.POST.get('TD-langage-programmation'))
        exam_module6 = float(request.POST.get('exam-matiere-choix1'))
        exam_module7 = float(request.POST.get('exam-matiere-choix2'))
        exam_module8 = float(request.POST.get('exam-ethique-deontologie'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 3  # Calculation for Traitement de l’image médicale
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Dispositifs spéciaux pour l’imagerie médicale
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Rayonnements non ionisants
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Systèmes à microcontrôleurs
        module5 = (exam_module5 * 0.6 + td_module5 * 0.4) * 2  # Calculation for Langage de programmation
        module6 = exam_module6 * 1  # Calculation for Matière au choix 1
        module7 = exam_module7 * 1  # Calculation for Matière au choix 2
        module8 = exam_module8 * 1  # Calculation for Ethique, déontologie et propriété intellectuelle

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + tp_module1 + tp_module2 + tp_module3
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/instrubiomedicalm1s2.html')

from django.shortcuts import render

def instrubiomedicalm2s1(request):
    if request.method == 'POST':
        exam_module1 = float(request.POST.get('exam-instrumentation-exploration'))
        td_module1 = float(request.POST.get('TD-instrumentation-exploration'))
        exam_module2 = float(request.POST.get('exam-instrumentation-imagerie'))
        td_module2 = float(request.POST.get('TD-instrumentation-imagerie'))
        exam_module3 = float(request.POST.get('exam-biocapteurs'))
        td_module3 = float(request.POST.get('TD-biocapteurs'))
        exam_module4 = float(request.POST.get('exam-systemes-embarques'))
        td_module4 = float(request.POST.get('TD-systemes-embarques'))
        exam_module5 = float(request.POST.get('exam-modelisation-simulation'))
        tp_module1 = float(request.POST.get('TP-instrumentation-biocapteurs'))
        tp_module2 = float(request.POST.get('TP-systemes-embarques'))
        tp_module3 = float(request.POST.get('TP-simulation-systemes'))
        exam_module6 = float(request.POST.get('exam-gestion-projets'))
        td_module6 = float(request.POST.get('TD-gestion-projets'))
        exam_module7 = float(request.POST.get('exam-matiere-choix1'))
        exam_module8 = float(request.POST.get('exam-matiere-choix2'))
        exam_module9 = float(request.POST.get('exam-recherche-documentaire'))

        module1 = (exam_module1 * 0.6 + td_module1 * 0.4) * 2  # Calculation for Instrumentation pour l’exploration fonctionnelle
        module2 = (exam_module2 * 0.6 + td_module2 * 0.4) * 2  # Calculation for Instrumentation de l’imagerie médicale
        module3 = (exam_module3 * 0.6 + td_module3 * 0.4) * 2  # Calculation for Biocapteurs
        module4 = (exam_module4 * 0.6 + td_module4 * 0.4) * 2  # Calculation for Systèmes embarqués biomédicaux
        module5 = exam_module5 * 1  # Calculation for Modélisation et simulation des systèmes biomédicaux
        module6 = (exam_module6 * 0.6 + td_module6 * 0.4) * 2  # Calculation for Gestion de projets pour les systèmes de santé
        module7 = exam_module7 * 1  # Calculation for Matière au choix 1
        module8 = exam_module8 * 1  # Calculation for Matière au choix 2
        module9 = exam_module9 * 1  # Calculation for Recherche documentaire et conception de mémoire

        # Perform further calculations based on the retrieved values
        total = module1 + module2 + module3 + module4 + module5 + module6 + module7 + module8 + module9 + tp_module1 + tp_module2 + tp_module3
        average = total / 17
        average = round(average, 2)

        return render(request, 'calculator/result_page.html', {'average': average})

    return render(request, 'calculator/instrubiomedicalm2s1.html')























from django.http import HttpResponse
def sitemap_xml(request):
    # Generate your sitemap XML content
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset
      xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
<!-- created with Free Online Sitemap Generator www.xml-sitemaps.com -->

<url>
  <loc>https://moyennedz.vercel.app/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>1.00</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/fr/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.80</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/bac_ar/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.80</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/universite/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.80</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/bac/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.64</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/math/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.64</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/MathThechnique/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.64</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/Gestion/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.64</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/science/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.64</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/philo/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.64</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/LesLangues/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.64</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/st/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.64</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/RtelecomeM/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.64</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/mi/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.64</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/droitl1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.64</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/st1er/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.51</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/ge/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.51</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/telecomeM1S1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.51</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/telecomeM1S2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.51</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/mis1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.51</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/mis2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.51</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/droitl1s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.51</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/droitl1s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.51</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/sts1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.41</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/sts2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.41</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/telecome/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.41</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/electronique/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.41</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/auto/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.41</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/electrotechnique/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.41</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/biomedical/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.41</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/telecomel2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/telecomel3/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/RTelecomeM2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/electroniquel2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/electroniquel3/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/SystemeEmbarquesm/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/autol2</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/autol3/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/autoinfoindu/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/electrotechniquel2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/electrotechniquel3/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/machineselectriques/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/biomedicall2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/biomedicall3/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/instrubiomedical/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.33</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/l2s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/telecomel2s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/telecomel3s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/telecomel3s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/electroniquel2s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/electroniquel3s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/electroniquel3s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/SysEmbarquesm1s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/SysEmbarquesm1s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/SysEmbarquesm2s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/autol2s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/autol3s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/autol3s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/autoinfoindum1s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/autoinfoindum1s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/autoinfoindum2s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/electrotechniquel2s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/electrotechniquel3s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/electrotechniquel3s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/machineselectriquesm1s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/machineselectriquesm1s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/machineselectriquesm2s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/biomedicall2s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/biomedicall3s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/biomedicall3s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/instrubiomedicalm1s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/instrubiomedicalm1s2/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>
<url>
  <loc>https://moyennedz.vercel.app/instrubiomedicalm2s1/</loc>
  <lastmod>2023-07-12T18:56:43+00:00</lastmod>
  <priority>0.26</priority>
</url>

</urlset>
    """



    return HttpResponse(xml_content, content_type='text/xml')


def robots_txt(request):
    content = render(request, 'robots.txt', content_type='text/plain')
    return HttpResponse(content)
