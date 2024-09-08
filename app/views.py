from django.shortcuts import render, redirect
from django.contrib.auth import login
from . import models
import jdatetime
from io import BytesIO
import xlsxwriter
from django.http import HttpResponse
from .gvars import form1_keys, form2_keys, form3_keys
import os
from dotenv import load_dotenv

# loading .env file
load_dotenv()
PASSWORD = os.getenv('PASSWORD')

def form1_json(req, customer_id=None, id=None, date_of_submit=None):
    new_data = {
        "id" : id,
        "customer_id" : customer_id,
        "date_of_submit" : date_of_submit,
        "undefined" : req.POST.get('undefined'),
        "CIC" : req.POST.get('CIC'),
        "hospitalupn" : req.POST.get('hospitalupn'),
        "patientuic" : req.POST.get('patientuic'),
        "hsctdate1" : req.POST.get('hsctdate1'),
        "ebmtcodecic" : req.POST.get('ebmtcodecic'),
        "contactperson" : req.POST.get('contactperson'),
        "hospital" : req.POST.get('hospital'),
        "unit" : req.POST.get('unit'),
        "email" : req.POST.get('email'),
        "dateofthisreport" : req.POST.get('dateofthisreport'),
        "firsttransplantforthispatient" : req.POST.get('firsttransplantforthispatient'),
        "patientfollowingnationalinternationalstudytrial" : req.POST.get('patientfollowingnationalinternationalstudytrial'),
        "patientfollowingnationalinternationalstudytrial_text" : req.POST.get('patientfollowingnationalinternationalstudytrial_text'),
        "hospitaluniquepatientnumberorcodeupn" : req.POST.get('hospitaluniquepatientnumberorcodeupn'),
        "initials" : req.POST.get('initials'),
        "dateofbirth" : req.POST.get('dateofbirth'),
        "sex" : req.POST.get('sex'),
        "dateofinitialdiagnosis" : req.POST.get('dateofinitialdiagnosis'),
        "acute_leukaemia" : req.POST.get('acute_leukaemia'),
        "acute_myelogenous_leukaemia__aml__related_precursor_neoplasms" : req.POST.get('acute_myelogenous_leukaemia__aml__related_precursor_neoplasms'),
        "precursor_lymphoid_neoplasms__old_all__" : req.POST.get('precursor_lymphoid_neoplasms__old_all__'),
        "trmnosal" : req.POST.get('trmnosal'),
        "chronic_leukaemia" : req.POST.get('chronic_leukaemia'),
        "chronic_myeloid_leukaemia__cml_" : req.POST.get('chronic_myeloid_leukaemia__cml_'),
        "chronic_lymphocytic_leukaemia__cll_" : req.POST.get('chronic_lymphocytic_leukaemia__cll_'),
        "lymphoma" : req.POST.get('lymphoma'),
        "non_hodgkin" : req.POST.get('non_hodgkin'),
        "hodgkin_s_disease" : req.POST.get('hodgkin_s_disease'),
        "myelomaplasmacelldisorder" : req.POST.get('myelomaplasmacelldisorder'),
        "solidtumour" : req.POST.get('solidtumour'),
        "myelodysplasticsyndromesmyeloproliferativeneoplasm" : req.POST.get('myelodysplasticsyndromesmyeloproliferativeneoplasm'),
        "mds" : req.POST.get('mds'),
        "mdsmpn" : req.POST.get('mdsmpn'),
        "myeloproliferativeneoplasm" : req.POST.get('myeloproliferativeneoplasm'),
        "bonemarrowfailureincludingaplasticanaemia" : req.POST.get('bonemarrowfailureincludingaplasticanaemia'),
        "inheriteddisorders" : req.POST.get('inheriteddisorders'),
        "primaryimmunedeficiencies" : req.POST.get('primaryimmunedeficiencies'),
        "metabolicdisorders" : req.POST.get('metabolicdisorders'),
        "histiocyticdisorders" : req.POST.get('histiocyticdisorders'),
        "autoimmunedisease" : req.POST.get('autoimmunedisease'),
        "juvenileidiopathicarthritis" : req.POST.get('juvenileidiopathicarthritis'),
        "multiplesclerosis" : req.POST.get('multiplesclerosis'),
        "systemiclupus" : req.POST.get('systemiclupus'),
        "systemicsclerosis" : req.POST.get('systemicsclerosis'),
        "haemoglobinopathy" : req.POST.get('haemoglobinopathy'),
        "otherdiagnosisspecify" : req.POST.get('otherdiagnosisspecify'),
        "systemused" : req.POST.get('systemused'),
        "score" : req.POST.get('score'),
        "weightkg" : req.POST.get('weightkg'),
        "heightcm" : req.POST.get('heightcm'),
        "wasthereanycoexistingdiseaseororganimpairmentattimeofpatient886" : req.POST.get('wasthereanycoexistingdiseaseororganimpairmentattimeofpatient886'),
        "indicatetype" : req.POST.get('indicatetype'),
        "reatedatanytimepointinthepatientspasthistoryexcludingnonmela138" : req.POST.get('reatedatanytimepointinthepatientspasthistoryexcludingnonmela138'),
        "crohnsdiseaseorulcerativecoliti" : req.POST.get('crohnsdiseaseorulcerativecoliti'),
        "slerapolymyositismixedctdorpolymyalgiarheumatica" : req.POST.get('slerapolymyositismixedctdorpolymyalgiarheumatica'),
        "requiringtreatmentwithinsulinororalhypoglycaemicsbutnotdietalone" : req.POST.get('requiringtreatmentwithinsulinororalhypoglycaemicsbutnotdietalone'),
        "serumcreatininemgdlormollondialysisorpriorrenaltransplantation" : req.POST.get('serumcreatininemgdlormollondialysisorpriorrenaltransplantation'),
        "chronichepatitisbilirubinbetweenupperlimitnormalulnandxtheul151" : req.POST.get('chronichepatitisbilirubinbetweenupperlimitnormalulnandxtheul151'),
        "livercirrhosisbilirubingreaterthanulnorastaltgreaterthanuln" : req.POST.get('livercirrhosisbilirubingreaterthanulnorastaltgreaterthanuln'),
        "atrialfibrillationorfluttersicksinussyndromeorventriculararr129" : req.POST.get('atrialfibrillationorfluttersicksinussyndromeorventriculararr129'),
        "coronaryarterydiseasecongestiveheartfailuremyocardialinfarct473" : req.POST.get('coronaryarterydiseasecongestiveheartfailuremyocardialinfarct473'),
        "transientischemicattackorcerebrovascularaccident" : req.POST.get('transientischemicattackorcerebrovascularaccident'),
        "exceptmitralvalveprolapse" : req.POST.get('exceptmitralvalveprolapse'),
        "dlcoandorfevordyspnoeaonslightactivity" : req.POST.get('dlcoandorfevordyspnoeaonslightactivity'),
        "dlcoandorfevordyspnoeaatrestorrequiringoxygen" : req.POST.get('dlcoandorfevordyspnoeaatrestorrequiringoxygen'),
        "patientswithabodymassindexkgm" : req.POST.get('patientswithabodymassindexkgm'),
        "requiringtreatment" : req.POST.get('requiringtreatment'),
        "depressionoranxietyrequiringpsychiatricconsultationortreatment" : req.POST.get('depressionoranxietyrequiringpsychiatricconsultationortreatment'),
        "werethereanyothermajorclinicalabnormalitiespriortotheprepara312" : req.POST.get('werethereanyothermajorclinicalabnormalitiespriortotheprepara312'),
        "autologous" : req.POST.get('autologous'),
        "sourceofthestemcells" : req.POST.get('sourceofthestemcells'),
        "sourceofthestemcells_other" : req.POST.get('sourceofthestemcells_other'),
        "otherthanforrbcremovalorvolumereduction" : req.POST.get('otherthanforrbcremovalorvolumereduction'),
        "geneticmanipulationofthegraft" : req.POST.get('geneticmanipulationofthegraft'),
        "allogeneic" : req.POST.get('allogeneic'),
        "patientcmvstatus" : req.POST.get('patientcmvstatus'),
        "multipledonorsincludingmultiplecbunits" : req.POST.get('multipledonorsincludingmultiplecbunits'),
        "numberofdonors_1" : req.POST.get('numberofdonors_1'),
        "hlamatchedotherrelative" : req.POST.get('hlamatchedotherrelative'),
        "donor_1_degreeofmismatch" : req.POST.get('donor_1_degreeofmismatch'),
        "donoridgivenbythecentre12" : req.POST.get('donoridgivenbythecentre12'),
        "antigenic_a" : req.POST.get('antigenic_a'),
        "antigenic_b" : req.POST.get('antigenic_b'),
        "antigenic_c" : req.POST.get('antigenic_c'),
        "antigenic_drb1" : req.POST.get('antigenic_drb1'),
        "antigenic_dqb1" : req.POST.get('antigenic_dqb1'),
        "antigenic_dpb1" : req.POST.get('antigenic_dpb1'),
        "allelic_a" : req.POST.get('allelic_a'),
        "allelic_b" : req.POST.get('allelic_b'),
        "allelic_c" : req.POST.get('allelic_c'),
        "allelic_drb1" : req.POST.get('allelic_drb1'),
        "allelic_dqb1" : req.POST.get('allelic_dqb1'),
        "allelic_dpb1" : req.POST.get('allelic_dpb1'),
        "unrelateddonor" : req.POST.get('unrelateddonor'),
        "ioncodeofthedonorregistryorcbbank1" : req.POST.get('ioncodeofthedonorregistryorcbbank1'),
        "bmdwcodeofthedonorregistryorcbbank" : req.POST.get('bmdwcodeofthedonorregistryorcbbank'),
        "nameofdonorregistrycbbank15" : req.POST.get('nameofdonorregistrycbbank15'),
        "donorcentrename" : req.POST.get('donorcentrename'),
        "donor12" : req.POST.get('donor12'),
        "patientidgivenbythedonorregistryorthecbbanklistedabove" : req.POST.get('patientidgivenbythedonorregistryorthecbbanklistedabove'),
        "dateofbirth2" : req.POST.get('dateofbirth2'),
        "donor1sex" : req.POST.get("donor1sex"),
        "donorcmvstatus1" : req.POST.get('donorcmvstatus1'),
        "didthisdonorprovidemorethanonestemcellproduct" : req.POST.get('didthisdonorprovidemorethanonestemcellproduct'),
        "sourceofstemcellsford1p1" : req.POST.get('sourceofstemcellsford1p1'),
        "sourceofstemcellsford1p1_other" : req.POST.get('sourceofstemcellsford1p1_other'),
        "otherthanforrbcremovalorvolumereductiond1p1" : req.POST.get('otherthanforrbcremovalorvolumereductiond1p1'),
        "otherthanforrbcremovalorvolumereductiond1p1_neg" : req.POST.get('otherthanforrbcremovalorvolumereductiond1p1_neg'),
        "otherthanforrbcremovalorvolumereductiond1p1_negy" : req.POST.get('otherthanforrbcremovalorvolumereductiond1p1_negy'),
        "otherthanforrbcremovalorvolumereductiond1p1_negyo" : req.POST.get('otherthanforrbcremovalorvolumereductiond1p1_negyo'),
        "positived1p1" : req.POST.get('positived1p1'),
        "cdenrichmentd1p1" : req.POST.get('cdenrichmentd1p1'),
        "geneticmanipulationd1p" : req.POST.get('geneticmanipulationd1p'),
        "sourceofstemcellsford1p2" : req.POST.get('sourceofstemcellsford1p2'),
        "sourceofstemcellsford1p2_other" : req.POST.get('sourceofstemcellsford1p2_other'),
        "otherthanforrbcremovalorvolumereductiond1p2" : req.POST.get('otherthanforrbcremovalorvolumereductiond1p2'),
        "otherthanforrbcremovalorvolumereductiond1p2_neg" : req.POST.get('otherthanforrbcremovalorvolumereductiond1p2_neg'),
        "otherthanforrbcremovalorvolumereductiond1p2_negy" : req.POST.get('otherthanforrbcremovalorvolumereductiond1p2_negy'),
        "otherthanforrbcremovalorvolumereductiond1p2_negyo" : req.POST.get('otherthanforrbcremovalorvolumereductiond1p2_negyo'),
        "positived1p2" : req.POST.get('positived1p2'),
        "geneticmanipulationd1p2" : req.POST.get('geneticmanipulationd1p2'),
        "hlamatchtype" : req.POST.get('hlamatchtype'),
        "hlamatchtype_degreeofmismatch" : req.POST.get('hlamatchtype_degreeofmismatch'),
        "donoridgivenbythecentre" : req.POST.get('donoridgivenbythecentre'),
        "donor2_a" : req.POST.get('donor2_a'),
        "donor2_b" : req.POST.get('donor2_b'),
        "donor2_c" : req.POST.get('donor2_c'),
        "donor2_drb1" : req.POST.get('donor2_drb1'),
        "donor2_dqb1" : req.POST.get('donor2_dqb1'),
        "donor2_dpb1" : req.POST.get('donor2_dpb1'),
        "donor_2_nrelateddonor" : req.POST.get('donor_2_nrelateddonor'),
        "ioncodeofthedonorregistryorcbbank" : req.POST.get('ioncodeofthedonorregistryorcbbank'),
        "bmdwcodeofthedonorregistryorcbbank4343" : req.POST.get('bmdwcodeofthedonorregistryorcbbank4343'),
        "nameofdonorregistrycbbank" : req.POST.get('nameofdonorregistrycbbank'),
        "donorcentrename16" : req.POST.get('donorcentrename16'),
        "donor" : req.POST.get('donor'),
        "patient" : req.POST.get('patient'),
        "donor2sex" : req.POST.get('donor2sex'),
        "donorcmvstatus2" : req.POST.get('donorcmvstatus2'),
        "dateofbirth3" : req.POST.get('dateofbirth3'),
        "sourceofstemcellsford2p1" : req.POST.get('sourceofstemcellsford2p1'),
        "sourceofstemcellsford2p1_other" : req.POST.get('sourceofstemcellsford2p1_other'),
        "otherthanforrbcremovalorvolumereductiond2p1" : req.POST.get('otherthanforrbcremovalorvolumereductiond2p1'),
        "otherthanforrbcremovalorvolumereductiond2p1_neg" : req.POST.get('otherthanforrbcremovalorvolumereductiond2p1_neg'),
        "otherthanforrbcremovalorvolumereductiond2p1_negy" : req.POST.get('otherthanforrbcremovalorvolumereductiond2p1_negy'),
        "otherthanforrbcremovalorvolumereductiond2p1_negyo" : req.POST.get('otherthanforrbcremovalorvolumereductiond2p1_negyo'),
        "positived2p1" : req.POST.get('positived2p1'),
        "geneticmanipulationd2p1" : req.POST.get('geneticmanipulationd2p1'),
        "sourceofstemcellsford2p2" : req.POST.get('sourceofstemcellsford2p2'),
        "sourceofstemcellsford2p2o" : req.POST.get('sourceofstemcellsford2p2o'),
        "otherthanforrbcremovalorvolumereductiond2p2" : req.POST.get('otherthanforrbcremovalorvolumereductiond2p2'),
        "otherthanforrbcremovalorvolumereductiond2p2_neg" : req.POST.get('otherthanforrbcremovalorvolumereductiond2p2_neg'),
        "otherthanforrbcremovalorvolumereductiond2p2_negy" : req.POST.get('otherthanforrbcremovalorvolumereductiond2p2_negy'),
        "otherthanforrbcremovalorvolumereductiond2p2_negyo" : req.POST.get('otherthanforrbcremovalorvolumereductiond2p2_negyo'),
        "positived2p2" : req.POST.get('positived2p2'),
        "geneticmanipulationd2p2" : req.POST.get('geneticmanipulationd2p2'),
        "lastdateassessed" : req.POST.get('lastdateassessed'),
        "iftypeoflasthsctbeforethisone" : req.POST.get('iftypeoflasthsctbeforethisone'),
        "ifandallograftwasthesamedonorusedforallpriorandcurrenthscts" : req.POST.get('ifandallograftwasthesamedonorusedforallpriorandcurrenthscts'),
        "ifwaslasthsctpeformedatanotherinstitution" : req.POST.get('ifwaslasthsctpeformedatanotherinstitution'),
        "ifwaslasthsctpeformedatanotherinstitutioncic" : req.POST.get('ifwaslasthsctpeformedatanotherinstitutioncic'),
        "nameoftheinstitution" : req.POST.get('nameoftheinstitution'),
        "city" : req.POST.get('city'),
        "hsctpartofaplannedmultiplesequentialgraftprotocolprogram" : req.POST.get('hsctpartofaplannedmultiplesequentialgraftprotocolprogram'),
        "preparativeregimengiven" : req.POST.get('preparativeregimengiven'),
        "wasthisintendedtobemyeloablativealloonly" : req.POST.get('wasthisintendedtobemyeloablativealloonly'),
        "wasthisintendedtobemyeloablativealloonlyno" : req.POST.get('wasthisintendedtobemyeloablativealloonlyno'),
        "wasthisintendedtobemyeloablativealloonlynoo" : req.POST.get('wasthisintendedtobemyeloablativealloonlynoo'),
        "drugs" : req.POST.get('drugs'),
        "araccytarabine" : req.POST.get('araccytarabine'),
        "araccytarabine_unit" : req.POST.get('araccytarabine_unit'),
        "carboplatin" : req.POST.get('carboplatin'),
        "carboplatin_unit" : req.POST.get('carboplatin_unit'),
        "algatgalsats" : req.POST.get('algatgalsats'),
        "algatgalsatsanimalorigin" : req.POST.get('algatgalsatsanimalorigin'),
        "animalorigin_other" : req.POST.get('animalorigin_other'),
        "algatgalsatsunit" : req.POST.get('algatgalsatsunit'),
        "bleomycin" : req.POST.get('bleomycin'),
        "bleomycin_unit" : req.POST.get('bleomycin_unit'),
        "Busulfan" : req.POST.get('Busulfan'),
        "busulfan_type" : req.POST.get('busulfan_type'),
        "busulfan_unit" : req.POST.get('busulfan_unit'),
        "cisplatin" : req.POST.get('cisplatin'),
        "cisplatin_unit" : req.POST.get('cisplatin_unit'),
        "clofarabine" : req.POST.get('clofarabine'),
        "clofarabine_unit" : req.POST.get('clofarabine_unit'),
        "corticosteroids" : req.POST.get('corticosteroids'),
        "corticosteroids_unit" : req.POST.get('corticosteroids_unit'),
        "cyclophosphamide" : req.POST.get('cyclophosphamide'),
        "cyclophosphamide_unit" : req.POST.get('cyclophosphamide_unit'),
        "daunorubicin" : req.POST.get('daunorubicin'),
        "daunorubicin_unit" : req.POST.get('daunorubicin_unit'),
        "doxorubicinadriamycine" : req.POST.get('doxorubicinadriamycine'),
        "doxorubicinadriamycine_unit" : req.POST.get('doxorubicinadriamycine_unit'),
        "epirubicin" : req.POST.get('epirubicin'),
        "epirubicin_unit" : req.POST.get('epirubicin_unit'),
        "etoposidevp" : req.POST.get('etoposidevp'),
        "etoposidevp_unit" : req.POST.get('etoposidevp_unit'),
        "fludarabine" : req.POST.get('fludarabine'),
        "fludarabine_unit" : req.POST.get('fludarabine_unit'),
        "gemtuzumab" : req.POST.get('gemtuzumab'),
        "gemtuzumab_unit" : req.POST.get('gemtuzumab_unit'),
        "idarubicin" : req.POST.get('idarubicin'),
        "idarubicin_unit" : req.POST.get('idarubicin_unit'),
        "ifosfamide" : req.POST.get('ifosfamide'),
        "ifosfamide_unit" : req.POST.get('ifosfamide_unit'),
        "imatinibmesylate" : req.POST.get('imatinibmesylate'),
        "imatinibmesylate_unit" : req.POST.get('imatinibmesylate_unit'),
        "melphalan" : req.POST.get('melphalan'),
        "melphalan_unit" : req.POST.get('melphalan_unit'),
        "mitoxantrone" : req.POST.get('mitoxantrone'),
        "mitoxantrone_unit" : req.POST.get('mitoxantrone_unit'),
        "paclitaxel" : req.POST.get('paclitaxel'),
        "paclitaxel_unit" : req.POST.get('paclitaxel_unit'),
        "rituximabmabtheraanticd" : req.POST.get('rituximabmabtheraanticd'),
        "rituximabmabtheraanticd_unit" : req.POST.get('rituximabmabtheraanticd_unit'),
        "teniposide" : req.POST.get('teniposide'),
        "teniposide_unit" : req.POST.get('teniposide_unit'),
        "teniposide_unit_unit" : req.POST.get('teniposide_unit_unit'),
        "thiotepa" : req.POST.get('thiotepa'),
        "thiotepa_unit" : req.POST.get('thiotepa_unit'),
        "treosulphan" : req.POST.get('treosulphan'),
        "treosulphan_unit" : req.POST.get('treosulphan_unit'),
        "zevalinradiolabelledmoab" : req.POST.get('zevalinradiolabelledmoab'),
        "zevalinradiolabelledmoab_unit" : req.POST.get('zevalinradiolabelledmoab_unit'),
        "otherradiolabelledmoab" : req.POST.get('otherradiolabelledmoab'),
        "otherradiolabelledmoab_unit" : req.POST.get('otherradiolabelledmoab_unit'),
        "othermoabspecify" : req.POST.get('othermoabspecify'),
        "othermoabspecify_unit" : req.POST.get('othermoabspecify_unit'),
        "otherspecifyrt" : req.POST.get('otherspecifyrt'),
        "otherspecifyrt_unit" : req.POST.get('otherspecifyrt_unit'),
        "totalbodyirradiation" : req.POST.get('totalbodyirradiation'),
        "totalprescribedradiationdoseasperprotocoltbi" : req.POST.get('totalprescribedradiationdoseasperprotocoltbi'),
        "tbirnumberoffractions" : req.POST.get('tbirnumberoffractions'),
        "tbirnumberoffractionsover" : req.POST.get('tbirnumberoffractionsover'),
        "tlitnitai" : req.POST.get('tlitnitai'),
        "totalprescribedradiationdoseasperprotocoltli" : req.POST.get('totalprescribedradiationdoseasperprotocoltli'),
        "gvhdprophylaxisorpreventivetreatmentallograftsonly" : req.POST.get('gvhdprophylaxisorpreventivetreatmentallograftsonly'),
        "drugsimmunosuppressivechemo" : req.POST.get('drugsimmunosuppressivechemo'),
        "drugsimmunosuppressivechemoo" : req.POST.get('drugsimmunosuppressivechemoo'),
        "drugsimmunosuppressivechemooo" : req.POST.get('drugsimmunosuppressivechemooo'),
        "drugsimmunosuppressivechemooos" : req.POST.get('drugsimmunosuppressivechemooos'),
        "survivalstatusondateofhsct" : req.POST.get('survivalstatusondateofhsct'),
        "maincauseofdeathcheckonlyonemaincause" : req.POST.get('maincauseofdeathcheckonlyonemaincause'),
        "maincauseofdeathcheckonlyonemaincauseother" : req.POST.get('maincauseofdeathcheckonlyonemaincauseother'),
        "contributorycauseofdeath" : req.POST.get('contributorycauseofdeath'),
        "contributorycauseofdeathinfection" : req.POST.get('contributorycauseofdeathinfection'),
        "contributorycauseofdeathotherspecify" : req.POST.get('contributorycauseofdeathotherspecify'),
        "dateofinitialdiagnosis1" : req.POST.get('dateofinitialdiagnosis1'),
        "amlwithrecurrentgeneticabnormalities" : req.POST.get('amlwithrecurrentgeneticabnormalities'),
        "amlwithrecurrentgeneticabnormalitiesny" : req.POST.get('amlwithrecurrentgeneticabnormalitiesny'),
        "amlnototherwisecategorisednos" : req.POST.get('amlnototherwisecategorisednos'),
        "didtherecipienthaveapredisposingcondition" : req.POST.get('didtherecipienthaveapredisposingcondition'),
        "didtherecipienthaveapredisposingconditiony" : req.POST.get('didtherecipienthaveapredisposingconditiony'),
        "isthisadonorcellleukaemia1" : req.POST.get('isthisadonorcellleukaemia1'),
        "chromosomeanalysisatdiagnosis1" : req.POST.get('chromosomeanalysisatdiagnosis1'),
        "chromosomeanalysisatdiagnosis1iack" : req.POST.get('chromosomeanalysisatdiagnosis1iack'),
        "chromosomeanalysisatdiagnosis1imk" : req.POST.get('chromosomeanalysisatdiagnosis1imk'),
        "youcantranscribethecompletekaryotype1" : req.POST.get('youcantranscribethecompletekaryotype1'),
        "t1517" : req.POST.get('t1517'),
        "t821" : req.POST.get('t821'),
        "inv16t1616" : req.POST.get('inv16t1616'),
        "11q23ant" : req.POST.get('11q23ant'),
        "t911" : req.POST.get('t911'),
        "t1119a" : req.POST.get('t1119a'),
        "t1011a" : req.POST.get('t1011a'),
        "t611a" : req.POST.get('t611a'),
        "3q26evatbb" : req.POST.get('3q26evatbb'),
        "anb5typ" : req.POST.get('anb5typ'),
        "del5qaa" : req.POST.get('del5qaa'),
        "mnomn5" : req.POST.get('mnomn5'),
        "add5qaas" : req.POST.get('add5qaas'),
        "otabnpss" : req.POST.get('otabnpss'),
        "abn7typ09" : req.POST.get('abn7typ09'),
        "del7q22" : req.POST.get('del7q22'),
        "mnspp3232" : req.POST.get('mnspp3232'),
        "add7q222" : req.POST.get('add7q222'),
        "wererertwrtert" : req.POST.get('wererertwrtert'),
        "wrgklwe4545" : req.POST.get('wrgklwe4545'),
        "t15rtyuytr67617" : req.POST.get('t15rtyuytr67617'),
        "we56cvowe" : req.POST.get('we56cvowe'),
        "iutriuytmnb" : req.POST.get('iutriuytmnb'),
        "rrewuiyruieuruei4444" : req.POST.get('rrewuiyruieuruei4444'),
        "molecularmarkeranalysisatdiagnosis3434" : req.POST.get('molecularmarkeranalysisatdiagnosis3434'),
        "rtweertereawryrtwrewrtolpo" : req.POST.get('rtweertereawryrtwrewrtolpo'),
        "asf56mmyutrrwewty" : req.POST.get('asf56mmyutrrwewty'),
        "qw545mmjerwerty" : req.POST.get('qw545mmjerwerty'),
        "evaluatedatleastonce44444" : req.POST.get('evaluatedatleastonce44444'),
        "notevaluatedsdsdsd" : req.POST.get('notevaluatedsdsdsd'),
        "cdgufooligir75" : req.POST.get('cdgufooligir75'),
        "peiqccnmdj7743" : req.POST.get('peiqccnmdj7743'),
        "ppowr5648nvjj" : req.POST.get('ppowr5648nvjj'),
        "nvmvjjdhd55544" : req.POST.get('nvmvjjdhd55544'),
        "jsdjerhuaueiwurh65" : req.POST.get('jsdjerhuaueiwurh65'),
        "ityouiiortuqwetqetrwr87" : req.POST.get('ityouiiortuqwetqetrwr87'),
        "cnvcmvuyeieuroweiow85" : req.POST.get('cnvcmvuyeieuroweiow85'),
        "oopweiweimcmxckkeiwe7775" : req.POST.get('oopweiweimcmxckkeiwe7775'),
        "asasasllfiryru66654545" : req.POST.get('asasasllfiryru66654545'),
        "asertuytmnbvc4434" : req.POST.get('asertuytmnbvc4434'),
        "wertcvnbhfsddf6679676" : req.POST.get('wertcvnbhfsddf6679676'),
        "xcxrrjkldwenncmx6655" : req.POST.get('xcxrrjkldwenncmx6655'),
        "asffdlsklfirieij775" : req.POST.get('asffdlsklfirieij775'),
        "zxzxldfkehruwetyiwuer755675" : req.POST.get('zxzxldfkehruwetyiwuer755675'),
        "awricxf6678" : req.POST.get('awricxf6678'),
        "wertkjhg450000" : req.POST.get('wertkjhg450000'),
        "asteeroiumn7767" : req.POST.get('asteeroiumn7767'),
        "asreernbvc54557" : req.POST.get('asreernbvc54557'),
        "zxcvbuytrre1123469" : req.POST.get('zxcvbuytrre1123469'),
        "involvementatdiagnosisbm1" : req.POST.get('involvementatdiagnosisbm1'),
        "involvementatdiagnosiscns1" : req.POST.get('involvementatdiagnosiscns1'),
        "involvementatdiagnosisto1" : req.POST.get('involvementatdiagnosisto1'),
        "involvementatdiagnosispoth1" : req.POST.get('involvementatdiagnosispoth1'),
        "involvementatdiagnosispotht1" : req.POST.get('involvementatdiagnosispotht1'),
        "dateofthishsct3434" : req.POST.get('dateofthishsct3434'),
        "primaryinductionfailure900000" : req.POST.get('primaryinductionfailure900000'),
        "primaryinductionfailure900000v" : req.POST.get('primaryinductionfailure900000v'),
        "primaryinductionfailure900000vu" : req.POST.get('primaryinductionfailure900000vu'),
        "primaryinductionfailure900000vq" : req.POST.get('primaryinductionfailure900000vq'),
        "primaryinductionfailure900000oo" : req.POST.get('primaryinductionfailure900000oo'),
        "dateoflastrelapsebeforethishsctwerwerwer" : req.POST.get('dateoflastrelapsebeforethishsctwerwerwer'),
        "dateofinitialdiagnosi657654" : req.POST.get('dateofinitialdiagnosi657654'),
        "blymphoblasticleukaemialymphomaoldprecursorbcellall" : req.POST.get('blymphoblasticleukaemialymphomaoldprecursorbcellall'),
        "blymphoblasticleukaemialymphomaoldprecursorbcellallo" : req.POST.get('blymphoblasticleukaemialymphomaoldprecursorbcellallo'),
        "secondaryorigin345345345345" : req.POST.get('secondaryorigin345345345345'),
        "isthisadonorcellleukaemia333" : req.POST.get('isthisadonorcellleukaemia333'),
        "chromosomeanalysisatdiagnosisallmethodsincludingfish12" : req.POST.get('chromosomeanalysisatdiagnosisallmethodsincludingfish12'),
        "ifabnormal2234234" : req.POST.get('ifabnormal2234234'),
        "youcantranscribethecompletekaryotype" : req.POST.get('youcantranscribethecompletekaryotype'),
        "t1777" : req.POST.get('t1777'),
        "t1778" : req.POST.get('t1778'),
        "t1779" : req.POST.get('t1779'),
        "t1779o" : req.POST.get('t1779o'),
        "t1780" : req.POST.get('t1780'),
        "t1781" : req.POST.get('t1781'),
        "t1782" : req.POST.get('t1782'),
        "t1783" : req.POST.get('t1783'),
        "t1785ot" : req.POST.get('t1785ot'),
        "t1784" : req.POST.get('t1784'),
        "t1785" : req.POST.get('t1785'),
        "t1785o" : req.POST.get('t1785o'),
        "t1785on" : req.POST.get('t1785on'),
        "t1786" : req.POST.get('t1786'),
        "t1787" : req.POST.get('t1787'),
        "t1788" : req.POST.get('t1788'),
        "t1789" : req.POST.get('t1789'),
        "t1789m" : req.POST.get('t1789m'),
        "t1790" : req.POST.get('t1790'),
        "t1790on" : req.POST.get('t1790on'),
        "t1791" : req.POST.get('t1791'),
        "t1792" : req.POST.get('t1792'),
        "t1793" : req.POST.get('t1793'),
        "t1794" : req.POST.get('t1794'),
        "t1795" : req.POST.get('t1795'),
        "markeranalysis232323" : req.POST.get('markeranalysis232323'),
        "bcrablmolecularproductoftqq12" : req.POST.get('bcrablmolecularproductoftqq12'),
        "bcrablmolecularproductoftqq123" : req.POST.get('bcrablmolecularproductoftqq123'),
        "bcrablmolecularproductoftqq124" : req.POST.get('bcrablmolecularproductoftqq124'),
        "bcrablmolecularproductoftqq125" : req.POST.get('bcrablmolecularproductoftqq125'),
        "bcrablmolecularproductoftqq126" : req.POST.get('bcrablmolecularproductoftqq126'),
        "bcrablmolecularproductoftqq127" : req.POST.get('bcrablmolecularproductoftqq127'),
        "bcrablmolecularproductoftqq128" : req.POST.get('bcrablmolecularproductoftqq128'),
        "bcrablmolecularproductoftqq129" : req.POST.get('bcrablmolecularproductoftqq129'),
        "bcrablmolecularproductoftqq120" : req.POST.get('bcrablmolecularproductoftqq120'),
        "bcrablmolecularproductoftqq1211" : req.POST.get('bcrablmolecularproductoftqq1211'),
        "bcrablmolecularproductoftqq1222" : req.POST.get('bcrablmolecularproductoftqq1222'),
        "bcrablmolecularproductoftqq1225o" : req.POST.get('bcrablmolecularproductoftqq1225o'),
        "bcrablmolecularproductoftqq1233" : req.POST.get('bcrablmolecularproductoftqq1233'),
        "dateofthishsct" : req.POST.get('dateofthishsct'),
        "dateofthishsctopts" : req.POST.get('dateofthishsctopts'),
        "dateofthishsctoptscn" : req.POST.get('dateofthishsctoptscn'),
        "dateofthishsctoptsccr" : req.POST.get('dateofthishsctoptsccr'),
        "dateofthishsctoptscmr" : req.POST.get('dateofthishsctoptscmr'),
        "dateofthishsctoptsrn" : req.POST.get('dateofthishsctoptsrn'),
        "dateofinitialdiagnosis22" : req.POST.get('dateofinitialdiagnosis22'),
        "acuteundifferentiatedleukaemia" : req.POST.get('acuteundifferentiatedleukaemia'),
        "acuteundifferentiatedleukaemianos" : req.POST.get('acuteundifferentiatedleukaemianos'),
        "acuteundifferentiatedleukaemiao" : req.POST.get('acuteundifferentiatedleukaemiao'),
        "relatedtopriorexposuretotherapeuticdrugsorradiation" : req.POST.get('relatedtopriorexposuretotherapeuticdrugsorradiation'),
        "isthisadonorcellleukaemia" : req.POST.get('isthisadonorcellleukaemia'),
        "dateofthishsct456" : req.POST.get('dateofthishsct456'),
        "statusstatusathsct1" : req.POST.get('statusstatusathsct1'),
        "statusstatusathsct1o" : req.POST.get('statusstatusathsct1o'),
        "statusstatusathsct1oc" : req.POST.get('statusstatusathsct1oc'),
        "statusstatusathsct1om" : req.POST.get('statusstatusathsct1om'),
        "dateofinitialdiagnosis33" : req.POST.get('dateofinitialdiagnosis33'),
        "hsctdate2" : req.POST.get('hsctdate2'),
        "chromosomeanalysisallmethodsincludingfish" : req.POST.get('chromosomeanalysisallmethodsincludingfish'),
        "chroTrisomy12" : req.POST.get('chroTrisomy12'),
        "chrodel13q14" : req.POST.get('chrodel13q14'),
        "chroDel11q2223" : req.POST.get('chroDel11q2223'),
        "chrodel17q" : req.POST.get('chrodel17q'),
        "chroosot" : req.POST.get('chroosot'),
        "chroos" : req.POST.get('chroos'),
        "molecularmarkers333" : req.POST.get('molecularmarkers333'),
        "treatmentprehsctprimarytreatment" : req.POST.get('treatmentprehsctprimarytreatment'),
        "treatmentprehsctprimarytreatmentdate" : req.POST.get('treatmentprehsctprimarytreatmentdate'),
        "regtreatmentprehsctprimarytreatment" : req.POST.get('regtreatmentprehsctprimarytreatment'),
        "dsregtreatmentprehsctprimarytreatment" : req.POST.get('dsregtreatmentprehsctprimarytreatment'),
        "deregtreatmentprehsctprimarytreatment" : req.POST.get('deregtreatmentprehsctprimarytreatment'),
        "dateofthishsct124" : req.POST.get('dateofthishsct124'),
        "statusytre6u67645r" : req.POST.get('statusytre6u67645r'),
        "statusytre6u67645ro" : req.POST.get('statusytre6u67645ro'),
        "dateofthishsct8564" : req.POST.get('dateofthishsct8564'),
        "prolymphocyticleukaemiaspllother" : req.POST.get('prolymphocyticleukaemiaspllother'),
        "prolymphocyticleukaemiaspllotherp" : req.POST.get('prolymphocyticleukaemiaspllotherp'),
        "prolymphocyticleukaemiaspllothert" : req.POST.get('prolymphocyticleukaemiaspllothert'),
        "chromosomalanalysisallmethodsincludingfish" : req.POST.get('chromosomalanalysisallmethodsincludingfish'),
        "invtqq444" : req.POST.get('invtqq444'),
        "del14q12" : req.POST.get('del14q12'),
        "t1114q23q11" : req.POST.get('t1114q23q11'),
        "t714q35q321" : req.POST.get('t714q35q321'),
        "tx14q35q11" : req.POST.get('tx14q35q11'),
        "idix8p11" : req.POST.get('idix8p11'),
        "ots33343434t" : req.POST.get('ots33343434t'),
        "ots33343434" : req.POST.get('ots33343434'),
        "tcellpllonlyimmunophenotypingcd4" : req.POST.get('tcellpllonlyimmunophenotypingcd4'),
        "tcellpllonlyimmunophenotypingcd8" : req.POST.get('tcellpllonlyimmunophenotypingcd8'),
        "lymphocytecoun444" : req.POST.get('lymphocytecoun444'),
        "dateofthishsct116" : req.POST.get('dateofthishsct116'),
        "dateofthishsctstatus888" : req.POST.get('dateofthishsctstatus888'),
        "dateofthishsct1978" : req.POST.get('dateofthishsct1978'),
        "bcellneoplasms" : req.POST.get('bcellneoplasms'),
        "bcellneoplasmsspl" : req.POST.get('bcellneoplasmsspl'),
        "bcellneoplasmslymp" : req.POST.get('bcellneoplasmslymp'),
        "internationalprognosticscoringsystemforwaldenstrmsmacroglobu147" : req.POST.get('internationalprognosticscoringsystemforwaldenstrmsmacroglobu147'),
        "grading" : req.POST.get('grading'),
        "prognosticscoreflipi" : req.POST.get('prognosticscoreflipi'),
        "prognosticscoremipi" : req.POST.get('prognosticscoremipi'),
        "kiproliferationindex" : req.POST.get('kiproliferationindex'),
        "bcellneoplasmsdiff4" : req.POST.get('bcellneoplasmsdiff4'),
        "bcellneoplasmsot" : req.POST.get('bcellneoplasmsot'),
        "transformedfromanothertypeoflymphoma" : req.POST.get('transformedfromanothertypeoflymphoma'),
        "transformedfromanothertypeoflymphomay" : req.POST.get('transformedfromanothertypeoflymphomay'),
        "indicatethetypeoftheoriginallymphoma" : req.POST.get('indicatethetypeoftheoriginallymphoma'),
        "dateofinitialdiagnosis44" : req.POST.get('dateofinitialdiagnosis44'),
        "maturetcellnkcellneoplasms43" : req.POST.get('maturetcellnkcellneoplasms43'),
        "maturetcellnkcellneoplasms43iscleortc" : req.POST.get('maturetcellnkcellneoplasms43iscleortc'),
        "maturetcellnkcellneoplasms43o" : req.POST.get('maturetcellnkcellneoplasms43o'),
        "maturetcellnkcellneoplasms43itentialpr" : req.POST.get('maturetcellnkcellneoplasms43itentialpr'),
        "dateofinitialdiagnosis55" : req.POST.get('dateofinitialdiagnosis55'),
        "classificationinp" : req.POST.get('classificationinp'),
        "classificationinpot" : req.POST.get('classificationinpot'),
        "treatmentprehscta" : req.POST.get('treatmentprehscta'),
        "treatmentprehsctayes" : req.POST.get('treatmentprehsctayes'),
        "drugsgiven_antibodies" : req.POST.get('drugsgiven_antibodies'),
        "drugsgiven_antibodies_other" : req.POST.get('drugsgiven_antibodies_other'),
        "drugsgiven_radioimmunotherapy" : req.POST.get('drugsgiven_radioimmunotherapy'),
        "relapseprogressionunderthisdruga" : req.POST.get('relapseprogressionunderthisdruga'),
        "relapseprogressionunderthisdrugbc" : req.POST.get('relapseprogressionunderthisdrugbc'),
        "relapseprogressionunderthisdrugb" : req.POST.get('relapseprogressionunderthisdrugb'),
        "relapseprogressionunderthisdrug" : req.POST.get('relapseprogressionunderthisdrug'),
        "relapseprogressionunderthisdrugc" : req.POST.get('relapseprogressionunderthisdrugc'),
        "relapseprogressionunderthisdrugd" : req.POST.get('relapseprogressionunderthisdrugd'),
        "relapseprogressionunderthisdruge" : req.POST.get('relapseprogressionunderthisdruge'),
        "relapseprogressionunderthisdrugf" : req.POST.get('relapseprogressionunderthisdrugf'),
        "drugsgiven_specificinhibitors" : req.POST.get('drugsgiven_specificinhibitors'),
        "drugsgiven_specificinhibitors_other" : req.POST.get('drugsgiven_specificinhibitors_other'),
        "drugsgiven_other" : req.POST.get('drugsgiven_other'),
        "drugsgiven_other_other" : req.POST.get('drugsgiven_other_other'),
        "dateofthishsct12706" : req.POST.get('dateofthishsct12706'),
        "chromosomeanalysisatanytimebeforehsct" : req.POST.get('chromosomeanalysisatanytimebeforehsct'),
        "chromosomeanalysisatanytimebeforehsctadel" : req.POST.get('chromosomeanalysisatanytimebeforehsctadel'),
        "chromosomeanalysisatanytimebeforehsctat28" : req.POST.get('chromosomeanalysisatanytimebeforehsctat28'),
        "chromosomeanalysisatanytimebeforehsctat814" : req.POST.get('chromosomeanalysisatanytimebeforehsctat814'),
        "chromosomeanalysisatanytimebeforehsctat822" : req.POST.get('chromosomeanalysisatanytimebeforehsctat822'),
        "chromosomeanalysisatanytimebeforehsctat1418" : req.POST.get('chromosomeanalysisatanytimebeforehsctat1418'),
        "chromosomeanalysisatanytimebeforehsctatmycrea" : req.POST.get('chromosomeanalysisatanytimebeforehsctatmycrea'),
        "chromosomeanalysisatanytimebeforehsctatbcl2rea" : req.POST.get('chromosomeanalysisatanytimebeforehsctatbcl2rea'),
        "chromosomeanalysisatanytimebeforehsctatbcl6a" : req.POST.get('chromosomeanalysisatanytimebeforehsctatbcl6a'),
        "mantlecelllymphomas" : req.POST.get('mantlecelllymphomas'),
        "burkittlymphomaorintermediatem" : req.POST.get('burkittlymphomaorintermediatem'),
        "intermediatedlcblburkittlymphomabcl" : req.POST.get('intermediatedlcblburkittlymphomabcl'),
        "bclrearrangement3434" : req.POST.get('bclrearrangement3434'),
        "olecularmarkeranalysesiepcratanytimebeforehsct" : req.POST.get('olecularmarkeranalysesiepcratanytimebeforehsct'),
        "mantlecelllymphomatp53" : req.POST.get('mantlecelllymphomatp53'),
        "burkittlymphomaorintermediatedlcblburkittlymphoma" : req.POST.get('burkittlymphomaorintermediatedlcblburkittlymphoma'),
        "intermediatedlcblburkittlymphoma454" : req.POST.get('intermediatedlcblburkittlymphoma454'),
        "bclrearrangement6" : req.POST.get('bclrearrangement6'),
        "dateofthishsct11478" : req.POST.get('dateofthishsct11478'),
        "numberofpriorlinesoftreatment656" : req.POST.get('numberofpriorlinesoftreatment656'),
        "numberofpriorlinesoftreatment6563more" : req.POST.get('numberofpriorlinesoftreatment6563more'),
        "ctscandone_90" : req.POST.get('ctscandone_90'),
        "ctscandone_90pet" : req.POST.get('ctscandone_90pet'),
        "ctscandone_status_list" : req.POST.get('ctscandone_status_list'),
        "ctscandone_status_list_complete" : req.POST.get('ctscandone_status_list_complete'),
        "wasthispatientrefractorytoanylineofchemotherapybeforethishsc56" : req.POST.get('wasthispatientrefractorytoanylineofchemotherapybeforethishsc56'),
        "numberofcompletecrcruachievedbythepatientpriortothishsct2" : req.POST.get('numberofcompletecrcruachievedbythepatientpriortothishsct2'),
        "numberofpartialremissionsprachievedbythepatientpriortothishsc6" : req.POST.get('numberofpartialremissionsprachievedbythepatientpriortothishsc6'),
        "dateofinitialdiagnosis66" : req.POST.get('dateofinitialdiagnosis66'),
        "whoclassificationatdiagnosis34" : req.POST.get('whoclassificationatdiagnosis34'),
        "therapyrelatedmds4545" : req.POST.get('therapyrelatedmds4545'),
        "isthisadonorcellleukaemia555" : req.POST.get('isthisadonorcellleukaemia555'),
        "chromosomeanalysisatdiagnosisallmethodsincludingfis5" : req.POST.get('chromosomeanalysisatdiagnosisallmethodsincludingfis5'),
        "complexkariotype343re" : req.POST.get('complexkariotype343re'),
        "youcantranscribethecompletekaryotype3" : req.POST.get('youcantranscribethecompletekaryotype3'),
        "delyy_chmi" : req.POST.get('delyy_chmi'),
        "abn5type_chmi" : req.POST.get('abn5type_chmi'),
        "del5q_chmi" : req.POST.get('del5q_chmi'),
        "otherabnspecify" : req.POST.get('otherabnspecify'),
        "atherabn5_chmi" : req.POST.get('atherabn5_chmi'),
        "del20q_chmi" : req.POST.get('del20q_chmi'),
        "abn7p_chmi" : req.POST.get('abn7p_chmi'),
        "del7q_chmi" : req.POST.get('del7q_chmi'),
        "otherabn7_chmi" : req.POST.get('otherabn7_chmi'),
        "abn3p_chmi" : req.POST.get('abn3p_chmi'),
        "inv3_chmi" : req.POST.get('inv3_chmi'),
        "t3q3q_chmi" : req.POST.get('t3q3q_chmi'),
        "del3q_chmi" : req.POST.get('del3q_chmi'),
        "otherabn3e_chmi" : req.POST.get('otherabn3e_chmi'),
        "del11q_chmi" : req.POST.get('del11q_chmi'),
        "trisomy8_chmi" : req.POST.get('trisomy8_chmi'),
        "trisomy19_chmi" : req.POST.get('trisomy19_chmi'),
        "i17g_chmi" : req.POST.get('i17g_chmi'),
        "others_chmi" : req.POST.get('others_chmi'),
        "molecularmarkersatdiagnosisw" : req.POST.get('molecularmarkersatdiagnosisw'),
        "molecularmarkersatdiagnosis" : req.POST.get('molecularmarkersatdiagnosis'),
        "dateofthishsct1197654" : req.POST.get('dateofthishsct1197654'),
        "whoclassificationathsct56" : req.POST.get('whoclassificationathsct56'),
        "treatedwithchemotherapy5345345" : req.POST.get('treatedwithchemotherapy5345345'),
        "treatedwithchemotherapy5345345cr" : req.POST.get('treatedwithchemotherapy5345345cr'),
        "treatedwithchemotherapy5345345rpl" : req.POST.get('treatedwithchemotherapy5345345rpl'),
        "dateofinitialdiagnosis77" : req.POST.get('dateofinitialdiagnosis77'),
        "classification43434" : req.POST.get('classification43434'),
        "therapyrelatedmdsmpn3866" : req.POST.get('therapyrelatedmdsmpn3866'),
        "chromosomeanalysisatdiagnosis444" : req.POST.get('chromosomeanalysisatdiagnosis444'),
        "complexkariotypeifun" : req.POST.get('complexkariotypeifun'),
        "youcantranscribethecompletekaryotype334" : req.POST.get('youcantranscribethecompletekaryotype334'),
        "indicatebelowthoseabnormalities_abn" : req.POST.get('indicatebelowthoseabnormalities_abn'),
        "indicatebelowthoseabnormalities_abno" : req.POST.get('indicatebelowthoseabnormalities_abno'),
        "indicatebelowthoseabnormalities_abn5" : req.POST.get('indicatebelowthoseabnormalities_abn5'),
        "indicatebelowthoseabnormalities_abn5o" : req.POST.get('indicatebelowthoseabnormalities_abn5o'),
        "indicatebelowthoseabnormalities_abn7" : req.POST.get('indicatebelowthoseabnormalities_abn7'),
        "indicatebelowthoseabnormalities_abn7o" : req.POST.get('indicatebelowthoseabnormalities_abn7o'),
        "indicatebelowthoseabnormalities_trisomyo" : req.POST.get('indicatebelowthoseabnormalities_trisomyo'),
        "indicatebelowthoseabnormalities_trisom9" : req.POST.get('indicatebelowthoseabnormalities_trisom9'),
        "indicatebelowthoseabnormalities_del20" : req.POST.get('indicatebelowthoseabnormalities_del20'),
        "indicatebelowthoseabnormalities_del13" : req.POST.get('indicatebelowthoseabnormalities_del13'),
        "indicatebelowthoseabnormalities_other" : req.POST.get('indicatebelowthoseabnormalities_other'),
        "indicatebelowthoseabnormalities_othero" : req.POST.get('indicatebelowthoseabnormalities_othero'),
        "molecularmarkersatdiagnosis1907" : req.POST.get('molecularmarkersatdiagnosis1907'),
        "bcrablmolecularproductoftqq" : req.POST.get('bcrablmolecularproductoftqq'),
        "jakmutation1" : req.POST.get('jakmutation1'),
        "fiplpdgfr1" : req.POST.get('fiplpdgfr1'),
        "ptpn11" : req.POST.get('ptpn11'),
        "kras22" : req.POST.get('kras22'),
        "nras12" : req.POST.get('nras12'),
        "cbl112" : req.POST.get('cbl112'),
        "other" : req.POST.get('other'),
        "other121212" : req.POST.get('other121212'),
        "dateofthishsct10984" : req.POST.get('dateofthishsct10984'),
        "whoclassificationathsct12" : req.POST.get('whoclassificationathsct12'),
        "cmmlatypicalcml12" : req.POST.get('cmmlatypicalcml12'),
        "cmmlatypicalcml12cr" : req.POST.get('cmmlatypicalcml12cr'),
        "cmmlatypicalcml12rl" : req.POST.get('cmmlatypicalcml12rl'),
        "dateofinitialdiagnosis88" : req.POST.get('dateofinitialdiagnosis88'),
        "myeloproliferativeneoplasmsmpnmaindiseasecode1t2" : req.POST.get('myeloproliferativeneoplasmsmpnmaindiseasecode1t2'),
        "myeloproliferativeneoplasmsmpnmaindiseasecode1t2os" : req.POST.get('myeloproliferativeneoplasmsmpnmaindiseasecode1t2os'),
        "secondaryorigin6776747" : req.POST.get('secondaryorigin6776747'),
        "ipssriskscoreformyelofibrosis3434" : req.POST.get('ipssriskscoreformyelofibrosis3434'),
        "chromosomeanalysisatdiagnosis090" : req.POST.get('chromosomeanalysisatdiagnosis090'),
        "chromosomeanalysisatdiagnosis090ifun" : req.POST.get('chromosomeanalysisatdiagnosis090ifun'),
        "youcantranscribethecompletekaryotype66443" : req.POST.get('youcantranscribethecompletekaryotype66443'),
        "abnormalities_abn1specify_o" : req.POST.get('abnormalities_abn1specify_o'),
        "abnormalities_abn1specify" : req.POST.get('abnormalities_abn1specify'),
        "abn5ormalities_abnspecify_o" : req.POST.get('abn5ormalities_abnspecify_o'),
        "abn5ormalities_abnspecify" : req.POST.get('abn5ormalities_abnspecify'),
        "abn7ormalities_abnspecify" : req.POST.get('abn7ormalities_abnspecify'),
        "trisomy8_tyuiop" : req.POST.get('trisomy8_tyuiop'),
        "trisomy9_tyuiop" : req.POST.get('trisomy9_tyuiop'),
        "del20_tyuiop" : req.POST.get('del20_tyuiop'),
        "del13_tyuiop" : req.POST.get('del13_tyuiop'),
        "otherspecifytyuirtyuiofc_txt" : req.POST.get('otherspecifytyuirtyuiofc_txt'),
        "otherspecifytyuirtyuiofc" : req.POST.get('otherspecifytyuirtyuiofc'),
        "molecularmarkeranalysisatdiagnosis1907" : req.POST.get('molecularmarkeranalysisatdiagnosis1907'),
        "bcrabl55678" : req.POST.get('bcrabl55678'),
        "jakmutation3434234" : req.POST.get('jakmutation3434234'),
        "ifpresent_jakmutation3434234" : req.POST.get('ifpresent_jakmutation3434234'),
        "cmplmutation4190" : req.POST.get('cmplmutation4190'),
        "calreticulinmutation65456" : req.POST.get('calreticulinmutation65456'),
        "fiplpdgfr1242" : req.POST.get('fiplpdgfr1242'),
        "otherspecifytyre54567654" : req.POST.get('otherspecifytyre54567654'),
        "otherspecifytyre54567654o" : req.POST.get('otherspecifytyre54567654o'),
        "dateofinitialdihsct" : req.POST.get('dateofinitialdihsct'),
        "whoclassificationathsct6777" : req.POST.get('whoclassificationathsct6777'),
        "dateoftransformationwhoclassificationathsct6777" : req.POST.get('dateoftransformationwhoclassificationathsct6777'),
        "whoclassificationathsct6777dateoftransformation" : req.POST.get('whoclassificationathsct6777dateoftransformation'),
        "dipssriskscoreformyelofibrosis45" : req.POST.get('dipssriskscoreformyelofibrosis45'),
        "dipssriskscorestatus" : req.POST.get('dipssriskscorestatus'),
        "dipssriskscorestatuscompleteremissioncr" : req.POST.get('dipssriskscorestatuscompleteremissioncr'),
        "dipssriskscorestatusrelapseaftercr" : req.POST.get('dipssriskscorestatusrelapseaftercr'),
        "dateofinitialdiagnosis13" : req.POST.get('dateofinitialdiagnosis13'),
        "classification127890" : req.POST.get('classification127890'),
        "classification127890mm" : req.POST.get('classification127890mm'),
        "classification127890otherspecify" : req.POST.get('classification127890otherspecify'),
        "heavychaintype3434" : req.POST.get('heavychaintype3434'),
        "lightchaintype5545" : req.POST.get('lightchaintype5545'),
        "stage532654356543" : req.POST.get('stage532654356543'),
        "symptomswewewe" : req.POST.get('symptomswewewe'),
        "issstage4erfe54545" : req.POST.get('issstage4erfe54545'),
        "chromosomeanalysisatdiagnosis5v6" : req.POST.get('chromosomeanalysisatdiagnosis5v6'),
        "ifabnormalcomplexkariotype409" : req.POST.get('ifabnormalcomplexkariotype409'),
        "youcantranscribethecompletekaryotyped444" : req.POST.get('youcantranscribethecompletekaryotyped444'),
        "indicatebelow_del13q14" : req.POST.get('indicatebelow_del13q14'),
        "indicatebelow_t1114" : req.POST.get('indicatebelow_t1114'),
        "indicatebelow_abn17q" : req.POST.get('indicatebelow_abn17q'),
        "indicatebelow_del17p" : req.POST.get('indicatebelow_del17p'),
        "indicatebelow_t414" : req.POST.get('indicatebelow_t414'),
        "indicatebelow_t416" : req.POST.get('indicatebelow_t416'),
        "indicatebelow_1qampl" : req.POST.get('indicatebelow_1qampl'),
        "indicatebelow_mycrea" : req.POST.get('indicatebelow_mycrea'),
        "indicatebelow_ost" : req.POST.get('indicatebelow_ost'),
        "indicatebelow_os" : req.POST.get('indicatebelow_os'),
        "molecularmarkeranalysisatdiagnosis1c67" : req.POST.get('molecularmarkeranalysisatdiagnosis1c67'),
        "dateofthishsct17765" : req.POST.get('dateofthishsct17765'),
        "plasmacelldisorders_status" : req.POST.get('plasmacelldisorders_status'),
        "plasmacelldisorders_status_stringentcompleteremission" : req.POST.get('plasmacelldisorders_status_stringentcompleteremission'),
        "plasmacelldisorders_status_verygoodpartialremission" : req.POST.get('plasmacelldisorders_status_verygoodpartialremission'),
        "plasmacelldisorders_status_relapsefromcr" : req.POST.get('plasmacelldisorders_status_relapsefromcr'),
        "dateofinitialdiagnosis18" : req.POST.get('dateofinitialdiagnosis18'),
        "acquired18905" : req.POST.get('acquired18905'),
        "acquired18905_other" : req.POST.get('acquired18905_other'),
        "etiology45896" : req.POST.get('etiology45896'),
        "etiology45896ost" : req.POST.get('etiology45896ost'),
        "congenital17903" : req.POST.get('congenital17903'),
        "congenital17903os" : req.POST.get('congenital17903os'),
        "dateofinitialdiagnosis199" : req.POST.get('dateofinitialdiagnosis199'),
        "classification667" : req.POST.get('classification667'),
        "classification667_thalassaemia" : req.POST.get('classification667_thalassaemia'),
        "classification667_skilcell" : req.POST.get('classification667_skilcell'),
        "classification667_other_sp" : req.POST.get('classification667_other_sp'),
        "dateofinitialdiagnosis1953" : req.POST.get('dateofinitialdiagnosis1953'),
        "dateofinitialdiagnosis1409" : req.POST.get('dateofinitialdiagnosis1409'),
        "classification61907" : req.POST.get('classification61907'),
        "classification61907_other" : req.POST.get('classification61907_other'),
        "tnmclassification_type" : req.POST.get('tnmclassification_type'),
        "tnmclassification_type_tumour" : req.POST.get('tnmclassification_type_tumour'),
        "tnmclassification_type_node" : req.POST.get('tnmclassification_type_node'),
        "tnmclassification_type_metastases" : req.POST.get('tnmclassification_type_metastases'),
        "tnmclassification_type_diseasespecificstaging" : req.POST.get('tnmclassification_type_diseasespecificstaging'),
        "estrogener2423534524" : req.POST.get('estrogener2423534524'),
        "progesteronpgr364454" : req.POST.get('progesteronpgr364454'),
        "herneucerbb353434" : req.POST.get('herneucerbb353434'),
        "axillarylymphnodesatsurgerynpositivenexamined" : req.POST.get('axillarylymphnodesatsurgerynpositivenexamined'),
        "sentinelnode2323" : req.POST.get('sentinelnode2323'),
        "carcinomatype3y799" : req.POST.get('carcinomatype3y799'),
        "proliferationindexactivitybykiormibimmunostainingofpositiveceee" : req.POST.get('proliferationindexactivitybykiormibimmunostainingofpositiveceee'),
        "histologicalclassification190" : req.POST.get('histologicalclassification190'),
        "siteoforigin16790" : req.POST.get('siteoforigin16790'),
        "siteoforigin16790_other" : req.POST.get('siteoforigin16790_other'),
        "statusathsct2323" : req.POST.get('statusathsct2323'),
        "riskcategoryatdiseaserecurrenceorplatinumrefractorinessfollo432" : req.POST.get('riskcategoryatdiseaserecurrenceorplatinumrefractorinessfollo432'),
        "rcadstatus" : req.POST.get('rcadstatus'),
        "rcadstatuscompleteremissioncr" : req.POST.get('rcadstatuscompleteremissioncr'),
        "rcadstatuscompleteremissioncrnumber" : req.POST.get('rcadstatuscompleteremissioncrnumber'),
        "rcadstatusreplacenumber" : req.POST.get('rcadstatusreplacenumber'),
        "rcadstatusreplacesensi" : req.POST.get('rcadstatusreplacesensi'),
        "organsinvolved35632" : req.POST.get('organsinvolved35632'),
        "organsinvolved35632otherspecify" : req.POST.get('organsinvolved35632otherspecify'),
        "dateofinitialdiagnosis56709" : req.POST.get('dateofinitialdiagnosis56709'),
        "classification5676549076" : req.POST.get('classification5676549076'),
        "classification5676549076scidotherspecify" : req.POST.get('classification5676549076scidotherspecify'),
        "classification5676549076otherspecify" : req.POST.get('classification5676549076otherspecify'),
        "dateofthishsct188989" : req.POST.get('dateofthishsct188989'),
        "dateofinitialdiagnosis113" : req.POST.get('dateofinitialdiagnosis113'),
        "classification1095123" : req.POST.get('classification1095123'),
        "classification1095123otherspecify" : req.POST.get('classification1095123otherspecify'),
        "dateofthishsct2479" : req.POST.get('dateofthishsct2479'),
        "dateofinitialdiagnosis11368" : req.POST.get('dateofinitialdiagnosis11368'),
        "classification1230" : req.POST.get('classification1230'),
        "classification1230otherssdsr43" : req.POST.get('classification1230otherssdsr43'),
        "classification" : req.POST.get('classification'),
        "classification1230other" : req.POST.get('classification1230other'),
        "dateofthishsct19089" : req.POST.get('dateofthishsct19089'),
        "dateofinitialdiagnosis1675" : req.POST.get('dateofinitialdiagnosis1675'),
        "classification17932" : req.POST.get('classification17932'),
        "classification17932otherspecify" : req.POST.get('classification17932otherspecify'),
        "dateofthishsct1896" : req.POST.get('dateofthishsct1896'),
        "dateofinitialdiagnosis19074" : req.POST.get('dateofinitialdiagnosis19074'),
        "classification657012" : req.POST.get('classification657012'),
        "classification657012inv" : req.POST.get('classification657012inv'),
        "classification657012invotherspecify" : req.POST.get('classification657012invotherspecify'),
        "dateofthefirstmobilisation789" : req.POST.get('dateofthefirstmobilisation789'),
        "performance1278904" : req.POST.get('performance1278904'),
        "performance_used_score" : req.POST.get('performance_used_score'),
        "creatinineclearancecockroftformula189" : req.POST.get('creatinineclearancecockroftformula189'),
        "proteinuria468009" : req.POST.get('proteinuria468009'),
        "modifiedrodnanskinscore233546" : req.POST.get('modifiedrodnanskinscore233546'),
        "dlco3455643556" : req.POST.get('dlco3455643556'),
        "pulmonaryarterialsystolicpressure333" : req.POST.get('pulmonaryarterialsystolicpressure333'),
        "giinvolvement2356" : req.POST.get('giinvolvement2356'),
        "dateofthishsct1258" : req.POST.get('dateofthishsct1258'),
        "classification27u90" : req.POST.get('classification27u90'),
        "dateofthefirstmobilisation12c6" : req.POST.get('dateofthefirstmobilisation12c6'),
        "sledaiscore3434" : req.POST.get('sledaiscore3434'),
        "dateofthishsct344646" : req.POST.get('dateofthishsct344646'),
        "classification1803461" : req.POST.get('classification1803461'),
        "othertypeofconnectivetissuediseasespecify" : req.POST.get('othertypeofconnectivetissuediseasespecify'),
        "dateofinitialdiagnosis18765" : req.POST.get('dateofinitialdiagnosis18765'),
        "autoimmunedisordersvasculitis5090" : req.POST.get('autoimmunedisordersvasculitis5090'),
        "autoimmunedisordersvasculitis5090otherspecify" : req.POST.get('autoimmunedisordersvasculitis5090otherspecify'),
        "autoimmunedisordersarthritis12666" : req.POST.get('autoimmunedisordersarthritis12666'),
        "juvenileidiopathicarthritisotherspecify" : req.POST.get('juvenileidiopathicarthritisotherspecify'),
        "autoimmunedisordersarthritis12666otherarthritis" : req.POST.get('autoimmunedisordersarthritis12666otherarthritis'),
        "dateofthishsct1194" : req.POST.get('dateofthishsct1194'),
        "autoimmunedisordersneurologicaldiseases443" : req.POST.get('autoimmunedisordersneurologicaldiseases443'),
        "dateofthefirstmobilisation32323" : req.POST.get('dateofthefirstmobilisation32323'),
        "statusatmobilisation443" : req.POST.get('statusatmobilisation443'),
        "statusatmobilisation443other" : req.POST.get('statusatmobilisation443other'),
        "statusatmobilisation443edss" : req.POST.get('statusatmobilisation443edss'),
        "numberofgadolinium567896556789" : req.POST.get('numberofgadolinium567896556789'),
        "blymphoblasticleukaemialymphomaoldprecursorbcellall123" : req.POST.get('blymphoblasticleukaemialymphomaoldprecursorbcellall123'),
        "blymphoblasticleukaemialymphomaoldprecursorbcellall126" : req.POST.get('blymphoblasticleukaemialymphomaoldprecursorbcellall126'),
        "blymphoblasticleukaemialymphomaoldprecursorbcellall126o" : req.POST.get('blymphoblasticleukaemialymphomaoldprecursorbcellall126o'),
        "dateofthishsct167" : req.POST.get('dateofthishsct167'),
        "dateofinitialdiagnosis09876" : req.POST.get('dateofinitialdiagnosis09876'),
        "haematologicaldiseases5455" : req.POST.get('haematologicaldiseases5455'),
        "haematologicaldiseases5455other" : req.POST.get('haematologicaldiseases5455other'),
        "dateofthishsct1976" : req.POST.get('dateofthishsct1976'),
        "boweldisease344534" : req.POST.get('boweldisease344534'),
        "dateofthefirstmobilisation4341" : req.POST.get('dateofthefirstmobilisation4341'),
        "statusatmobilisationcdai" : req.POST.get('statusatmobilisationcdai'),
        "statusatmobilisationserum" : req.POST.get('statusatmobilisationserum'),
        "boweldisease344534other" : req.POST.get('boweldisease344534other'),
        "dateofthishsct187645" : req.POST.get('dateofthishsct187645'),
        "otherautoimmune2323123" : req.POST.get('otherautoimmune2323123'),
        "otherautoimmune2323123other" : req.POST.get('otherautoimmune2323123other'),
        "dateofthishsct1158" : req.POST.get('dateofthishsct1158'),
        "primarydiseasediagnosis553434" : req.POST.get('primarydiseasediagnosis553434'),
        "ebmtcodecic34565432" : req.POST.get('ebmtcodecic34565432'),
        "contactperson43434" : req.POST.get('contactperson43434'),
        "hospital234234" : req.POST.get('hospital234234'),
        "unit23342" : req.POST.get('unit23342'),
        "email234234" : req.POST.get('email234234'),
        "dateofthisreport454545" : req.POST.get('dateofthisreport454545'),
        "hospitaluniquepatientnumbercode343" : req.POST.get('hospitaluniquepatientnumbercode343'),
        "hospitaluniquepatientnumbercode454" : req.POST.get('hospitaluniquepatientnumbercode454'),
        "dateofbirth645" : req.POST.get('dateofbirth645'),
        "sex43" : req.POST.get('sex43'),
        "dateofthetransplant6343" : req.POST.get('dateofthetransplant6343'),
        "absoluteneutrophilcountanc3434" : req.POST.get('absoluteneutrophilcountanc3434'),
        "absoluteneutrophilcountanc3434no" : req.POST.get('absoluteneutrophilcountanc3434no'),
        "absoluteneutrophilcountanc3434yes" : req.POST.get('absoluteneutrophilcountanc3434yes'),
        "plateletreconstitution32323" : req.POST.get('plateletreconstitution32323'),
        "plateletreconstitution32323yes" : req.POST.get('plateletreconstitution32323yes'),
        "earlygraftloss35634" : req.POST.get('earlygraftloss35634'),
        "acutegraftversushostdiseaseallograftsonly323" : req.POST.get('acutegraftversushostdiseaseallograftsonly323'),
        "dateofonset32355" : req.POST.get('dateofonset32355'),
        "stage_skin_5434543" : req.POST.get('stage_skin_5434543'),
        "stage_liver_5434543" : req.POST.get('stage_liver_5434543'),
        "stage_lowergitract_5434543" : req.POST.get('stage_lowergitract_5434543'),
        "stage_uppergitract_5434543" : req.POST.get('stage_uppergitract_5434543'),
        "stage_other_5434543" : req.POST.get('stage_other_5434543'),
        "additionalcellinfusionsexcludinganewhsct49" : req.POST.get('additionalcellinfusionsexcludinganewhsct49'),
        "additionalcellinfusionsexcludinganewhsct49ny" : req.POST.get('additionalcellinfusionsexcludinganewhsct49ny'),
        "additionalcellinfusionsexcludinganewhsct49ny2" : req.POST.get('additionalcellinfusionsexcludinganewhsct49ny2'),
        "firstdateofthecelltherapyinfusion509" : req.POST.get('firstdateofthecelltherapyinfusion509'),
        "sourceofcells379086" : req.POST.get('sourceofcells379086'),
        "typeofcellscheckallthatapply410" : req.POST.get('typeofcellscheckallthatapply410'),
        "typeofcellscheckallthatapply410o" : req.POST.get('typeofcellscheckallthatapply410o'),
        "chronologicalnumberofthecellinfusionepisodeforthispatieot" : req.POST.get('chronologicalnumberofthecellinfusionepisodeforthispatieot'),
        "indication23456754334567" : req.POST.get('indication23456754334567'),
        "indication23456754334567o" : req.POST.get('indication23456754334567o'),
        "numberofinfusionswithinweeks567" : req.POST.get('numberofinfusionswithinweeks567'),
        "additionaldiseasetreatmentgiven454" : req.POST.get('additionaldiseasetreatmentgiven454'),
        "additionaldiseasetreatmentgiven454y" : req.POST.get('additionaldiseasetreatmentgiven454y'),
        "datestarted45654456" : req.POST.get('datestarted45654456'),
        "chemodrug454" : req.POST.get('chemodrug454'),
        "chemodrug454y" : req.POST.get('chemodrug454y'),
        "chemodrug454yo" : req.POST.get('chemodrug454yo'),
        "chemodrug454yintrathecal" : req.POST.get('chemodrug454yintrathecal'),
        "radiotherapy4644655" : req.POST.get('radiotherapy4644655'),
        "bestdiseasestatusresponseafterhsct12" : req.POST.get('bestdiseasestatusresponseafterhsct12'),
        "bestdiseasestatusresponseafterhsct12date" : req.POST.get('bestdiseasestatusresponseafterhsct12date'),
        "bestdiseasestatusresponseafterhsct12date2" : req.POST.get('bestdiseasestatusresponseafterhsct12date2'),
        "dayassessment56546" : req.POST.get('dayassessment56546'),
        "dateofdeath90995" : req.POST.get('dateofdeath90995'),
        "chronicgraftversushostdiseasepr12344" : req.POST.get('chronicgraftversushostdiseasepr12344'),
        "chronicgraftversushostdiseasepr12344date" : req.POST.get('chronicgraftversushostdiseasepr12344date'),
        "maximumextentduringthisperiod2434" : req.POST.get('maximumextentduringthisperiod2434'),
        "maximumextentduringthisperiod3434" : req.POST.get('maximumextentduringthisperiod3434'),
        "firstrelapseorprogressionafterhsct456" : req.POST.get('firstrelapseorprogressionafterhsct456'),
        "firstrelapseorprogressionafterhsct456datey" : req.POST.get('firstrelapseorprogressionafterhsct456datey'),
        "relapseprogressiondetectedbymethod34343" : req.POST.get('relapseprogressiondetectedbymethod34343'),
        "relapseprogressiondetectedbymethod34343dn" : req.POST.get('relapseprogressiondetectedbymethod34343dn'),
        "relapseprogressiondetectedbymethod34343dy" : req.POST.get('relapseprogressiondetectedbymethod34343dy'),
        "relapseprogressiondetectedbymethodcytogenetic323" : req.POST.get('relapseprogressiondetectedbymethodcytogenetic323'),
        "relapseprogressiondetectedbymethodcytogenetic323dn" : req.POST.get('relapseprogressiondetectedbymethodcytogenetic323dn'),
        "relapseprogressiondetectedbymethodcytogenetic323dy" : req.POST.get('relapseprogressiondetectedbymethodcytogenetic323dy'),
        "relapseprogressiondetectedbymethod5454" : req.POST.get('relapseprogressiondetectedbymethod5454'),
        "relapseprogressiondetectedbymethod5454dn" : req.POST.get('relapseprogressiondetectedbymethod5454dn'),
        "relapseprogressiondetectedbymethod5454dy" : req.POST.get('relapseprogressiondetectedbymethod5454dy'),
        "wasdiseasedetectedbymethodwhenthepat4343" : req.POST.get('wasdiseasedetectedbymethodwhenthepat4343'),
        "lastdateassessed3434234" : req.POST.get('lastdateassessed3434234'),
        "wasdiseasedetectedbymethodwhenthepatientwas545" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwas545'),
        "wasdiseasedetectedbymethodwhenthepatientwas545y" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwas545y'),
        "dateoflastassessment34334" : req.POST.get('dateoflastassessment34334'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastasses4545" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastasses4545'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastasses4545y" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastasses4545y'),
        "lastdateassessed9075" : req.POST.get('lastdateassessed9075'),
        "survivalstatuslastcontactdateatdayassessment4509" : req.POST.get('survivalstatuslastcontactdateatdayassessment4509'),
        "maincauseofdeath29042" : req.POST.get('maincauseofdeath29042'),
        "maincauseofdeath29042other" : req.POST.get('maincauseofdeath29042other'),
        "contributorycauseofdeath232" : req.POST.get('contributorycauseofdeath232'),
        "contributorycauseofdeath232infection" : req.POST.get('contributorycauseofdeath232infection'),
        "contributorycauseofdeath232otherspecify" : req.POST.get('contributorycauseofdeath232otherspecify'),
        "primarydiseasediagnosis76432" : req.POST.get('primarydiseasediagnosis76432'),
        "ebmtcodecic34347" : req.POST.get('ebmtcodecic34347'),
        "contactperson6343" : req.POST.get('contactperson6343'),
        "hospital1256" : req.POST.get('hospital1256'),
        "unit77435" : req.POST.get('unit77435'),
        "email96564" : req.POST.get('email96564'),
        "dateofthisreport7443545" : req.POST.get('dateofthisreport7443545'),
        "hospitaluniquepatientnumbercode4553" : req.POST.get('hospitaluniquepatientnumbercode4553'),
        "hospitaluniquepatientnumbercode" : req.POST.get('hospitaluniquepatientnumbercode'),
        "dateofbirth55334" : req.POST.get('dateofbirth55334'),
        "sex5443434" : req.POST.get('sex5443434'),
        "dateofthetransplant5399" : req.POST.get('dateofthetransplant5399'),
        "dateoflastfollowupordeath4653" : req.POST.get('dateoflastfollowupordeath4653'),
        "bestdiseasestatusresponseaftertransplant54" : req.POST.get('bestdiseasestatusresponseaftertransplant54'),
        "hsctdate3" : req.POST.get('hsctdate3'),
        "neverincrdateassessed4" : req.POST.get('neverincrdateassessed4'),
        "maximumgrade543564" : req.POST.get('maximumgrade543564'),
        "dateofonset345378" : req.POST.get('dateofonset345378'),
        "stage78787_skin" : req.POST.get('stage78787_skin'),
        "stage78787_liver" : req.POST.get('stage78787_liver'),
        "stage78787_lowergitract" : req.POST.get('stage78787_lowergitract'),
        "stage78787_uppergitract" : req.POST.get('stage78787_uppergitract'),
        "stage78787_other" : req.POST.get('stage78787_other'),
        "chronicgraftversushostdiseasepresentduringthi333" : req.POST.get('chronicgraftversushostdiseasepresentduringthi333'),
        "chronicgraftversushostdiseasepresentduringthi333y" : req.POST.get('chronicgraftversushostdiseasepresentduringthi333y'),
        "chronicgraftversushostdiseasepresentduringthi333date" : req.POST.get('chronicgraftversushostdiseasepresentduringthi333date'),
        "chronicgraftversushostdiseasepresentduringthi333ydtre" : req.POST.get('chronicgraftversushostdiseasepresentduringthi333ydtre'),
        "maximumextentduringthisperiodewe345" : req.POST.get('maximumextentduringthisperiodewe345'),
        "maximumnihscoreduringthisperiod4545" : req.POST.get('maximumnihscoreduringthisperiod4545'),
        "lategraftfailure343434" : req.POST.get('lategraftfailure343434'),
        "didasecondarymalignancylymphoproliferati5454545" : req.POST.get('didasecondarymalignancylymphoproliferati5454545'),
        "dateofdiagnosisy565664" : req.POST.get('dateofdiagnosisy565664'),
        "diagnosis35676543" : req.POST.get('diagnosis35676543'),
        "isthissecondarymalignancyadonorcellleukaemia48907" : req.POST.get('isthissecondarymalignancyadonorcellleukaemia48907'),
        "isthissecondarymalignancyadonorcellleukaemia" : req.POST.get('isthissecondarymalignancyadonorcellleukaemia'),
        "startdateoftheadditionaltreatmentsincelastreport4341" : req.POST.get('startdateoftheadditionaltreatmentsincelastreport4341'),
        "didthediseasetreatmentincludeadditionalcellinfusions438" : req.POST.get('didthediseasetreatmentincludeadditionalcellinfusions438'),
        "isthiscellinfusionanallogeneicboost4343" : req.POST.get('isthiscellinfusionanallogeneicboost4343'),
        "analloboostisaninfusionofcellsfromthesamedonorwit54479" : req.POST.get('analloboostisaninfusionofcellsfromthesamedonorwit54479'),
        "analloboostisaninfusionofcellsfromthesamedonorwithoutcond190" : req.POST.get('analloboostisaninfusionofcellsfromthesamedonorwithoutcond190'),
        "analloboostisaninfusionofcellsfromthesamedonorwithoutcond190y" : req.POST.get('analloboostisaninfusionofcellsfromthesamedonorwithoutcond190y'),
        "datestarted345676543456" : req.POST.get('datestarted345676543456'),
        "chemodrug5890234" : req.POST.get('chemodrug5890234'),
        "chemodrug5890234" : req.POST.get('chemodrug5890234'),
        "chemodrug5890234y" : req.POST.get('chemodrug5890234y'),
        "chemodrug5890234y" : req.POST.get('chemodrug5890234y'),
        "chemodrug5890234y2" : req.POST.get('chemodrug5890234y2'),
        "chemodrug5890234y2" : req.POST.get('chemodrug5890234y2'),
        "chemodrug5890234yo" : req.POST.get('chemodrug5890234yo'),
        "chemodrug5890234yo" : req.POST.get('chemodrug5890234yo'),
        "intrathecal3456543" : req.POST.get('intrathecal3456543'),
        "intrathecal3456543" : req.POST.get('intrathecal3456543'),
        "radiotherapy3674" : req.POST.get('radiotherapy3674'),
        "radiotherapy3674" : req.POST.get('radiotherapy3674'),
        "firstrelapseorprogressionafterhsct1906" : req.POST.get('firstrelapseorprogressionafterhsct1906'),
        "datefirstseen1903452" : req.POST.get('datefirstseen1903452'),
        "relapseprogressiondetectedbymethod18654" : req.POST.get('relapseprogressiondetectedbymethod18654'),
        "relapseprogressiondetectedbymethod18654dn" : req.POST.get('relapseprogressiondetectedbymethod18654dn'),
        "relapseprogressiondetectedbymethod18654dy" : req.POST.get('relapseprogressiondetectedbymethod18654dy'),
        "relapseprogressiondetectedbymethod17689" : req.POST.get('relapseprogressiondetectedbymethod17689'),
        "relapseprogressiondetectedbymethod17689dn" : req.POST.get('relapseprogressiondetectedbymethod17689dn'),
        "relapseprogressiondetectedbymethod17689dy" : req.POST.get('relapseprogressiondetectedbymethod17689dy'),
        "relapseprogressiondetectedbymethod19016" : req.POST.get('relapseprogressiondetectedbymethod19016'),
        "relapseprogressiondetectedbymethod19016dn" : req.POST.get('relapseprogressiondetectedbymethod19016dn'),
        "relapseprogressiondetectedbymethod19016dy" : req.POST.get('relapseprogressiondetectedbymethod19016dy'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessedordat506" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessedordat506'),
        "lastdateassessed506" : req.POST.get('lastdateassessed506'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessedoat956" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessedoat956'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessedoat956y" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessedoat956y'),
        "lastdateassessed9561" : req.POST.get('lastdateassessed9561'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessordat149" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessordat149'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessordat149y" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessordat149y'),
        "lastdateassessed1490" : req.POST.get('lastdateassessed1490'),
        "haspatientorpartnerbecomepregnantafterthistransplant12" : req.POST.get('haspatientorpartnerbecomepregnantafterthistransplant12'),
        "haspatientorpartnerbecomepregnantafterthistransplant12y" : req.POST.get('haspatientorpartnerbecomepregnantafterthistransplant12y'),
        "survivalstatus23457654" : req.POST.get('survivalstatus23457654'),
        "checkhereifpatientlosttofollowup1637" : req.POST.get('checkhereifpatientlosttofollowup1637'),
        "maincauseofdeath5390645" : req.POST.get('maincauseofdeath5390645'),
        "maincauseofdeath5390645other" : req.POST.get('maincauseofdeath5390645other'),
        "contributorycauseofdeathcontributorycauseofdeath10" : req.POST.get('contributorycauseofdeathcontributorycauseofdeath10'),
        "contributorycauseofdeathcontributorycauseofdeath10inf" : req.POST.get('contributorycauseofdeathcontributorycauseofdeath10inf'),
        "contributorycauseofdeathcontributorycauseofdeath10inf1" : req.POST.get('contributorycauseofdeathcontributorycauseofdeath10inf1'),
        "contributorycauseofdeathcontributorycauseofdeath10o" : req.POST.get('contributorycauseofdeathcontributorycauseofdeath10o'),
        "dateofthisreport4567870" : req.POST.get('dateofthisreport4567870'),
        "karnofsky" : req.POST.get('karnofsky'),
        "typeofcell190564534o" : req.POST.get('typeofcell190564534o'),
        "indication556734535746756o" : req.POST.get('indication556734535746756o'),
        "numberofinfusionswithinweeks7876567654" : req.POST.get('numberofinfusionswithinweeks7876567654'),
        "dateofthisreport34234234" : req.POST.get('dateofthisreport34234234'),
        "typeofcell188890o" : req.POST.get('typeofcell188890o'),
        "chronologicalnumberofciforthispatient1690" : req.POST.get('chronologicalnumberofciforthispatient1690'),
        "indication2345987000" : req.POST.get('indication2345987000'),
        "indication2345987000o" : req.POST.get('indication2345987000o'),
        "numberofinfusionswithinweeks12456" : req.POST.get('numberofinfusionswithinweeks12456'),
        "maximumgrade232325" : req.POST.get('maximumgrade232325'),
        "t" : req.POST.get('t'),
        "_8l94P6HACuT1Jv6fwip8wkoPYFVLUUaxFD9DmUApRgAKjxmWt21626593011647" : req.POST.get('_8l94P6HACuT1Jv6fwip8wkoPYFVLUUaxFD9DmUApRgAKjxmWt21626593011647'),
        "_Uu2jkcPOj2LbsPsswB4AfNVUN0eQSpf7uZDGI2l7JycOlzaUxO1626593011648" : req.POST.get('_Uu2jkcPOj2LbsPsswB4AfNVUN0eQSpf7uZDGI2l7JycOlzaUxO1626593011648'),
        "_r2N3NjYhXAZUJm9ayO9i7Ry3UfRjNHKIHilUT5sW08ZYetNJG31626593011648" : req.POST.get('_r2N3NjYhXAZUJm9ayO9i7Ry3UfRjNHKIHilUT5sW08ZYetNJG31626593011648'),
        "_luzEujO9Mj77SUyz5sFsoBbOArf09PIstaJqoAlgGdEkZHbB8i1626593011648" : req.POST.get('_luzEujO9Mj77SUyz5sFsoBbOArf09PIstaJqoAlgGdEkZHbB8i1626593011648'),
        "_qzRpR89v8BzE7Tgt9aTXmEWZtKqNe059J5ekXkGghHGYogcHDV1626593011648" : req.POST.get('_qzRpR89v8BzE7Tgt9aTXmEWZtKqNe059J5ekXkGghHGYogcHDV1626593011648'),
        "_g2S90lTvcmMpTk3A3zhZnPbAsl8wukw8GQ0lyUrdwgZjpfsHBg1626593011649" : req.POST.get('_g2S90lTvcmMpTk3A3zhZnPbAsl8wukw8GQ0lyUrdwgZjpfsHBg1626593011649'),
        "_Gz7AFfjFHf6UrtLPnD1dMnU1gyLgrMUBsITrdLyO5dtGvuo5sH1626593011649" : req.POST.get('_Gz7AFfjFHf6UrtLPnD1dMnU1gyLgrMUBsITrdLyO5dtGvuo5sH1626593011649'),
        "_T8KxaTl5JhxTCjEyWugbjn3578UJsRmXWAjzK4KbirPbKI4vxg1626593011649" : req.POST.get('_T8KxaTl5JhxTCjEyWugbjn3578UJsRmXWAjzK4KbirPbKI4vxg1626593011649'),
        "_hDJgL3RaRRnUj5yRfY9emABC1ZuQa4SfYdD73Nvkj4BFj6Lywf1626593011649" : req.POST.get('_hDJgL3RaRRnUj5yRfY9emABC1ZuQa4SfYdD73Nvkj4BFj6Lywf1626593011649'),
        "_BPxHnue2YTfezfYR2BnMUWRTno8PLlaaM7ZOhzQriHSPolhQzn1626593011649" : req.POST.get('_BPxHnue2YTfezfYR2BnMUWRTno8PLlaaM7ZOhzQriHSPolhQzn1626593011649'),
        "_gy6RZmdkkIFp3X7ZLUAXuEw9FFafpV3DTSP0ScBFu9e3Fvsqer1626593011650" : req.POST.get('_gy6RZmdkkIFp3X7ZLUAXuEw9FFafpV3DTSP0ScBFu9e3Fvsqer1626593011650'),
        "_vlEoeGUrhDJsXWaQhPrADlGBYYbM9x6ywKmAYktiwYIJE33nds1626593011650" : req.POST.get('_vlEoeGUrhDJsXWaQhPrADlGBYYbM9x6ywKmAYktiwYIJE33nds1626593011650'),
        "_114RI5IQTr4VVj5HddG35D48SMRyo4HRh6kk5CPeGEr6anUUGD1626593011650" : req.POST.get('_114RI5IQTr4VVj5HddG35D48SMRyo4HRh6kk5CPeGEr6anUUGD1626593011650'),
        "_sZbgIxQfneG5D4OIqpdrmAzSGIOIfZ2Mf3zOWx9YxAP8W36SLq1626593011650" : req.POST.get('_sZbgIxQfneG5D4OIqpdrmAzSGIOIfZ2Mf3zOWx9YxAP8W36SLq1626593011650'),
        "_A5jK1unj8XsvkYvQK8B6XNHa5UrEqCMDFBayuBtrqFszjm4l3x1626593011650" : req.POST.get('_A5jK1unj8XsvkYvQK8B6XNHa5UrEqCMDFBayuBtrqFszjm4l3x1626593011650'),
        "_Q636XWxW1cfRUU1VhaqR2lPTH5O96KoHwREkHWqPnTTBRp2W7e1626593011650" : req.POST.get('_Q636XWxW1cfRUU1VhaqR2lPTH5O96KoHwREkHWqPnTTBRp2W7e1626593011650'),
        "_0l2jJvWwOY2ywbz1fytByBbwkf7TWppGfJDDs30pHKzplCIPqD1626593011650" : req.POST.get('_0l2jJvWwOY2ywbz1fytByBbwkf7TWppGfJDDs30pHKzplCIPqD1626593011650'),
        "_wASgRBXTkaeW8Mmi7mc2CcEEMR97MVLN1xG62xHImlzyALkt991626593011651" : req.POST.get('_wASgRBXTkaeW8Mmi7mc2CcEEMR97MVLN1xG62xHImlzyALkt991626593011651'),
        "_AEDhAj5DSIw9VmpORuabDyzk9V93wYxnHmOzdm99eXsRhxoGxX1626593011651" : req.POST.get('_AEDhAj5DSIw9VmpORuabDyzk9V93wYxnHmOzdm99eXsRhxoGxX1626593011651'),
        "_rvXID27EgzTGMqfindSxL42CWNHaYPhUCfy1Ozd0W2U5UZqUMv1626593011651" : req.POST.get('_rvXID27EgzTGMqfindSxL42CWNHaYPhUCfy1Ozd0W2U5UZqUMv1626593011651'),
        "_9bmjZNrfsevMDXRvFFULxOctPs7KsfDLpMpQPnZe2SEnj0JhCV1626593011651" : req.POST.get('_9bmjZNrfsevMDXRvFFULxOctPs7KsfDLpMpQPnZe2SEnj0JhCV1626593011651'),
        "_IjM9dadr8Yh7S2om55hs3HNF2VEOo4oIjtzwCgTAk0qQiiKa5u1626593011651" : req.POST.get('_IjM9dadr8Yh7S2om55hs3HNF2VEOo4oIjtzwCgTAk0qQiiKa5u1626593011651'),
        "_Hbw8alimke7FVyBLfSqj7YplPotZS9kTlT8dZqe54uaWemxvl61626593011651" : req.POST.get('_Hbw8alimke7FVyBLfSqj7YplPotZS9kTlT8dZqe54uaWemxvl61626593011651'),
        "_C1nzIMJrjJSK8rFcTa04UAxKNUBJa2SWrgMQL94n957I6GtY0j1626593011652" : req.POST.get('_C1nzIMJrjJSK8rFcTa04UAxKNUBJa2SWrgMQL94n957I6GtY0j1626593011652'),
        "_cPCnYEytVOdZhdHfhaxpROTXBzkKkDFzIj65n7mEmNGki9xklX1626593011652" : req.POST.get('_cPCnYEytVOdZhdHfhaxpROTXBzkKkDFzIj65n7mEmNGki9xklX1626593011652'),
        "_yxsNsiw5dn8RJELRMIw1qqIOnYbjF13Ylq14bCv0IboCLDCoub1626593011652" : req.POST.get('_yxsNsiw5dn8RJELRMIw1qqIOnYbjF13Ylq14bCv0IboCLDCoub1626593011652'),
        "_KxPDcI4OmtElF4vhZNtalqaZaoBnHxVDV91d2VfQ69fqoHLXem1626593011652" : req.POST.get('_KxPDcI4OmtElF4vhZNtalqaZaoBnHxVDV91d2VfQ69fqoHLXem1626593011652'),
        "_EE0s99Myb6accVW1y38MYOjMPyv7WjbhUNkLtUcaxYC2GxUOm51626593011652" : req.POST.get('_EE0s99Myb6accVW1y38MYOjMPyv7WjbhUNkLtUcaxYC2GxUOm51626593011652'),
        "_icusPmxhptgHZZ1SAL256BVn6tS6XKJZC2Xbo7s2LyGaJpb1CA1626593011652" : req.POST.get('_icusPmxhptgHZZ1SAL256BVn6tS6XKJZC2Xbo7s2LyGaJpb1CA1626593011652'),
        "_IoDD3vA7ze17MsQTVwwqFBNn6dPHoMS0aRtwdcKpmiTFH6h4Hf1626593011652" : req.POST.get('_IoDD3vA7ze17MsQTVwwqFBNn6dPHoMS0aRtwdcKpmiTFH6h4Hf1626593011652'),
        "_9x4IXfcHkZRfDIJ4S5oPFmkCvKdeo75rCGduN4wNmbZzXs3CLn1626593011652" : req.POST.get('_9x4IXfcHkZRfDIJ4S5oPFmkCvKdeo75rCGduN4wNmbZzXs3CLn1626593011652'),
        "_tCg9vCk7msGfPKIuyzMHBA1D0gZXOX4TWHzFfyrZsv52033zMQ1626593011652" : req.POST.get('_tCg9vCk7msGfPKIuyzMHBA1D0gZXOX4TWHzFfyrZsv52033zMQ1626593011652'),
        "_pfUEGZbOK5lusMDo2dbScq0VJfnDhP2sMaQD9Vz2CAxuIWxqk41626593011652" : req.POST.get('_pfUEGZbOK5lusMDo2dbScq0VJfnDhP2sMaQD9Vz2CAxuIWxqk41626593011652'),
        "_olJhYuA3b7SNOPhI1W4b8s6na4tlPTQmC5hz2hicKhZs4ErKhS1626593011652" : req.POST.get('_olJhYuA3b7SNOPhI1W4b8s6na4tlPTQmC5hz2hicKhZs4ErKhS1626593011652'),
        "_D8VZDRZ5s4iG1LkXsdx8SWhhoHlj3tRfzvjqyNjtOCaj7ByO7a1626593011653" : req.POST.get('_D8VZDRZ5s4iG1LkXsdx8SWhhoHlj3tRfzvjqyNjtOCaj7ByO7a1626593011653'),
        "_3NeV2DZKJRnO3lOHNcLJsTjvO1otPPofbFPy5Y01ff40SUcOlf1626593011653" : req.POST.get('_3NeV2DZKJRnO3lOHNcLJsTjvO1otPPofbFPy5Y01ff40SUcOlf1626593011653'),
        "_WgElSieC1gDxNsiSeDtthjiSX8OzXn2tKIJphQokUUkTRtwuhI1626593011653" : req.POST.get('_WgElSieC1gDxNsiSeDtthjiSX8OzXn2tKIJphQokUUkTRtwuhI1626593011653'),
        "_pJ6HS5ss1KUjK8bjdwc5mcPXIKtTg9K92W8TYGsEZpcx3Gt0Ip1626593011653" : req.POST.get('_pJ6HS5ss1KUjK8bjdwc5mcPXIKtTg9K92W8TYGsEZpcx3Gt0Ip1626593011653'),
        "_kaWTU6JYkNRa1Gt8T88Ip6MycprdqNTijlTd3jSrRvkais0h8G1626593011653" : req.POST.get('_kaWTU6JYkNRa1Gt8T88Ip6MycprdqNTijlTd3jSrRvkais0h8G1626593011653'),
        "_KF0UVGZzfYwMnuhmmoYFutMcKw2f4u4sN40NOquJxUVtUUQV4h1626593011653" : req.POST.get('_KF0UVGZzfYwMnuhmmoYFutMcKw2f4u4sN40NOquJxUVtUUQV4h1626593011653'),
        "_nKeKf3Yv8PaPsDrIs3VbTMQ2n9KWMSOLFGyxKtxfJ7QJubD1hA1626593011653" : req.POST.get('_nKeKf3Yv8PaPsDrIs3VbTMQ2n9KWMSOLFGyxKtxfJ7QJubD1hA1626593011653'),
        "_WlchHFZ1OTZ3gyrKcgbeHhWWk3pdQzbeTVWWYkBNrCjQferXxp1626593011653" : req.POST.get('_WlchHFZ1OTZ3gyrKcgbeHhWWk3pdQzbeTVWWYkBNrCjQferXxp1626593011653'),
        "_zkMCEUVriDebsFTXDOvWShUnvznnCIjmIG399X7Fv6YFCZOUzg1626593011653" : req.POST.get('_zkMCEUVriDebsFTXDOvWShUnvznnCIjmIG399X7Fv6YFCZOUzg1626593011653'),
        "_PLMmooXaWHofnaylPkJ8kvc4BtBBEvdKsXekchfc0JAfUQoE5W1626593011653" : req.POST.get('_PLMmooXaWHofnaylPkJ8kvc4BtBBEvdKsXekchfc0JAfUQoE5W1626593011653'),
        "_CcGrCnAp3vSSf2JwL1Pe4VKJ185kts7jjJXmfSzfKucsRFGWCS1626593011653" : req.POST.get('_CcGrCnAp3vSSf2JwL1Pe4VKJ185kts7jjJXmfSzfKucsRFGWCS1626593011653'),
        "_2IpOySZ6KcImYPwzTnCWh4r3FcxfMthG9sPHfQ2SwC1Gs8llos1626593011653" : req.POST.get('_2IpOySZ6KcImYPwzTnCWh4r3FcxfMthG9sPHfQ2SwC1Gs8llos1626593011653'),
        "_CtyOC88HIw2wznR6NDOkA2h9pJfLsx8A7yLWaP33HHqMWGfiqG1626593011653" : req.POST.get('_CtyOC88HIw2wznR6NDOkA2h9pJfLsx8A7yLWaP33HHqMWGfiqG1626593011653'),
        "_TbTSpsjUWWSYsJWV09m54diMaBKfPyasoTZ6BLF197VKCRonkk1626593011653" : req.POST.get('_TbTSpsjUWWSYsJWV09m54diMaBKfPyasoTZ6BLF197VKCRonkk1626593011653'),
        "_9ozQLL0XgqKqweYlG1RWWB58NaH3CJ8vi4TmNhBVQ1sL5CYwzh1626593011654" : req.POST.get('_9ozQLL0XgqKqweYlG1RWWB58NaH3CJ8vi4TmNhBVQ1sL5CYwzh1626593011654'),
        "_DFEjgkrd6uG1ExYHQGQ25NC19L63tG5KxjVoYYQi0vEP6Luhra1626593011654" : req.POST.get('_DFEjgkrd6uG1ExYHQGQ25NC19L63tG5KxjVoYYQi0vEP6Luhra1626593011654'),
        "_1LHHP9ZHa14XsC75SCerDWyPVQfOYv2sMpdoaBbyDpJabxnz5j1626593011654" : req.POST.get('_1LHHP9ZHa14XsC75SCerDWyPVQfOYv2sMpdoaBbyDpJabxnz5j1626593011654'),
        "_FuUzQpEoW3bn6vAuSNhvrNLoTgxd4sktHXYvrA5BFIGJCXKZTX1626593011654" : req.POST.get('_FuUzQpEoW3bn6vAuSNhvrNLoTgxd4sktHXYvrA5BFIGJCXKZTX1626593011654'),
        "_Z5Sn85Z9ind7FuZRxHgMR2gOi28Yh7IjqooFJMmZVm5KqMGQod1626593011654" : req.POST.get('_Z5Sn85Z9ind7FuZRxHgMR2gOi28Yh7IjqooFJMmZVm5KqMGQod1626593011654'),
        "_WebpTUpwpceKhmDQFTOB6sqnBhZQZpF0xrubjos2EA18zxGi7S1626593011654" : req.POST.get('_WebpTUpwpceKhmDQFTOB6sqnBhZQZpF0xrubjos2EA18zxGi7S1626593011654'),
        "_Dvm9CGSEhjW2fpKyXSYXsblb0AFDnJGw5Az8fUqXLsGp7QWaUX1626593011654" : req.POST.get('_Dvm9CGSEhjW2fpKyXSYXsblb0AFDnJGw5Az8fUqXLsGp7QWaUX1626593011654'),
        "_gOR9XRSHIEXgxevzEaodp9gbZaBT8PIPhuPJ70HqyKRKfVhfXk1626593011654" : req.POST.get('_gOR9XRSHIEXgxevzEaodp9gbZaBT8PIPhuPJ70HqyKRKfVhfXk1626593011654'),
        "_pYPTkioLM0U1nDtS3esAJbcWHT6wwC2XVi6cmb9qNvkFDkvdCj1626593011654" : req.POST.get('_pYPTkioLM0U1nDtS3esAJbcWHT6wwC2XVi6cmb9qNvkFDkvdCj1626593011654'),
        "_xQFmOjZi8UOosb3NBGHcoUBaba8RTF4AN3zxEgzb70MIUVbWaJ1626593011654" : req.POST.get('_xQFmOjZi8UOosb3NBGHcoUBaba8RTF4AN3zxEgzb70MIUVbWaJ1626593011654'),
        "_JTQwWmBORjuC92ISJLGG9GS9331ONoJdRW3vC4rTxINhV5Z8Yt1626593011655" : req.POST.get('_JTQwWmBORjuC92ISJLGG9GS9331ONoJdRW3vC4rTxINhV5Z8Yt1626593011655'),
        "_L8mZDXJA37SCng60Oc0kSARc0MtpGhte6Qu41EY90zCJwQMFrO1626593011655" : req.POST.get('_L8mZDXJA37SCng60Oc0kSARc0MtpGhte6Qu41EY90zCJwQMFrO1626593011655'),
        "_jtQpUYAayJrVkCLWFZE8qS8CShNYebWG3lSZMHRt2LPTNEO8Hj1626593011655" : req.POST.get('_jtQpUYAayJrVkCLWFZE8qS8CShNYebWG3lSZMHRt2LPTNEO8Hj1626593011655'),
        "_75INqIPceGGgKc0PlhreuRfDhaXMSifZpCuTi1bwwh53sINiAC1626593011655" : req.POST.get('_75INqIPceGGgKc0PlhreuRfDhaXMSifZpCuTi1bwwh53sINiAC1626593011655'),
        "_914JYRBex2B1nK1PrFKcNVgseWveEM5Ul1Dd6Erz3jBogcMcGR1626593011655" : req.POST.get('_914JYRBex2B1nK1PrFKcNVgseWveEM5Ul1Dd6Erz3jBogcMcGR1626593011655'),
        "_DvMKm3uw8Q309in7VOy1X7a5AG3vuJYMcp42nneuzoJ8oR1aU81626593011655" : req.POST.get('_DvMKm3uw8Q309in7VOy1X7a5AG3vuJYMcp42nneuzoJ8oR1aU81626593011655'),
        "_AFAxo1Yb5wjgWYOgbayU5OwMJnvYLxiffRqJbyUVPHrKEWVX0E1626593011655" : req.POST.get('_AFAxo1Yb5wjgWYOgbayU5OwMJnvYLxiffRqJbyUVPHrKEWVX0E1626593011655'),
        "_UtMtMJqx0JkMjSYxMq8hjYGpM4MrFNuTomPGJ7vSnOZiEfeOrZ1626593097349" : req.POST.get('_UtMtMJqx0JkMjSYxMq8hjYGpM4MrFNuTomPGJ7vSnOZiEfeOrZ1626593097349'),
        "_S3dD6QfPa0k8EqhkeVmMrUgn9C2At7xCUARjzBvU4y4ZUiaaGD1626593097349" : req.POST.get('_S3dD6QfPa0k8EqhkeVmMrUgn9C2At7xCUARjzBvU4y4ZUiaaGD1626593097349'),
        "_k2TPSoJCZdxSOcioR3N3U8AK7AcdXEaFkfEETKmiTjlhdNvaen1626593097349" : req.POST.get('_k2TPSoJCZdxSOcioR3N3U8AK7AcdXEaFkfEETKmiTjlhdNvaen1626593097349'),
        "_R0ca9V9Q8w0yA6oyKdENu5nGLeCEh4cuGYfkzG2PJ7dxShpxwl1626593097349" : req.POST.get('_R0ca9V9Q8w0yA6oyKdENu5nGLeCEh4cuGYfkzG2PJ7dxShpxwl1626593097349'),
        "_QZIWlXrrwVp4V7IfFaoob0t3y8vOuuP14cUqeDYItC9lOnXh2g1626593097349" : req.POST.get('_QZIWlXrrwVp4V7IfFaoob0t3y8vOuuP14cUqeDYItC9lOnXh2g1626593097349'),
        "_xN2TTVpcsEkClCDXrW0GojzCB0H6Ci5By24OEO89hRYYtf1ona1626593097350" : req.POST.get('_xN2TTVpcsEkClCDXrW0GojzCB0H6Ci5By24OEO89hRYYtf1ona1626593097350'),
        "_94jH8rEDkKoydpdggZZQvJYrj5meTnrVUqBz4Vxfh9gEs84ohW1626593097350" : req.POST.get('_94jH8rEDkKoydpdggZZQvJYrj5meTnrVUqBz4Vxfh9gEs84ohW1626593097350'),
        "_A9PU99Guflxl6lKeLMPNg6pLY7A5kezIjtyMNmZJxHf8fRdbfV1626593097350" : req.POST.get('_A9PU99Guflxl6lKeLMPNg6pLY7A5kezIjtyMNmZJxHf8fRdbfV1626593097350'),
        "_Uj5OiWIBMZGKpz8RswFYkNEbVBN5HndXPhkrW5J6gnYgNNYwOu1626593097350" : req.POST.get('_Uj5OiWIBMZGKpz8RswFYkNEbVBN5HndXPhkrW5J6gnYgNNYwOu1626593097350'),
        "_lmuzOqsgkhD7PvK6YQXMQmPL8pFbOR5VcFujVrcBPGHJ67JXhx1626593097350" : req.POST.get('_lmuzOqsgkhD7PvK6YQXMQmPL8pFbOR5VcFujVrcBPGHJ67JXhx1626593097350'),
        "_mELy9WvbeIdkJMcFPPjCVqx00mMX9ZKF1g6bnO7yFYbM1cmuu31626593097350" : req.POST.get('_mELy9WvbeIdkJMcFPPjCVqx00mMX9ZKF1g6bnO7yFYbM1cmuu31626593097350'),
        "_gpErlS2NMA7UeosbH8tXQj4AirwyFExmrkQByrm7mmtaSddEPp1626593097350" : req.POST.get('_gpErlS2NMA7UeosbH8tXQj4AirwyFExmrkQByrm7mmtaSddEPp1626593097350'),
        "_vF4fKpxfFGvpWfJhP0lpcTZuUwW5Cto07PyjkAIANe5qKMEbBU1626593097350" : req.POST.get('_vF4fKpxfFGvpWfJhP0lpcTZuUwW5Cto07PyjkAIANe5qKMEbBU1626593097350'),
        "_aZMPB6WsVmNThAaV6phFs48Wscbc6cGX5IsvaZ4xnwFOqh9pai1626593097350" : req.POST.get('_aZMPB6WsVmNThAaV6phFs48Wscbc6cGX5IsvaZ4xnwFOqh9pai1626593097350'),
        "_QHAlQROvB1HzOqkBr6Av9XzTMUPtyOEpVNkDLT68NtYTLXbOSv1626593097350" : req.POST.get('_QHAlQROvB1HzOqkBr6Av9XzTMUPtyOEpVNkDLT68NtYTLXbOSv1626593097350'),
        "_vm0td8sLzugj4bfOtflpjey4vGvjkNkK9mVLAELXJVQvHLREA31626593097351" : req.POST.get('_vm0td8sLzugj4bfOtflpjey4vGvjkNkK9mVLAELXJVQvHLREA31626593097351'),
        "_7nR5n1pCg5FVWkJZR5Mlde5r1fQyGrytZoGXht83CUzG5zD04H1626593097351" : req.POST.get('_7nR5n1pCg5FVWkJZR5Mlde5r1fQyGrytZoGXht83CUzG5zD04H1626593097351'),
        "_UtFMlGSJW4DhLCHqLfhSJAVx7Iq1ByZVPd62hvUC6oO115lVQk1626593097351" : req.POST.get('_UtFMlGSJW4DhLCHqLfhSJAVx7Iq1ByZVPd62hvUC6oO115lVQk1626593097351'),
        "_kkKphxh3RFtp3RI8cwdk4q5plVSqo7xXyKmjX6x4c8Z3eE32tq1626593097351" : req.POST.get('_kkKphxh3RFtp3RI8cwdk4q5plVSqo7xXyKmjX6x4c8Z3eE32tq1626593097351'),
        "_RCSU69f6KN96RVJQBUQwKXmoARJptsMlEr6VvkBJ5gXR5j12JZ1626593097351" : req.POST.get('_RCSU69f6KN96RVJQBUQwKXmoARJptsMlEr6VvkBJ5gXR5j12JZ1626593097351'),
        "_QJe6fixclSaV3mGpOm0oyuE1QD25YmavwOTSdmh20FDBgeJV5r1626593097351" : req.POST.get('_QJe6fixclSaV3mGpOm0oyuE1QD25YmavwOTSdmh20FDBgeJV5r1626593097351'),
        "_PpICvGhtDZSK0JtCOCDOQ2UxLwWhRLGa94kCtPX5KSsFYDQ03e1626593097351" : req.POST.get('_PpICvGhtDZSK0JtCOCDOQ2UxLwWhRLGa94kCtPX5KSsFYDQ03e1626593097351'),
        "_SE1f4prfoEEMGyTyEiqvuLcpNHTahvJ6ddt3pfxzYBrSSUbiST1626593097351" : req.POST.get('_SE1f4prfoEEMGyTyEiqvuLcpNHTahvJ6ddt3pfxzYBrSSUbiST1626593097351'),
        "_4wF7nkWMueezk7ZLHZXZHE8zhdtuSZMO51s7YRlIB0EMXd2Vp61626593097351" : req.POST.get('_4wF7nkWMueezk7ZLHZXZHE8zhdtuSZMO51s7YRlIB0EMXd2Vp61626593097351'),
        "_yDXvZyLNWsWHP5nAJiPCDSoyTKayk6NXuKLjKbDPQ9tBtaaduz1626593097351" : req.POST.get('_yDXvZyLNWsWHP5nAJiPCDSoyTKayk6NXuKLjKbDPQ9tBtaaduz1626593097351'),
        "_7GP92TvCdaKWHMUy6RGgZWm3B1GKzOL9Hej5fTMfeV3vWNao4F1626593097351" : req.POST.get('_7GP92TvCdaKWHMUy6RGgZWm3B1GKzOL9Hej5fTMfeV3vWNao4F1626593097351'),
        "_SuTqe9ArbgkcOuFuQItxtktBlIT1rGaxHoyHx7pN0VC2bfgCto1626593097351" : req.POST.get('_SuTqe9ArbgkcOuFuQItxtktBlIT1rGaxHoyHx7pN0VC2bfgCto1626593097351'),
        "_j49hEX0fV8WlQQIY6hjXGx7h1CbWum4V5vwjo3SeM5PtZBTbFy1626593097351" : req.POST.get('_j49hEX0fV8WlQQIY6hjXGx7h1CbWum4V5vwjo3SeM5PtZBTbFy1626593097351'),
        "_QQRV72IrexNNXFBDCI0PBVFOB8TJ2T1uEsvMjCHr1NqacaVrKk1626593097352" : req.POST.get('_QQRV72IrexNNXFBDCI0PBVFOB8TJ2T1uEsvMjCHr1NqacaVrKk1626593097352'),
        "_vvyOKlX1oph3KfeaIejSmzrHtg3PaosBHy9ZRWKk0hkTMHiAWA1626593097352" : req.POST.get('_vvyOKlX1oph3KfeaIejSmzrHtg3PaosBHy9ZRWKk0hkTMHiAWA1626593097352'),
        "_OgE7lbWvKCd0bnuF9VdNAXzfv4xHPtzbksyEMTPc8gLomQrxVf1626593097352" : req.POST.get('_OgE7lbWvKCd0bnuF9VdNAXzfv4xHPtzbksyEMTPc8gLomQrxVf1626593097352'),
        "_QeH57C3yqKOX0yce3HxVDuzAPsTvUShv8Ayt57bMiFdsUU3oGW1626593097352" : req.POST.get('_QeH57C3yqKOX0yce3HxVDuzAPsTvUShv8Ayt57bMiFdsUU3oGW1626593097352'),
        "_t2t3F85wuHlIyI61l2TDLOaABwJWfL0KYmh9lEqvQNTmW8x2UT1626593097352" : req.POST.get('_t2t3F85wuHlIyI61l2TDLOaABwJWfL0KYmh9lEqvQNTmW8x2UT1626593097352'),
        "_otFxuiAABCMj7Kh0WaLPs2M8KW4Jw2OGZmnyvfvf5ALja3Jh7f1626593097352" : req.POST.get('_otFxuiAABCMj7Kh0WaLPs2M8KW4Jw2OGZmnyvfvf5ALja3Jh7f1626593097352'),
        "_LaTzyQPkPG9BsP7iTKY3Ui1khvOoCGjsr5Js9tT1rxsX5hcuQb1626593097352" : req.POST.get('_LaTzyQPkPG9BsP7iTKY3Ui1khvOoCGjsr5Js9tT1rxsX5hcuQb1626593097352'),
        "_gHhs2pKbXAioDPAdUtb0zdpLM8a7fYz2jr9iLOFsFmf8TlCGZ51626593097353" : req.POST.get('_gHhs2pKbXAioDPAdUtb0zdpLM8a7fYz2jr9iLOFsFmf8TlCGZ51626593097353'),
        "_d08yju31PQHhUp2YOwmmasWuwSb3u1rgA2392dw911Ie3q9ZdB1626593097353" : req.POST.get('_d08yju31PQHhUp2YOwmmasWuwSb3u1rgA2392dw911Ie3q9ZdB1626593097353'),
        "_QRhuqmfCUh6Rd5UuF6AzS8baCnfKtSD9BsVk2AOBpV8MxvVDq61626593097353" : req.POST.get('_QRhuqmfCUh6Rd5UuF6AzS8baCnfKtSD9BsVk2AOBpV8MxvVDq61626593097353'),
        "_BfC2WYL8mtJX4XruYxtgI2n7cNC68Gf0bbXNSNg08fFMbFJ1eK1626593097353" : req.POST.get('_BfC2WYL8mtJX4XruYxtgI2n7cNC68Gf0bbXNSNg08fFMbFJ1eK1626593097353'),
        "_Fyx6ety5kQAmZXW6Y6AZtLmgD9vS1bShONIaE8kD4EZqsTRLEc1626593097353" : req.POST.get('_Fyx6ety5kQAmZXW6Y6AZtLmgD9vS1bShONIaE8kD4EZqsTRLEc1626593097353'),
        "_Xpdc7dx3Rn0j0oT4XtkCRmUTWiCLxMucCm70krBh7WluQxpxCE1626593097354" : req.POST.get('_Xpdc7dx3Rn0j0oT4XtkCRmUTWiCLxMucCm70krBh7WluQxpxCE1626593097354'),
        "_upVL6nCpqio0NrbGTLdYvur9Ff59w1qbwvzZboyDxopZWUSuWf1626593097354" : req.POST.get('_upVL6nCpqio0NrbGTLdYvur9Ff59w1qbwvzZboyDxopZWUSuWf1626593097354'),
        "_eKIVE971rWB4aw1yAS3Tpsh5RfdYwQk7AbcUtbMLZvezmARKzh1626593097354" : req.POST.get('_eKIVE971rWB4aw1yAS3Tpsh5RfdYwQk7AbcUtbMLZvezmARKzh1626593097354'),
        "_H9z3xLwK3b3jGJzny3rJIpWd0VYA0PKjPP37BDVTirhwvhOhM71626593097354" : req.POST.get('_H9z3xLwK3b3jGJzny3rJIpWd0VYA0PKjPP37BDVTirhwvhOhM71626593097354'),
        "_AmI2Vk4tzp5LN7Qty9hO3tUbKRuspgcdxIDPojhdoQ0NlCHfba1626593097354" : req.POST.get('_AmI2Vk4tzp5LN7Qty9hO3tUbKRuspgcdxIDPojhdoQ0NlCHfba1626593097354'),
        "_F0r4OhtCag4BJDGsvgEA1pneVT27BL32BKmUube6f5euzvLb9f1626593097354" : req.POST.get('_F0r4OhtCag4BJDGsvgEA1pneVT27BL32BKmUube6f5euzvLb9f1626593097354'),
        "_c1k0qdEGzx4M7PiNmHJxkCvx62wSAm7rQ24Ns3FzuuXnlGRsCP1626593097354" : req.POST.get('_c1k0qdEGzx4M7PiNmHJxkCvx62wSAm7rQ24Ns3FzuuXnlGRsCP1626593097354'),
        "_AtCYZSzWNK8QsS53ThYveJbOKyMdm2cMWjjecVOzKc12x6vfHZ1626593097354" : req.POST.get('_AtCYZSzWNK8QsS53ThYveJbOKyMdm2cMWjjecVOzKc12x6vfHZ1626593097354'),
        "_pmTiN1dnNZD60kfVA18F0JOYCjui0oTXJ8ZjZP56Gl8NMaiesE1626593097355" : req.POST.get('_pmTiN1dnNZD60kfVA18F0JOYCjui0oTXJ8ZjZP56Gl8NMaiesE1626593097355'),
        "_Aw3ZpEZdCpGynIP25tTe9TPclNGQmSyAfYlsvSjamzBQyOTMBf1626593097355" : req.POST.get('_Aw3ZpEZdCpGynIP25tTe9TPclNGQmSyAfYlsvSjamzBQyOTMBf1626593097355'),
        "_OddOhoIE0YqQ5Su7lDvXi3aYXrpRV3dwYj8zYdPOP4bOWgtxvS1626593097355" : req.POST.get('_OddOhoIE0YqQ5Su7lDvXi3aYXrpRV3dwYj8zYdPOP4bOWgtxvS1626593097355'),
        "_UGFfGj81E9CORDxGA9HSLbzmEg51dYPhALnff18VstpEGoZvDM1626593097355" : req.POST.get('_UGFfGj81E9CORDxGA9HSLbzmEg51dYPhALnff18VstpEGoZvDM1626593097355'),
        "_W4Q78tNvcuuogKoLiB8ZkByW2rcDUaSAibqfdXrctQH6dzvVTK1626593097355" : req.POST.get('_W4Q78tNvcuuogKoLiB8ZkByW2rcDUaSAibqfdXrctQH6dzvVTK1626593097355'),
        "_QyfHJGXKYkgZ9r5DNehnEflCaDbFFQQKluxWxV6rJzNJekjTMU1626593097355" : req.POST.get('_QyfHJGXKYkgZ9r5DNehnEflCaDbFFQQKluxWxV6rJzNJekjTMU1626593097355'),
        "_3FNWRStOFOKpL1srVz7oCkMQAHeTIjxXxmvhBamLQHvHT8iHnd1626593097355" : req.POST.get('_3FNWRStOFOKpL1srVz7oCkMQAHeTIjxXxmvhBamLQHvHT8iHnd1626593097355'),
        "_7zCiiaKpGbOlCbbzEJODPdPjmFIArIvZyXPgNy760jbFq6QfwU1626593097355" : req.POST.get('_7zCiiaKpGbOlCbbzEJODPdPjmFIArIvZyXPgNy760jbFq6QfwU1626593097355'),
        "_OUF8H2CtaVk3fFPfk6rUI3nXMsw8LBHRSdt1nxOky85mx7L4Bc1626593097356" : req.POST.get('_OUF8H2CtaVk3fFPfk6rUI3nXMsw8LBHRSdt1nxOky85mx7L4Bc1626593097356'),
        "_Uybz16a35x8BbFmA5w3JLPFFQ224d9lAeprveQXfzBn75z1isj1626593097356" : req.POST.get('_Uybz16a35x8BbFmA5w3JLPFFQ224d9lAeprveQXfzBn75z1isj1626593097356'),
        "_20Pg9RbFxb8IsHK4RB9ztd8awfti45bvb04eQBQfGXA0H5bOWc1626593097356" : req.POST.get('_20Pg9RbFxb8IsHK4RB9ztd8awfti45bvb04eQBQfGXA0H5bOWc1626593097356'),
        "_11yBfZTTONsK92qffP8Exi46FDVTmfR3g6W5OibevjqRrqkuRu1626593097356" : req.POST.get('_11yBfZTTONsK92qffP8Exi46FDVTmfR3g6W5OibevjqRrqkuRu1626593097356'),
        "_7rB6L5qGyeIM6a28VcUVE7HV0NVYK5RI1CWXz5dKQ0yrtEuugB1626593097356" : req.POST.get('_7rB6L5qGyeIM6a28VcUVE7HV0NVYK5RI1CWXz5dKQ0yrtEuugB1626593097356'),
        "_DCLn0hYeNA5qFpduCko4gNEqRdddhCX6OL437a5G3BEaKuIxdS1626593097356" : req.POST.get('_DCLn0hYeNA5qFpduCko4gNEqRdddhCX6OL437a5G3BEaKuIxdS1626593097356'),
        "_blVPumSnEhmLSelJzeCGs3nPimpQ1YHnomRnPJnLaRmd8MzN6A1626593097357" : req.POST.get('_blVPumSnEhmLSelJzeCGs3nPimpQ1YHnomRnPJnLaRmd8MzN6A1626593097357'),
        "_t3yEEBEibs8fJXIMla8DMVCkvpfJwKpzLe9yq12IXylvAdsuPZ1626593097357" : req.POST.get('_t3yEEBEibs8fJXIMla8DMVCkvpfJwKpzLe9yq12IXylvAdsuPZ1626593097357'),
        "_Jktp0QCcOzs3j5z8HJCoe8lEB1PwQfJgbalXfDS6UrbBru4Az11626593097357" : req.POST.get('_Jktp0QCcOzs3j5z8HJCoe8lEB1PwQfJgbalXfDS6UrbBru4Az11626593097357'),
        "chronologicalnoh" : req.POST.get('chronologicalnoh'),
        "sourceofthestemcellss" : req.POST.get('sourceofthestemcellss'),
        "sourceofthestemcells_others" : req.POST.get('sourceofthestemcells_others'),
        "otherthanforrbcremovalorvolumereductions" : req.POST.get('otherthanforrbcremovalorvolumereductions'),
        "geneticmanipulationofthegrafts" : req.POST.get('geneticmanipulationofthegrafts'),
        "chronologicalnohs" : req.POST.get('chronologicalnohs'),
        "celltherapy" : req.POST.get('celltherapy'),
        "otherinputtextledmoab" : req.POST.get('otherinputtextledmoab'),
        "othermoabspecifyf1" : req.POST.get('othermoabspecifyf1'),
        "otherspecifyrtf1" : req.POST.get('otherspecifyrtf1'),
        "ecptext" : req.POST.get('ecptext'),
        "other120text" : req.POST.get('other120text'),
        "araccytarabinedose" : req.POST.get('araccytarabinedose'),
        "carboplatindose" : req.POST.get('carboplatindose'),
        "algatgalsatsanimalorigindose" : req.POST.get('algatgalsatsanimalorigindose'),
        "bleomycindose" : req.POST.get('bleomycindose'),
        "busulfantypedose" : req.POST.get('busulfantypedose'),
        "cisplatindose" : req.POST.get('cisplatindose'),
        "clofarabinedose" : req.POST.get('clofarabinedose'),
        "corticosteroidsdose" : req.POST.get('corticosteroidsdose'),
        "cyclophosphamidedose" : req.POST.get('cyclophosphamidedose'),
        "daunorubicindose" : req.POST.get('daunorubicindose'),
        "doxorubicinadriamycinedose" : req.POST.get('doxorubicinadriamycinedose'),
        "epirubicindose" : req.POST.get('epirubicindose'),
        "etoposidevpdose" : req.POST.get('etoposidevpdose'),
        "fludarabinedose" : req.POST.get('fludarabinedose'),
        "gemtuzumabdose" : req.POST.get('gemtuzumabdose'),
        "idarubicindose" : req.POST.get('idarubicindose'),
        "ifosfamidedose" : req.POST.get('ifosfamidedose'),
        "imatinibmesylatedose" : req.POST.get('imatinibmesylatedose'),
        "melphalandose" : req.POST.get('melphalandose'),
        "mitoxantronedose" : req.POST.get('mitoxantronedose'),
        "paclitaxeldose" : req.POST.get('paclitaxeldose'),
        "rituximabmabtheraanticddose" : req.POST.get('rituximabmabtheraanticddose'),
        "teniposidedose" : req.POST.get('teniposidedose'),
        "thiotepadose" : req.POST.get('thiotepadose'),
        "treosulphandose" : req.POST.get('treosulphandose'),
        "zevalinradiolabelledmoabdose" : req.POST.get('zevalinradiolabelledmoabdose'),
        "otherradiolabelledmoabdose" : req.POST.get('otherradiolabelledmoabdose'),
        "othermoabspecifydose" : req.POST.get('othermoabspecifydose'),
        "otherspecifyrtdose" : req.POST.get('otherspecifyrtdose'),
        "wasthisintendedtobemyeloablativealloonlyno1" : req.POST.get('wasthisintendedtobemyeloablativealloonlyno1'),
        "wasthisintendedtobemyeloablativealloonlyno2" : req.POST.get('wasthisintendedtobemyeloablativealloonlyno2'),
        "wasthisintendedtobemyeloablativealloonlyno3" : req.POST.get('wasthisintendedtobemyeloablativealloonlyno3'),
        "wasthisintendedtobemyeloablativealloonlyno4" : req.POST.get('wasthisintendedtobemyeloablativealloonlyno4'),
        "wasthisintendedtobemyeloablativealloonlyno5" : req.POST.get('wasthisintendedtobemyeloablativealloonlyno5'),
        "maincauseofdeathcheckonlyonemaincause1" : req.POST.get('maincauseofdeathcheckonlyonemaincause1'),
        "maincauseofdeathcheckonlyonemaincause2" : req.POST.get('maincauseofdeathcheckonlyonemaincause2'),
        "maincauseofdeathcheckonlyonemaincause3" : req.POST.get('maincauseofdeathcheckonlyonemaincause3'),
        "maincauseofdeathcheckonlyonemaincause4" : req.POST.get('maincauseofdeathcheckonlyonemaincause4'),
        "contributorycauseofdeath5" : req.POST.get('contributorycauseofdeath5'),
        "contributorycauseofdeath6" : req.POST.get('contributorycauseofdeath6'),
        "contributorycauseofdeath7" : req.POST.get('contributorycauseofdeath7'),
        "contributorycauseofdeath8" : req.POST.get('contributorycauseofdeath8'),
        "contributorycauseofdeathinfection9" : req.POST.get('contributorycauseofdeathinfection9'),
        "contributorycauseofdeathinfection10" : req.POST.get('contributorycauseofdeathinfection10'),
        "contributorycauseofdeathinfection11" : req.POST.get('contributorycauseofdeathinfection11'),
        "contributorycauseofdeathinfection12" : req.POST.get('contributorycauseofdeathinfection12'),
        "contributorycauseofdeathinfection13" : req.POST.get('contributorycauseofdeathinfection13'),
        "contributorycauseofdeath14" : req.POST.get('contributorycauseofdeath14'),
        "contributorycauseofdeath15" : req.POST.get('contributorycauseofdeath15'),
        "contributorycauseofdeath16" : req.POST.get('contributorycauseofdeath16'),
        "contributorycauseofdeath17" : req.POST.get('contributorycauseofdeath17'),
        "contributorycauseofdeath18" : req.POST.get('contributorycauseofdeath18'),
        "contributorycauseofdeath19" : req.POST.get('contributorycauseofdeath19'),
        "contributorycauseofdeath20" : req.POST.get('contributorycauseofdeath20'),
        "contributorycauseofdeath21" : req.POST.get('contributorycauseofdeath21'),
        "contributorycauseofdeath22" : req.POST.get('contributorycauseofdeath22'),
        "contributorycauseofdeath23" : req.POST.get('contributorycauseofdeath23'),
        "contributorycauseofdeathinfection9in" : req.POST.get('contributorycauseofdeathinfection9in'),
        "contributorycauseofdeathinfection10in" : req.POST.get('contributorycauseofdeathinfection10in'),
        "contributorycauseofdeathinfection11in" : req.POST.get('contributorycauseofdeathinfection11in')
}
    new_data = {k: v for k, v in new_data.items() if v is not None and v != ''}
    return new_data

def form2_json(req, id=None, customer_id=None, date_of_submit=None):
    new_data = {
        "id" : id,
        "customer_id" : customer_id,
        "date_of_submit" : date_of_submit,
        "CIC" : req.POST.get('CIC'),
        "hospitalupn" : req.POST.get('hospitalupn'),
        "patientuic" : req.POST.get('patientuic'),
        "hsctdate" : req.POST.get('hsctdate'),
        "primarydiseasediagnosis" : req.POST.get('primarydiseasediagnosis'),
        "ebmtcodecic" : req.POST.get('ebmtcodecic'),
        "contactperson" : req.POST.get('contactperson'),
        "hospital" : req.POST.get('hospital'),
        "unit" : req.POST.get('unit'),
        "email" : req.POST.get('email'),
        "dateofthisreport" : req.POST.get('dateofthisreport'),
        "hospitaluniquepatientnumbercode" : req.POST.get('hospitaluniquepatientnumbercode'),
        "Initials" : req.POST.get('Initials'),
        "dateofbirth" : req.POST.get('dateofbirth'),
        "sex" : req.POST.get('sex'),
        "dateofthetransplant" : req.POST.get('dateofthetransplant'),
        "absoluteneutrophilcountanc" : req.POST.get('absoluteneutrophilcountanc'),
        "dateoflastassessment11" : req.POST.get('dateoflastassessment11'),
        "dateofancrecovery11" : req.POST.get('dateofancrecovery11'),
        "plateletreconstitution" : req.POST.get('plateletreconstitution'),
        "dateplateletsxl11" : req.POST.get('dateplateletsxl11'),
        "earlygraftloss" : req.POST.get('earlygraftloss'),
        "acutegraftversushostdiseaseallograftsonly" : req.POST.get('acutegraftversushostdiseaseallograftsonly'),
        "dateofonset" : req.POST.get('dateofonset'),
        "austageskin" : req.POST.get('austageskin'),
        "austageliver" : req.POST.get('austageliver'),
        "austagelgt" : req.POST.get('austagelgt'),
        "austageugt" : req.POST.get('austageugt'),
        "austageuotttt" : req.POST.get('austageuotttt'),
        "additionalcellinfusionsexcludinganewhsct" : req.POST.get('additionalcellinfusionsexcludinganewhsct'),
        "isthiscellinfusionanallogeneicboost" : req.POST.get('isthiscellinfusionanallogeneicboost'),
        "isthiscellinfusionanautologousboost" : req.POST.get('isthiscellinfusionanautologousboost'),
        "firstdateofthecelltherapyinfusion" : req.POST.get('firstdateofthecelltherapyinfusion'),
        "sourceofcells" : req.POST.get('sourceofcells'),
        "typeofcellscheckallthatapply" : req.POST.get('typeofcellscheckallthatapply'),
        "typeofcellscheckallthatapplyotxt" : req.POST.get('typeofcellscheckallthatapplyotxt'),
        "chronologicalnumberofthecellinfusionepisodeforthispatient" : req.POST.get('chronologicalnumberofthecellinfusionepisodeforthispatient'),
        "indication" : req.POST.get('indication'),
        "indicationotherspecify" : req.POST.get('indicationotherspecify'),
        "numberofinfusionswithinweeks" : req.POST.get('numberofinfusionswithinweeks'),
        "additionaldiseasetreatmentgiven" : req.POST.get('additionaldiseasetreatmentgiven'),
        "reasonforthisadditionaltreatment" : req.POST.get('reasonforthisadditionaltreatment'),
        "datestarted" : req.POST.get('datestarted'),
        "chemodrug" : req.POST.get('chemodrug'),
        "chemodrugyes" : req.POST.get('chemodrugyes'),
        "chemodrugyesotherdrugchemotherapyspecify" : req.POST.get('chemodrugyesotherdrugchemotherapyspecify'),
        "intrathecal" : req.POST.get('intrathecal'),
        "radiotherapy" : req.POST.get('radiotherapy'),
        "bestdiseasestatusresponseafterhsct" : req.POST.get('bestdiseasestatusresponseafterhsct'),
        "bestdiseasestatusresponseafterhsctdateachieved" : req.POST.get('bestdiseasestatusresponseafterhsctdateachieved'),
        "bestdiseasestatusresponseafterhsctdateassessed" : req.POST.get('bestdiseasestatusresponseafterhsctdateassessed'),
        "lastcontactdatefordayassessmentdd" : req.POST.get('lastcontactdatefordayassessmentdd'),
        "lastcontactdatefordayassessmentdd2" : req.POST.get('lastcontactdatefordayassessmentdd2'),
        "chronicgraftversushostdiseasepresent" : req.POST.get('chronicgraftversushostdiseasepresent'),
        "chronicgraftversushostdiseasepresentdt" : req.POST.get('chronicgraftversushostdiseasepresentdt'),
        "chronicgraftversushostdiseasepresentmtpr" : req.POST.get('chronicgraftversushostdiseasepresentmtpr'),
        "chronicgraftversushostdiseasepresentmtprmxz" : req.POST.get('chronicgraftversushostdiseasepresentmtprmxz'),
        "maximumextentduringthisperiod" : req.POST.get('maximumextentduringthisperiod'),
        "firstrelapseorprogressionafterhsct" : req.POST.get('firstrelapseorprogressionafterhsct'),
        "firstrelapseorprogressionafterhsctdate" : req.POST.get('firstrelapseorprogressionafterhsctdate'),
        "relapseprogressiondetectedbymethod" : req.POST.get('relapseprogressiondetectedbymethod'),
        "relapseprogressiondetectedbymethoddaten" : req.POST.get('relapseprogressiondetectedbymethoddaten'),
        "relapseprogressiondetectedbymethoddatey" : req.POST.get('relapseprogressiondetectedbymethoddatey'),
        "relapseprogressiondetectedbymethodcytogeneticcy" : req.POST.get('relapseprogressiondetectedbymethodcytogeneticcy'),
        "relapseprogressiondetectedbymethodcytogeneticcydn" : req.POST.get('relapseprogressiondetectedbymethodcytogeneticcydn'),
        "relapseprogressiondetectedbymethodcytogeneticcydy" : req.POST.get('relapseprogressiondetectedbymethodcytogeneticcydy'),
        "relapseprogressiondetectedbymethodbm" : req.POST.get('relapseprogressiondetectedbymethodbm'),
        "relapseprogressiondetectedbymethodbmdtn" : req.POST.get('relapseprogressiondetectedbymethodbmdtn'),
        "relapseprogressiondetectedbymethodbmdty" : req.POST.get('relapseprogressiondetectedbymethodbmdty'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessedbefor458" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessedbefor458'),
        "lastdateassessed458" : req.POST.get('lastdateassessed458'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessedbefor672" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessedbefor672'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessedbefor" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessedbefor'),
        "dateoflastassessment667" : req.POST.get('dateoflastassessment667'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessedbefor151" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessedbefor151'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessedbefor324" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessedbefor324'),
        "wasthepresenceofthediseaseconsideredrelapseprogressionsincehsct" : req.POST.get('wasthepresenceofthediseaseconsideredrelapseprogressionsincehsct'),
        "lastdateassessed" : req.POST.get('lastdateassessed'),
        "survivalstatuslastcontactdateatdayassessment" : req.POST.get('survivalstatuslastcontactdateatdayassessment'),
        "maincauseofdeath22" : req.POST.get('maincauseofdeath22'),
        "maincauseofdeath22other" : req.POST.get('maincauseofdeath22other'),
        "contributorycauseofdeath1212" : req.POST.get('contributorycauseofdeath1212'),
        "contributorycauseofdeath1212infection" : req.POST.get('contributorycauseofdeath1212infection'),
        "contributorycauseofdeath1212others" : req.POST.get('contributorycauseofdeath1212others'),
        "celltherapy" : req.POST.get('celltherapy'),
        "detectedbyanymethod1relaps" : req.POST.get('detectedbyanymethod1relaps'),
        "bacterialinput" : req.POST.get('bacterialinput'),
        "viralinput" : req.POST.get('viralinput'),
        "fungalinput" : req.POST.get('fungalinput'),
        "chemodrugyes1" : req.POST.get('chemodrugyes1'),
        "chemodrugyes2" : req.POST.get('chemodrugyes2'),
        "chemodrugyes3" : req.POST.get('chemodrugyes3'),
        "chemodrugyes4" : req.POST.get('chemodrugyes4'),
        "chemodrugyes5" : req.POST.get('chemodrugyes5'),
        "chemodrugyes6" : req.POST.get('chemodrugyes6'),
        "chemodrugyes7" : req.POST.get('chemodrugyes7'),
        "chemodrugyes8" : req.POST.get('chemodrugyes8'),
        "chemodrugyes9" : req.POST.get('chemodrugyes9'),
        "chemodrugyes10" : req.POST.get('chemodrugyes10'),
        "chemodrugyes11" : req.POST.get('chemodrugyes11'),
        "gvhdchk" : req.POST.get('gvhdchk'),
        "interstitialpneumonitischk" : req.POST.get('interstitialpneumonitischk'),
        "pulmonarytoxicitychk" : req.POST.get('pulmonarytoxicitychk'),
        "infectionchk" : req.POST.get('infectionchk'),
        "bacterialchk" : req.POST.get('bacterialchk'),
        "viralchk" : req.POST.get('viralchk'),
        "fungalchk" : req.POST.get('fungalchk'),
        "parasiticchk" : req.POST.get('parasiticchk'),
        "unknownchk" : req.POST.get('unknownchk'),
        "poorgraftfunctionchk" : req.POST.get('poorgraftfunctionchk'),
        "vodchk" : req.POST.get('vodchk'),
        "haemorrhage" : req.POST.get('haemorrhage'),
        "cardiactoxicitychk" : req.POST.get('cardiactoxicitychk'),
        "cnschk" : req.POST.get('cnschk'),
        "gastrointestinalchk" : req.POST.get('gastrointestinalchk'),
        "skintoxicitychk" : req.POST.get('skintoxicitychk'),
        "renalfailurechk" : req.POST.get('renalfailurechk'),
        "multipleorganchk" : req.POST.get('multipleorganchk'),
        "otherspecifychk12" : req.POST.get('otherspecifychk12'),
        "relapseprogressiondetectedbymethod1txt" : req.POST.get('relapseprogressiondetectedbymethod1txt'),
        "relapseprogressiondetectedbymethod2txt" : req.POST.get('relapseprogressiondetectedbymethod2txt'),
        "relapseprogressiondetectedbymethod3txt" : req.POST.get('relapseprogressiondetectedbymethod3txt')
    }
    new_data = {k: v for k, v in new_data.items() if v is not None and v != ''}
    return new_data

def form3_json(req, id=None, customer_id=None, date_of_submit=None):
    new_data = {
        "id" : id,
        "customer_id" : customer_id,
        "date_of_submit" : date_of_submit,
        "CIC" : req.POST.get('CIC'),
        "hospitalupn" : req.POST.get('hospitalupn'),
        "patientuic" : req.POST.get('patientuic'),
        "hsctdate" : req.POST.get('hsctdate'),
        "primarydiseasediagnosis" : req.POST.get('primarydiseasediagnosis'),
        "ebmtcodecic" : req.POST.get('ebmtcodecic'),
        "contactperson" : req.POST.get('contactperson'),
        "hospital" : req.POST.get('hospital'),
        "unit" : req.POST.get('unit'),
        "email" : req.POST.get('email'),
        "dateofthisreport" : req.POST.get('dateofthisreport'),
        "patientfollowingnationalinternationalstudytrial" : req.POST.get('patientfollowingnationalinternationalstudytrial'),
        "hospitaluniquepatientnumbercode" : req.POST.get('hospitaluniquepatientnumbercode'),
        "dateofbirth" : req.POST.get('dateofbirth'),
        "sex" : req.POST.get('sex'),
        "dateofthetransplant" : req.POST.get('dateofthetransplant'),
        "dateoflastfollowupordeath" : req.POST.get('dateoflastfollowupordeath'),
        "bestdiseasestatusresponseaftertransplant" : req.POST.get('bestdiseasestatusresponseaftertransplant'),
        "bestdiseasestatusresponseaftertransplantdate1" : req.POST.get('bestdiseasestatusresponseaftertransplantdate1'),
        "bestdiseasestatusresponseaftertransplantdate2" : req.POST.get('bestdiseasestatusresponseaftertransplantdate2'),
        "didasecondarymalignancylymphoproliferativeormyeloproliferati942" : req.POST.get('didasecondarymalignancylymphoproliferativeormyeloproliferati942'),
        "dateofdiagnosis12" : req.POST.get('dateofdiagnosis12'),
        "diagnosis1243434" : req.POST.get('diagnosis1243434'),
        "isthissecondarymalignancyadonorcellleukaemia" : req.POST.get('isthissecondarymalignancyadonorcellleukaemia'),
        "wasadditionaltreatmentgivenforthediseaseindicationfortransplant" : req.POST.get('wasadditionaltreatmentgivenforthediseaseindicationfortransplant'),
        "wasadditionaltreatmentgivenforthediseaseindicationfortransplantd" : req.POST.get('wasadditionaltreatmentgivenforthediseaseindicationfortransplantd'),
        "didthediseasetreatmentincludeadditionalcellinfusions" : req.POST.get('didthediseasetreatmentincludeadditionalcellinfusions'),
        "isthiscellinfusionanallogeneicboosty" : req.POST.get('isthiscellinfusionanallogeneicboosty'),
        "analloboostisaninfusionofcellsfromthesamedonorwithoutconditi3" : req.POST.get('analloboostisaninfusionofcellsfromthesamedonorwithoutconditi3'),
        "analloboostisaninfusionofcellsfromthesamedonorwithoutconditi" : req.POST.get('analloboostisaninfusionofcellsfromthesamedonorwithoutconditi'),
        "analloboostisaninfusionofcellsfromthesamedonorwithoutconditiy" : req.POST.get('analloboostisaninfusionofcellsfromthesamedonorwithoutconditiy'),
        "datestarted345345" : req.POST.get('datestarted345345'),
        "chemodrug2354234234" : req.POST.get('chemodrug2354234234'),
        "chemodrug2354234234y" : req.POST.get('chemodrug2354234234y'),
        "chemodrug2354234234yq" : req.POST.get('chemodrug2354234234yq'),
        "yes" : req.POST.get('yes'),
        "chemodrug2354234234yot" : req.POST.get('chemodrug2354234234yot'),
        "chemodrug2354234234yotr" : req.POST.get('chemodrug2354234234yotr'),
        "radiotherapy232323" : req.POST.get('radiotherapy232323'),
        "firstrelapseorprogressionafterhsct" : req.POST.get('firstrelapseorprogressionafterhsct'),
        "datefirstseen2323" : req.POST.get('datefirstseen2323'),
        "relapseprogressiondetectedbymethod" : req.POST.get('relapseprogressiondetectedbymethod'),
        "dateassessed343434" : req.POST.get('dateassessed343434'),
        "datefirstseen454545" : req.POST.get('datefirstseen454545'),
        "dateassessed8878" : req.POST.get('dateassessed8878'),
        "datefirstseen3334" : req.POST.get('datefirstseen3334'),
        "dateassessed997" : req.POST.get('dateassessed997'),
        "datefirstseen23788" : req.POST.get('datefirstseen23788'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessedordat506" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessedordat506'),
        "lastdateassesse21212" : req.POST.get('lastdateassesse21212'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessedordat956" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessedordat956'),
        "wasthepresenceofthediseaseconsideredrelapseprogressionsincehsct" : req.POST.get('wasthepresenceofthediseaseconsideredrelapseprogressionsincehsct'),
        "lastdateassessed457777" : req.POST.get('lastdateassessed457777'),
        "wasdiseasedetectedbymethodwhenthepatientwaslastassessedordat149" : req.POST.get('wasdiseasedetectedbymethodwhenthepatientwaslastassessedordat149'),
        "wasthepresenceofthediseaseconsideredrelapseprogressionsincehsc3" : req.POST.get('wasthepresenceofthediseaseconsideredrelapseprogressionsincehsc3'),
        "lastdateassessed98765" : req.POST.get('lastdateassessed98765'),
        "haspatientorpartnerbecomepregnantafterthistransplant" : req.POST.get('haspatientorpartnerbecomepregnantafterthistransplant'),
        "didthepregnancyresultinalivebirth" : req.POST.get('didthepregnancyresultinalivebirth'),
        "survivalstatus" : req.POST.get('survivalstatus'),
        "chywdyhrfhrjwhery" : req.POST.get('chywdyhrfhrjwhery'),
        "maincauseofdeath" : req.POST.get('maincauseofdeath'),
        "maincauseofdeathother" : req.POST.get('maincauseofdeathother'),
        "contributorycauseofdeathcontributorycauseofdeath" : req.POST.get('contributorycauseofdeathcontributorycauseofdeath'),
        "contributorycauseofdeathcontributorycauseofdeathi" : req.POST.get('contributorycauseofdeathcontributorycauseofdeathi'),
        "contributorycauseofdeathcontributorycauseofdeatho" : req.POST.get('contributorycauseofdeathcontributorycauseofdeatho'),
        "dateofthsdsdasdsd" : req.POST.get('dateofthsdsdasdsd'),
        "diseasestatusbeforethisciewe" : req.POST.get('diseasestatusbeforethisciewe'),
        "cellinfusionciregimennothsctorautologousstemcellreinfusion" : req.POST.get('cellinfusionciregimennothsctorautologousstemcellreinfusion'),
        "typeofcellscheckallthatapplysssff" : req.POST.get('typeofcellscheckallthatapplysssff'),
        "typeofcellscheckallthatapplysssffos" : req.POST.get('typeofcellscheckallthatapplysssffos'),
    }
    new_data = {k: v for k, v in new_data.items() if v is not None and v != ''}
    return new_data

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
        patients = models.Patient.objects.all()

    if req.method == 'POST':
        customer_id = req.POST.get('searchinpt').split('-')[0]
        customer_id = int(customer_id[:len(customer_id)-1])
        patients = models.Patient.objects.filter(cid=customer_id)

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

def form2(req):
    if not req.user.is_authenticated:
        return redirect('login-page')
    
    if req.method == 'GET':
        patients = models.Patient.objects.all()
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
        patients = models.Patient.objects.all()
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
        patients = models.Patient.objects.all()
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

    patients = models.Patient.objects.all()

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
        patients = models.Patient.objects.all()
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
        patients = models.Patient.objects.all()
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
        patients = models.Patient.objects.all()
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
                        print(ikey, ivalue)
                        if fvalue == ivalue:
                            print('inside if')
                            matched += 1
                        else:
                            conflict = True
                            break
                if conflict:
                    break
            print(matched, len(i_form))
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
            if form['id'] == int(id):
                chosen_form = form
                break

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
    
def multi_patient_report(req):
    if not req.user.is_authenticated:
        return redirect('login-page')

    patients = models.Patient.objects.all()

    if req.method == 'GET':
        context = {
            'patients': patients,
        }
        return render(req, 'app/multi_patient_report.html', context)

    elif req.method == 'POST':
        count = req.POST['hiddeninput']
        patientids = []

        if count == 'All':
            patients = models.Patient.objects.all()
            for patient in patients:
                patientids.append(int(patient.cid))
        else:
            for i in range(int(count)):
                try:
                    patient = req.POST[f'searchinpt-{i+1}']
                    patient_id = patient.split('-')[0]
                    patient_id = int(patient_id[:len(patient_id)-1])
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
