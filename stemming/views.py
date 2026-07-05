import csv, re, time, docx, nltk
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect  
from django.utils.html import strip_tags 
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.Morphology.Disambiguator.DisambiguatorPrefixRuleSunda import *
from Sastrawi.Morphology.Disambiguator.DisambiguatorSuffixRuleSunda import *
from .models import StemmingResult, KamusStopword, KamusSunda


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
    DisambiguatorInfixRuleSunda72(), DisambiguatorPrefixRuleSunda73(), DisambiguatorPrefixSuffixRuleSunda74(),
    DisambiguatorPrefixSuffixRuleSunda75(), DisambiguatorPrefixInfixSuffixRuleSunda76(), DisambiguatorPrefixSuffixRuleSunda77(),
    DisambiguatorPrefixSuffixRuleSunda78(), DisambiguatorPrefixSuffixRuleSunda79(), DisambiguatorPrefixSuffixRuleSunda80(),
    DisambiguatorPrefixSuffixRuleSunda81(), DisambiguatorPrefixSuffixRuleSunda82(), DisambiguatorPrefixSuffixRuleSunda83(),
    DisambiguatorPrefixSuffixRuleSunda84(), DisambiguatorPrefixSuffixRuleSunda85(), DisambiguatorPrefixSuffixRuleSunda86(),
    DisambiguatorPrefixSuffixRuleSunda87(), DisambiguatorPrefixSuffixRuleSunda88(), DisambiguatorPrefixSuffixRuleSunda89(),
    DisambiguatorPrefixSuffixRuleSunda90()
]


SUFFIX_DISAMBIGUATORS = [
    DisambiguatorSuffixRuleSunda75(),
]

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
                # PROSES TXT (Gunakan .read().decode() agar biner jadi string)
                if nama_file.endswith('.txt'):
                    # Gunakan 'utf-8-sig' untuk menangani file TXT dari Windows (Notepad)
                    teks_input = file_upload.read().decode('utf-8-sig')

                # PROSES DOCX
                elif nama_file.endswith('.docx'):
                    doc = docx.Document(file_upload)
                    teks_input = '\n'.join([para.text for para in doc.paragraphs])

                # PROSES EXCEL
                elif nama_file.endswith('.xlsx'):
                    df = pd.read_excel(file_upload, engine='openpyxl')
                    df.columns = df.columns.str.lower().str.strip()
                    # Ambil kolom 'isi' jika ada, jika tidak ambil kolom pertama
                    col_data = df['isi'] if 'isi' in df.columns else df.iloc[:, 0]
                    teks_input = " ".join(col_data.dropna().astype(str).tolist())

            except Exception as e:
                # Jika ada error saat membaca file, tampilkan di terminal
                print(f"Error reading file: {e}")

       
        # ==============================
        # PROSES NLP
        # ==============================
        if teks_input:
            # hapus hasil sebelumnya
            StemmingResult.objects.all().delete()

            # ==========================================
            # LOAD DATABASE 
            # ==========================================
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

            # ==========================================
            # CLEANSING
            # ==========================================
            proses = strip_tags(teks_input)
            # hapus karakter selain huruf
            proses = re.sub(
                r'[^a-zA-ZéÉ\s]', ' ', proses
            )
            # hapus spasi berlebih
            proses = re.sub(
                r'\s+', ' ', proses).strip()

            # ==========================================
            # CASE FOLDING
            # ==========================================
            proses = proses.lower()

            # ==========================================
            # TOKENIZING (NLTK)
            # ==========================================
            tokens = word_tokenize(proses)
            print("\n=== DEBUG ===")
            print("Ada di proses :", "" in proses)
            print("Ada di token  :", "" in tokens)
            print("Ada di stopword :", "" in db_stopwords)

            # ==========================================
            # STOPWORD REMOVAL
            # ==========================================
            filtered = [
                t for t in tokens 
                if t not in db_stopwords and len(t) > 1
            ]
            print("Ada di filtered :", "" in filtered)

            # ==========================================
            # STEMMING ECS
            # ==========================================
            objs = []
            kata_valid_count = 0
            for kata in filtered:
                hasil_stem, is_valid = ecs_sunda(
                    kata, db_kamus_sunda
                )

                # is_valid = False
                # factory = StemmerFactory()
                # stemmer = factory.create_stemmer()
                # output   = stemmer.stem(kata)

                # tokens2 = word_tokenize(output)
                # output3 = sorted(tokens2)
                # output4 = ' '.join([str(e) for e in output3])
                if is_valid:
                    kata_valid_count += 1

                objs.append(
                    StemmingResult(
                        tokens=kata,
                        stem=hasil_stem,
                        is_correct=is_valid,
                        status_manual="Otomatis"
                    )
                )

            # ==========================================
            # SIMPAN KE DATABASE
            # ==========================================
            if objs:
                StemmingResult.objects.bulk_create(objs)

            # ==========================================
            # EVALUASI
            # ==========================================
            total_kata = len(filtered)
            akurasi = (
                kata_valid_count / total_kata * 100
                if total_kata > 0 else 0
            )

            # ==========================================
            # CONTEXT KE HTML
            # ==========================================
            context = {
                'dataset': teks_input,
                'proses': proses,
                'tokenizing': tokens,
                'remove_stopword': filtered,
                'stemming_data': StemmingResult.objects.all(),
                'total_kata': total_kata,
                'kata_benar': kata_valid_count,
                'akurasi': round(akurasi, 2),
                'running_time': round(
                    time.time() - start_time,4
                ),
            }

    return render(
        request,
        'hasil.html',
        context
    )


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