# reldi-normtagner-sr
Twitter-based training dataset for non-standard Serbian

`vert_2_conllu.py` is used for transforming the old vert format into the conllu format. The conllu format should be the reference format.

Validating the conllu format can be done with UD tools like this:
```
python ../tools/validate.py --lang SR --level 1 reldi-normtagner-sr.conllu
```
This test should be passed completely.

```
python ../tools/validate.py --lang SR --level 2 reldi-normtagner-sr.conllu
```

In this test only format and syntax errors should be identified, something along this:

```
Format errors: 98913
Syntax errors: 276039
```
