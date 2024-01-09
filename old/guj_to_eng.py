def guj_to_eng(word):
    dict1 = {
        'અ': "a", 'આ': "aa", 'ઇ': "i", 'ઈ': "ee", 'ઉ': "u", 'ઊ': "oo", 'ઋ': "ri",
        'એ': "e", 'ઐ': "ai", 'ઓ': "o", 'ઔ': "au"}

    dict2 = {'ક': "k", 'ચ': "ch", 'ટ': "t", 'ત': "t",
             'પ': "p", 'ખ': "kh", 'છ': "chh", 'ઠ': "th", 'થ': "th", 'ફ': "f", 'ગ': "g", 'જ': "j", 'ડ': "d",
             'દ': "d", 'બ': "b", 'ઘ': "th", 'ઝ': "jh", 'ઢ': "dh", 'ધ': "dh", 'ભ': "bh",
             'ઙ': "n", 'ઞ': "n", 'ણ': "n", 'ન': "n", 'મ': "m", 'ય': "y", 'ર': "r", 'લ': "l", 'વ': "v",
             'શ': "sh", 'ષ': "sh", 'સ': "s", 'હ': "h", 'ળ': "l", 'જ્ઞ': "gy"}

    dict3 = {
        'ા': "a", 'િ': "i", 'ી': "ee", 'ુ': "u", 'ૂ': "oo", 'ૃ': "ru", 'ે': "e", 'ૈ': "ai",
        'ો': "o", 'ૌ': "au", 'ૅ': "e", 'ૉ': "o", 'ં': "an", '્': "", ' ': " "}

    # store translation from gujarti to english
    s1 = ""
    ln = len(word)
    #print(ln)
    # indicate letter is in dict3
    flag1 = 0
    # indicate letter is in dict1 means letter is vowel
    flag2 = 0

    for i in range(0, ln - 1):
        # word[i] in dict3 means symbol hence skip, no need to translate
        if flag1 == 1:
            flag1 = 0
            continue
        elif word[i] == ' ':
            s1 += " "
            continue
        elif word[i] in dict1:
            # letter is vowel hence no need to add 'a'
            flag2 = 1
            s1 += dict1[word[i]]
            # print(s1)
        else:
            s1 += dict2[word[i]]
            # print(s1)

        if word[i + 1] not in dict3:
            # letter is consonant
            if flag2 == 0:
                s1 += "a"
                # print(s1)
            # letter is vowel
            else:
                flag2 = 0
        # letter is symbol
        else:
            s1 += dict3[word[i + 1]]
            # print(s1)
            flag1 = 1

    # translate last letter of word
    if ln > 1 and flag1 == 0:
        # letter is symbol
        if word[-1] in dict3:
            s1 += dict3[word[-1]]
        # letter is consonant
        else:
            s1 += dict2[word[-1]]
    # if word is of one length
    elif ln == 1:
        if word[-1] in dict1:
            s1 += dict1[word[-1]]
        else:
            s1 += dict2[word[-1]]

    #print(s1)
    return s1