# Results of testing the .conllup file format using the ud-tools validator

## Level 1
```
*** PASSED ***
```

## Level 2
```
[Line 6 Sent 490437095392301056.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 6 Sent 490437095392301056.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'

The following 37 relations are currently permitted in language [ud]:
acl, advcl, advmod, amod, appos, aux, case, cc, ccomp, clf, compound, conj, cop, csubj, dep, det, discourse, dislocated, expl, fixed, flat, goeswith, iobj, list, mark, nmod, nsubj, nummod, obj, obl, orphan, parataxis, punct, reparandum, root, vocative, xcomp
If a language needs a relation subtype that is not documented in the universal guidelines, the relation
must have a language-specific documentation page in a prescribed format.
See https://universaldependencies.org/contributing_language_specific.html for further guidelines.
Documented dependency relations can be specifically turned on/off for each language in which they are used.
See https://quest.ms.mff.cuni.cz/udvalidator/cgi-bin/unidep/langspec/specify_deprel.pl for details.

[Line 7 Sent 490437095392301056.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 7 Sent 490437095392301056.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 8 Sent 490437095392301056.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 8 Sent 490437095392301056.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 9 Sent 490437095392301056.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 9 Sent 490437095392301056.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 10 Sent 490437095392301056.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 10 Sent 490437095392301056.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 11 Sent 490437095392301056.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 11 Sent 490437095392301056.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 12 Sent 490437095392301056.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 12 Sent 490437095392301056.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 13 Sent 490437095392301056.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 13 Sent 490437095392301056.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 14 Sent 490437095392301056.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
[Line 14 Sent 490437095392301056.1]: [L2 Syntax unknown-deprel] Unknown DEPREL label: '_'
[Line 15 Sent 490437095392301056.1]: [L2 Syntax invalid-deprel] Invalid DEPREL value '_'.
...suppressing further errors regarding Syntax
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
[Line 28 Sent 490437095392301056.1]: [L2 Format invalid-head] Invalid HEAD: '_'.
...suppressing further errors regarding Format
[Line 65953 Sent 445205611081641984.1]: [L2 Enhanced edeps-only-sometimes] Enhanced graph must be empty because we saw empty DEPS on line 6
[Tree number 3558 on line 65953 Sent 445205611081641984.1]: [L2 Enhanced unconnected-egraph] Enhanced graph is not connected. Nodes ['1', '10', '11', '12', '2', '2.1', '3', '4', '5', '6', '7', '8', '9'] are not reachable from any root
Enhanced errors: 2
Format errors: 98930
Syntax errors: 276093
*** FAILED *** with 375025 errors
```