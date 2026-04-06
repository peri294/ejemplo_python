review = """La película sigue a un grupo de astronautas que
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo
a través
de tormentas solares y fallos en el sistema de navegación. Al
llegar
a Marte descubren que la base está abandonada y los
suministros
destruidos. Torres decide sacrificar la nave nodriza para
salvar
al equipo y logran volver a la Tierra en una cápsula de
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje
secreto."""
print('ingrese una lista de palabras spoiler separadas por comas:')
review.lower()
spoiler_words = input()
spoiler_words = spoiler_words.split(',')
words = review.split()
for word in review:
    if word in spoiler_words:
        wordlen = len(word)
        review = review.replace(word, '*' * wordlen)
    print(review)