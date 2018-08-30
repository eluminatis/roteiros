Como configurar corretamente o accordion bootstrap para se montar dinamicamente com os videos do bd

	- o id do panel-group que envolve tudo deve ser o mesmo do data-parent dos button do panel-title
	- o id do panel-collapse deve ser colocado em href e aria-controls do button do panel-title
	- o id do panel-heading deve ser colocado em aria-labelledby no panel-collapse
