# The Levenshtein Distance

The Levenshtein distance is a metric to measure how apart are two sequences of words. In other words, it measures the minimum number of edits that you need to do to change a one-word sequence into the other. These edits can be insertions, deletions or substitutions. This metric was named after Vladimir Levenshtein, who originally considered it in 1965.

Ref: <a href="https://en.wikipedia.org/wiki/Levenshtein_distance" target="_blank">Wiki</a>

Saying that; The more similar the two words are the less distance between them, and vice versa. One common use for this distance is in the autocompletion or autocorrection features of text processors or chat applications.

Hello vs Helo is 1 char distance
Hello vs Kelo is 2 chars distance

ie, by using this algoritgm you can semanticly determine your customers searchs much better. Lets assume a customer is searching "aple" but probably meaning "apple"
so you need Levenshtein Distance.

The formal definition of the Levenshtein distance between two strings a and b can be seen as follows:

![Levenshtein Distance Formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/6224efffbe9a4e01afbddeeb900bfd1b3350b335)


It is important to note that the rows on the minimum above correspond to a deletion, an insertion, and a substitution in that order.

It is also possible to calculate the Levenshtein similarity ratio based on the Levenshtein distance.


##Also I 've added numpy.zero function usage alternativly. This is for a better code thanks to using nump.zero() matrix.
You can find at alternative.py


