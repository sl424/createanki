import genanki

vocab_model = genanki.Model(
        1622598035, # random.randrange(1 << 30, 1 << 31)
        "Drew DeVault's Japanese vocab note",
        fields=[
            {'name': 'Japanese'},
            {'name': 'English'},
            {'name': 'Reading'},
            {'name': 'Slug'},
        ], templates=[
            {
                'name': 'Vocab Card',
                'qfmt': '<h1>{{Japanese}}</h1>',
                'afmt': '''
                {{FrontSide}}
                <div class="reading">{{Reading}}</div>
                <hr id="answer" />
                {{English}}
                <ul class="links">
                    <li>
                        <a href="https://jisho.org/word/{{Slug}}">
                            Look up on Jisho.org
                        </a>
                    </li>
                </ul>
                ''',
            },
            {
                'name': 'Vocab Card (reverse)',
                'qfmt': '<div class="noinfo">{{English}}</div>',
                'afmt': '''
                {{FrontSide}}
                <hr id="answer" />
                <h1>{{Japanese}}</h1>
                <h2 class="reading">{{Reading}}</h2>
                <ul class="links">
                    <li>
                        <a href="https://jisho.org/word/{{Slug}}">
                            Look up on Jisho.org
                        </a>
                    </li>
                </ul>
                ''',
            },
            {
                'name': 'Vocab Card (reading)',
                'qfmt': '<h1 class="reading">{{Reading}}</h1>',
                'afmt': '''
                <h1>{{Japanese}}</h1>
                <h2 class="reading">{{Reading}}</h2>
                <hr id="answer" />
                {{English}}
                <ul class="links">
                    <li>
                        <a href="https://jisho.org/word/{{Slug}}">
                            Look up on Jisho.org
                        </a>
                    </li>
                </ul>
                ''',
            },
        ], css="""
        body {
            background: white;
            font-size: 1.5rem;
        }

        h1 {
            text-align: center;
        }

        .reading {
            text-align: center;
        }

        ol, ul {
            max-width: 500px;
            margin: 0 auto;
        }

        .links {
            margin-top: 1rem;
            list-style: none;
            text-align: center;
        }

        .pos {
            font-size: 0.9rem;
        }

        .tags, .info {
            font-size: 0.8rem;
        }

        .noinfo .info {
            display: none;
        }
        """)
