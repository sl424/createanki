# ddevlang

Source code for tools I use for learning Japanese, and maybe other languages in
the future. Mainly for generating Anki decks right now.

## Generate vocabulary decks

Information is fetched from jisho.org.

To generate a "general" vocab deck of all common vocabulary:

```
./vocabgen output.apkg
```

To generate a deck of JLPT N4 and N5 vocab:

```
./vocabgen -j 4-5 output.apkg
```

To generate a deck of music vocab for the concert you're going to next week:

```
./vocabgen -t '#music' output.apkg
```

[List of search tags](https://jisho.org/docs)

For dirty words, including the uncommon ones:

```
./vocabgen -Tt '#X' output.apkg
```

For additional flags, see `./vocabgen -h`

## Contributing

Patches and questions welcome at my public inbox:
[~sircmpwn/public-inbox@lists.sr.ht](https://lists.sr.ht/~sircmpwn/public-inbox).

## TODO

Incorporate word frequency lists from Wikipedia for ordering the resulting
notes:

https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Japanese

https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Japanese10001-20000

kanjigen

- stroke order via kanjivg
- separate reading and writing practice decks
