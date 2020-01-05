import genanki

def gen_model(rand_num, model_name):
	vocab_model = genanki.Model(
		rand_num, # random.randrange(1 << 30, 1 << 31)
		model_name, #model name
		fields=[
			{'name': 'vocab'},
			{'name': 'furigana'},
			{'name': 'speech'},
			{'name': 'spanish'},
			{'name': 'audio'},
			{'name': 'note'},
			], templates=[
			{
			'name': 'ja->es',
			'qfmt': '''
				<div class="japanese" style="font-size:30px;">{{vocab}}</div> 
				<div style="font-size: 15px;">{{speech}}</div> <br/><br/> 
			''',
			'afmt': '''
				<div class="japanese" style="font-size:30px;">{{furigana:furigana}}</div> 
				<div style="font-size: 15px; ">{{speech}}</div> <br> 
				<hr id=answer>
				<div style="font-size: 30px; ">{{spanish}}<br> </div><br>
				<div style="font-size: 20px; "> {{furigana:nte}}<br></div><br>
				<div> {{audio}}</div>'
			''',
			},
			{
			'name': 'es->ja',
			'qfmt': '''
				<div class="japanese" style="font-size:30px;">{{spanish}}</div> 
				<div style="font-size: 15px;">{{speech}}</div> <br/><br/>'
			''',
			'afmt': '''
				<div class="japanese" style="font-size:30px;">{{spanish}}</div> 
				<div style="font-size: 15px; ">{{speech}}</div> <br> 
				<hr id=answer>
				<div style="font-size: 30px; ">{{vocab}}<br> </div><br>
				<div style="font-size: 20px; "> {{furigana:note}}<br></div><br>
				<div> {{Vocabulary-Audio}} </div>'
			''',
			},
			], css="""
			.card {
				font-family: arial;
				font-size: 20px;
				text-align: center;
				color: black;
				background-color: white;
			},
			""")
	return vocab_model
