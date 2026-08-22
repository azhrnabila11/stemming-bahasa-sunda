import re

class DisambiguatorSuffixRuleSunda75(object):
    def disambiguate(self, word, kamus_dasar=None):
        if kamus_dasar is None:
            return None

        kandidat = []
        if word.endswith('eunana'):
            kandidat.append(word[:-6])

        if word.endswith('anana'):
            kandidat.append(word[:-5])

        if word.endswith('nana'):
            kandidat.append(word[:-4])

        if word.endswith('ana'):
            kandidat.append(word[:-3])

        if word.endswith('na'):
            kandidat.append(word[:-2])

        if word.endswith('keun'):
            kandidat.append(word[:-4])

        if word.endswith('eun'):
            hasil = word[:-3]
            if len(hasil) >= 4 and not hasil.startswith('leung'):
                kandidat.append(hasil)

        if word.endswith('an'):
            hasil = word[:-2]
            if len(hasil) >= 4 and not hasil.startswith("kuni"):
                kandidat.append(hasil)

        # =================================
        # pilih kandidat yang ada di kamus
        # =================================
        for hasil in kandidat:
            if hasil in kamus_dasar:
                return hasil

        # =================================
        # fallback
        # =================================
        for hasil in kandidat:
            if len(hasil) >= 3:
                return hasil

        return None