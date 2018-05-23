# Cidades e estados para projetos laravel

adicione todos os arquivos do repositorio cada um em sua pasta e roda

	composer dump-autoload
	
	php artisan migrate:fresh --seed
	
pronto, vc já tem uma base de dados com todos os estados brasileiros e suas cidades

## Instruções de uso

#### create do model que terá no endereço fk's para estado e cidade

Para ter todos os estados em ordem alfabética disponíveis para seleção no formulário, no metodo create passe pasa a view a seguinte variavel

	$states = \App\Models\State::orderBy('name')->get();
	
na **view** create adicione os seguintes campos

	<!-- estado -->
	<div class="form-group">
	    <label class="control-label" for="estado">Estado</label>
	    <select id="estado" name="state_id" class="form-control">
		<option value="">Escolha um estado</option>
		@foreach($states as $state)
			<option value="{{ $state->id }}">{{ $state->name }}</option>
		@endforeach
	    </select>
	</div>

	<!-- cidade -->
	<div class="form-group">
	    <label class="control-label" for="cidade">Cidade</label>
	    <select id="cidade" name="city_id" class="form-control" disabled>
		<option value="">Escolha um estado</option>
	    </select>
	</div>
        
na **section js** *:-)* da sua view coloque

	function atualizar_cidades(){
		var estado = $('#estado').val();
		var page = "{{ url('api/cidades_por_estado') }}/" + estado;
		$.ajax({
		    type: 'GET',
		    dataType: 'html',
		    url: page,
		    beforeSend: function () {
			$("#cidade").prop('disabled', true);
		    },
		    success: function (msg) {
			var cidades = JSON.parse(msg);
			var options = '';
			for (var i = 0; i < cidades.length; i++) {
			    var obj = cidades[i];
			    options += '<option value="' + obj.id + '">' + obj.name + '</option>';
			}
			$("#cidade").empty();
			$("#cidade").append(options);
			$("#cidade").prop('disabled', false);
		    }
		});
	}
	$(document).ready(function () {
		@if (old('city_id') !== NULL)
		    $('#estado').val({{ old('state_id') }});
		    atualizar_cidades();
		    $('#city_id').val({{ old('city_id') }});
		@endif
		$('#estado').change(function () {
		    atualizar_cidades();
		});
	});
	
no seu **routes/web** registre a seguinte rota publica auxiliar

	Route::get('api/cidades_por_estado/{estado}', 'StateController@cities_by_state');
	
No **StateController** registre o metodo que retornará as cidades do estado atual do select

	/**
     * Busca no banco por todas as cidades do estado passado e as retorna
     * 
     * @return JSON
     */
    public function cities_by_state($id_estado) {
        $state = \App\Models\State::find($id_estado);
        $cities = $state->cities;
        return $cities;
    }
 
 na **view** edit coloque os mesmos inputs da create apenas mudando um pouquinho o js
 
	function atualizar_cidades(assincrono = true){
		var estado = $('#estado').val();
		var page = "{{ url('api/cidades_por_estado') }}/" + estado;
		$.ajax({
		    type: 'GET',
		    dataType: 'html',
		    url: page,
            async: assincrono,
		    beforeSend: function () {
			$("#cidade").prop('disabled', true);
		    },
		    success: function (msg) {
			var cidades = JSON.parse(msg);
			var options = '';
			for (var i = 0; i < cidades.length; i++) {
			    var obj = cidades[i];
			    options += '<option value="' + obj.id + '">' + obj.name + '</option>';
			}
			$("#cidade").empty();
			$("#cidade").append(options);
			$("#cidade").prop('disabled', false);
		    }
		});
	}
	$(document).ready(function () {

		$('#estado').val('{{ $clienteancine->state_id }}');
		atualizar_cidades(false);
		$('#cidade').val('{{ $clienteancine->city_id }}');
		
		@if (old('city_id') !== NULL)
		    $('#estado').val({{ old('state_id') }});
		    atualizar_cidades(false);
		    $('#cidade').val({{ old('city_id') }});
		@endif

		$('#estado').change(function () {
		    atualizar_cidades();
		});
	});
