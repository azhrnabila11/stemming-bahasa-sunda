import csv, re, time, docx, nltk
import os
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect  
from django.utils.html import strip_tags 
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from rule_sunda.DisambiguatorPrefixRuleSunda import *
from rule_sunda.DisambiguatorSuffixRuleSunda import *
from rule_sunda.DisambiguatorKonfiksRuleSunda import *
from .models import StemmingResult, KamusStopword, KamusSunda

nltk_dir = '/tmp/nltk_data'
if not os.path.exists(nltk_dir):
    os.makedirs(nltk_dir, exist_ok=True)
    
if nltk_dir not in nltk.data.path:
    nltk.data.path.append(nltk_dir)

for res in ['punkt', 'punkt_tab']:
    try:
        nltk.data.find(f'tokenizers/{res}')
    except LookupError:
        nltk.download(res, download_dir=nltk_dir)

# 1. KONFIGURASI DISAMBIGUATOR
PREFIX_DISAMBIGUATORS = [
    DisambiguatorPrefixRuleSunda50(), DisambiguatorPrefixRuleSunda51(), DisambiguatorPrefixRuleSunda52(),
    DisambiguatorPrefixRuleSunda53(), DisambiguatorPrefixRuleSunda54(),
    DisambiguatorPrefixRuleSunda55(), DisambiguatorPrefixRuleSunda56(),
    DisambiguatorPrefixRuleSunda57(), DisambiguatorPrefixRuleSunda58(), DisambiguatorPrefixRuleSunda58A(),
    DisambiguatorPrefixRuleSunda59(), DisambiguatorPrefixRuleSunda59A(), DisambiguatorPrefixRuleSunda60(),
    DisambiguatorPrefixRuleSunda61(), DisambiguatorPrefixRuleSunda61A(), DisambiguatorPrefixRuleSunda62(), DisambiguatorPrefixRuleSunda62A(),
    DisambiguatorPrefixRuleSunda63(), DisambiguatorPrefixRuleSunda63A(), DisambiguatorPrefixRuleSunda64(),
    DisambiguatorPrefixRuleSunda65(), DisambiguatorPrefixRuleSunda66(),
    DisambiguatorPrefixRuleSunda67(), DisambiguatorInfixRuleSunda68(),
    DisambiguatorInfixRuleSunda69(), DisambiguatorInfixRuleSunda70(), 
    DisambiguatorInfixRuleSunda70A(), DisambiguatorInfixRuleSunda71(),
    DisambiguatorInfixRuleSunda72(), DisambiguatorPrefixRuleSunda73(),
]

SUFFIX_DISAMBIGUATORS = [
    DisambiguatorSuffixRuleSunda75(),
]

KONFIKS_DISAMBIGUATORS = [
    DisambiguatorPrefixSuffixRuleSunda74(),
    DisambiguatorPrefixSuffixRuleSunda75(), DisambiguatorPrefixInfixSuffixRuleSunda76(), DisambiguatorPrefixSuffixRuleSunda77(),
    DisambiguatorPrefixSuffixRuleSunda78(), DisambiguatorPrefixSuffixRuleSunda79(), DisambiguatorPrefixSuffixRuleSunda80(),
    DisambiguatorPrefixSuffixRuleSunda81(), DisambiguatorPrefixSuffixRuleSunda82(), DisambiguatorPrefixSuffixRuleSunda83(),
    DisambiguatorPrefixSuffixRuleSunda84(), DisambiguatorPrefixSuffixRuleSunda85(), DisambiguatorPrefixSuffixRuleSunda86(),
    DisambiguatorPrefixSuffixRuleSunda87(), DisambiguatorPrefixSuffixRuleSunda88(), DisambiguatorPrefixSuffixRuleSunda89(),
    DisambiguatorPrefixSuffixRuleSunda90(),
]

ALL_SUNDA_RULES = PREFIX_DISAMBIGUATORS + SUFFIX_DISAMBIGUATORS + KONFIKS_DISAMBIGUATORS
for rule_obj in ALL_SUNDA_RULES:
    orig_method = rule_obj.disambiguate
    def make_safe(func):
        def safe_disambiguate(word, kamus_dasar=None):
            if kamus_dasar is None:
                return None
            return func(word, kamus_dasar)
        return safe_disambiguate
    rule_obj.disambiguate = make_safe(orig_method)

def home(request):
    return render(request, 'home.html')

def is_valid_root(word, kamus_dasar):
    return (
        word is not None 
        and len(word) >= 2 and word in kamus_dasar
    )


def ecs_sunda(word, kamus_dasar):
    original = word.lower().strip()
    current = original
    max_loop = 10
    loop = 0

    while loop < max_loop:
        loop += 1
        changed = False

        # =========================
        # PREFIX
        # =========================
        for prefix_rule in PREFIX_DISAMBIGUATORS:
            hasil = prefix_rule.disambiguate(
                current, kamus_dasar
            )

            if hasil and hasil != current:
                print("ini dari prefix: " + type(prefix_rule).__name__)
                current = hasil
                changed = True         

        # =========================
        # SUFFIX
        # =========================
        for suffix_rule in SUFFIX_DISAMBIGUATORS:
            hasil = suffix_rule.disambiguate(
                current, kamus_dasar
            )

            if hasil and hasil != current:
                print("ini dari suffix: " + type(suffix_rule).__name__)
                current = hasil
                changed = True

        # =========================
        # KONFIKS
        # =========================
        for konfiks_rule in KONFIKS_DISAMBIGUATORS:
            hasil = konfiks_rule.disambiguate(
                current, kamus_dasar
            )

            if hasil and hasil != current:
                print("ini dari konfiks: " + type(konfiks_rule).__name__)
                current = hasil
                changed = True
        

        if not changed:
            break

    # =========================
    # VALIDASI AKHIR
    # =========================
    if current in kamus_dasar:
        return current, True

    # fallback:
    # jika tidak berubah sama sekali
    if current == original:
        return original, True
    
    return current, False

@csrf_protect
def stemming_process(request):
    context = {}
    if request.method == 'POST':
        start_time = time.time()
        teks_input = request.POST.get('input_text', '').strip()
        file_upload = request.FILES.get('upload_file')

        if not teks_input and file_upload:
            nama_file = file_upload.name.lower()
            try:
                if nama_file.endswith('.txt'):
                    teks_input = file_upload.read().decode('utf-8-sig')
                elif nama_file.endswith('.docx'):
                    doc = docx.Document(file_upload)
                    teks_input = '\n'.join([para.text for para in doc.paragraphs])
                elif nama_file.endswith('.xlsx'):
                    df = pd.read_excel(file_upload, engine='openpyxl')
                    df.columns = df.columns.str.lower().str.strip()
                    col_data = df['isi'] if 'isi' in df.columns else df.iloc[:, 0]
                    teks_input = " ".join(col_data.dropna().astype(str).tolist())
            except Exception as e:
                print(f"Error reading file: {e}")

        if teks_input:
            StemmingResult.objects.all().delete()

            db_kamus_sunda = {
                str(kata).lower().strip() 
                for kata in KamusSunda.objects.values_list('kata_dasar', flat=True) 
                if kata
            }

            db_stopwords = {
                str(kata).lower().strip() 
                for kata in KamusStopword.objects.values_list('kata_stopword', flat=True) 
                if kata
            }

            proses = strip_tags(teks_input)
            proses = re.sub(r'[^a-zA-ZéÉ\s]', ' ', proses)
            proses = re.sub(r'\s+', ' ', proses).strip()
            proses = proses.lower()

            tokens = word_tokenize(proses)

            filtered = [
                t for t in tokens 
                if t not in db_stopwords and len(t) > 1
            ]

            # Inisialisasi Sastrawi Indonesia
            factory = StemmerFactory()
            stemmer_indo = factory.create_stemmer()

            objs = []
            kata_valid_sunda_count = 0
            kata_valid_indo_count = 0

            for kata in filtered:
                # 1. Jalankan ECS Sunda (Adaptasi)
                hasil_sunda, is_valid_sunda = ecs_sunda(kata, db_kamus_sunda)

                # 2. Jalankan ECS Indonesia (Sastrawi)
                hasil_indo = stemmer_indo.stem(kata)
                is_valid_indo = hasil_indo in db_kamus_sunda

                if is_valid_sunda:
                    kata_valid_sunda_count += 1

                if is_valid_indo:
                    kata_valid_indo_count += 1

                objs.append(
                    StemmingResult(
                        tokens=kata,
                        stem=hasil_sunda,
                        is_correct=is_valid_sunda,
                        status_manual=hasil_indo
                    )
                )

            # SIMPAN KE DATABASE
            if objs:
                StemmingResult.objects.bulk_create(objs)

            # EVALUASI AKURASI GANDA
            total_kata = len(filtered)
            
            akurasi_sunda = (
                kata_valid_sunda_count / total_kata * 100
                if total_kata > 0 else 0
            )

            akurasi_indo = (
                kata_valid_indo_count / total_kata * 100
                if total_kata > 0 else 0
            )

            # CONTEXT KE HTML
            context = {
                'dataset': teks_input,
                'proses': proses,
                'tokenizing': tokens,
                'remove_stopword': filtered,
                'stemming_data': StemmingResult.objects.all(),
                'total_kata': total_kata,
                'kata_benar_sunda': kata_valid_sunda_count,
                'akurasi_sunda': round(akurasi_sunda, 2),
                'kata_benar_indo': kata_valid_indo_count,
                'akurasi_indo': round(akurasi_indo, 2),
                'running_time': round(time.time() - start_time, 4),
            }

    return render(request, 'hasil.html', context)


# ==============================
# EXPORT CSV
# ==============================
def export_csv(request):
    results = StemmingResult.objects.all()
    response = HttpResponse(
        content_type='text/csv'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="hasil_stemming.csv"'

    writer = csv.writer(response, delimiter=';')
    writer.writerow([
        'Token',
        'Stem',
        'Status Stemming'
    ])

    for r in results:
        writer.writerow([
            r.tokens,
            r.stem,
            r.is_correct
        ])

    return response
