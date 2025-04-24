import statistics as stat

dati = [2, 3, 4, 4, 4, 4, 5, 5, 6, 7, 8, 9, 9, 9, 10, 10, 10, 10, 11, 12, 13, 14, 15, 16]

# print(f"La media numerica della lista Dati è: {stat.mean(dati)}")
# print(f"il numero mediano della lista Dati e` :{stat.median(dati)}")
# print(f"La radice della varianza: quanto in media i dati si discostano : {stat.stdev(dati)}")
# print(stat.variance(dati))
# print(f"il valore che compare piu spesso nella lista e` : {stat.mode(dati)}")


numeri = [1, 2, 3, 4, 5]
numeri.append(6)
numeri.append(7)
numeri[0] = 10
numeri[2] = 30
# print(numeri)

persona = {"nome": "luca", "eta": "30"}
persona["citta"] = "roma"
# print(persona)

data_set = [10, 15, 20, 25, 30]
# print(stat.mean(data_set))
# print(stat.median(data_set))
# print(stat.stdev(data_set))

frase = "ciao mondo ciao python mondo ciao"

def world_count(frase):
    different_words = set(frase.split())
    frase_split = frase.split()
    count_words = {}
    for word in frase_split:
        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word] = 1

    return different_words, count_words

print(world_count(frase))



# frase = "ciao mondo ciao python mondo ciao"
# count_words = {}
# frase_split = frase.split()
# print(frase_split)
# for word in frase_split:
#     if word in count_words:
#         count_words[word] += 1
#     else:
#         count_words[word] = 1
#
# print(count_words)
