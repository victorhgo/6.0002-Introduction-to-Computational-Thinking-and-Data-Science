""" Write a lambda that sorts words in a sentence by length (I assume from lesser to greater)

    We can transform the sentence into a list of words using split(). Then we sort this sentence
    using sorted() and we use len() of each word as a key to sort it.
"""

sentence = "Dearest Mother Nature, who, next to the angels, art the most perfect of all God's creatures, " \
           "I thank thee for thy kindly instruction. I acknowledge and confess that thou art the Mother and " \
           "Empress of the great world, made for the little world of man's mind. Thou movest the bodies above, " \
           "and transmutest the elements below. At the bidding of thy Lord thou dost accomplish both small things " \
           "and great, and renewest, by ceaseless decay and generation, the face of the earth and of the heavens. " \
           "I confess that nothing can live without a soul, and that all that exists and is endued with being flows " \
           "forth from thee by virtue of the power that God has given to thee. All matter is ruled by thee, and the " \
           "elements are under thy governance. From them thou takest the first substance, and from the heavens thou " \
           "dost obtain the form. That substance is formless and void until it is modified and individualized by thee." \
           "First thou givest it a substantial, and then an individual form. In thy great wisdom thou dost cunningly " \
           "mould all thy works through the heavenly influences, so that no mortal hand can utterly destroy them. " \
           "Under thy hands God has put all things that are necessary."

sortedSentence = sorted(sentence.split(), key= lambda x: len(x))

print(sortedSentence)