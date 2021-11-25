# The Levenshtein Distance

The Levenshtein distance is a metric to measure how apart are two sequences of words. In other words, it measures the minimum number of edits that you need to do to change a one-word sequence into the other. These edits can be insertions, deletions or substitutions. This metric was named after Vladimir Levenshtein, who originally considered it in 1965.

Ref: <a href="https://en.wikipedia.org/wiki/Levenshtein_distance" target="_blank">Wiki</a>

The formal definition of the Levenshtein distance between two strings a and b can be seen as follows:

![Levenshtein Distance Formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/6224efffbe9a4e01afbddeeb900bfd1b3350b335)


It is important to note that the rows on the minimum above correspond to a deletion, an insertion, and a substitution in that order.

It is also possible to calculate the Levenshtein similarity ratio based on the Levenshtein distance.
