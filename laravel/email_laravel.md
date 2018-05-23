# Email com laravel

#### FROM

Se todos os email's enviados pelo seu app forem ter o mesmo endereço de remetente, você não precisar ficar definindo isso a cada envio, basta criar e configurar as seguintes variaveis em seu .env

	MAIL_FROM_ADDRESS=seuemail@exemplo.com
	MAIL_FROM_NAME=SeuNome
	
caso cada email possa ter um remetente diferente configure diretamente no ->from do metodo build

	public function build()
	{
	    return $this->from('example@example.com')
			->view('emails.orders.shipped');
	}
	
### Mailables

Cada tipo de email disparado por seu app é representado por uma classe mailable, você deve gerar asssim:
	
	php artisan make:mail SeuMailable
	
Toda a configuração é feita no build. Dentro deste método, você pode chamar vários métodos, como from, subject, view, e attach para configurar apresentação e entrega do e-mail.

	public function build()
	{
	    return $this->from('example@example.com')
			->subject('Seu assunto')
			->view('emails.seuTemplate')
			->attach('caminho para o anexo se necessário');
	}
	
Ao anexar arquivos a uma mensagem, você também pode especificar o nome de exibição e / ou o tipo MIME, passando um arraysegundo argumento para o attachmétodo:

	public function build()
	{
	    return $this->from('example@example.com')
			->subject('Seu assunto')
			->view('emails.seuTemplate')
			->attach('/path/to/file', [
		                'as' => 'name.pdf',
		                'mime' => 'application/pdf',
			]);
			
			//também existe o ->text('texto desagatemelizado') para textos planos
	}
	
## Passando variaveis para a classe Mailable

Você deve definir variavei publicas na classe mailable e passar variaveis pelo contrutor para ela e automaticamente ela estara disponivel dentro de sua view
 
	<?php

	namespace App\Mail;

	use App\Order;
	use Illuminate\Bus\Queueable;
	use Illuminate\Mail\Mailable;
	use Illuminate\Queue\SerializesModels;

	class OrderShipped extends Mailable
	{
	    use Queueable, SerializesModels;

	    /**
	     * a variavel que recebe um array de variveis que vc queira 			passar
	     */
	    public $data;

	    /**
	     * o construtor recebe a variavel e a joga dentra da var publica
	     * e agora vc pode usa-la dentro da view
	     */
	    public function __construct($data)
	    {
		$this->data = $data;
	    }

	    /**
	     * Build the message.
	     *
	     * @return $this
	     */
	    public function build()
	    {
		return $this->view('emails.template');
	    }
	}
	
Depois de os dados serem passados pelo construtor e definidos como propriedade publica, você poderá acessá-los de dentro da view

	<div>
	    <p>Preço: {{ $data['var1'] }}</p>
	</div>
	
## Inserindo imagens no corpo do email

o laravel disponibiliza a variavel $message nos mailables com alguns metodos que facilitam seu trabalho, um deles é o método de inserir imagens no corpo do email, na view coloque a imagem da seguinte forma

	<body>
	    Aqui temos um exemplo de inserção de imagem no corpo
	    
	    <img src="{{ $message->embed(asset('images/email_rodape.png')) }}">
	</body>
	
## Enviando emails

no seu controller registre o uso da fachade Illuminate\Support\Facades\Mail e o seu mailable App\Mail\SeuMailable. Feito isso é só chamar o método Mail::to('destinatario')->send(New SeuMailable($vars))

O to() aceita um endereço de email, uma instância do usuário ou uma coleção de usuários. Se você passar um objeto ou uma coleção de objetos, o programa de email usará automaticamente as propriedades email e name ao configurar os destinatários de e-mail

	<?php

	namespace App\Http\Controllers;

	use App\Http\Controllers\Controller;
	use App\Mail\SeuMailable; //importando seu mailable
	use Illuminate\Support\Facades\Mail; //importando facade de emails

	class OrderController extends Controller
	{
	    /**
	     * Envia um email qualquer a um tolo qualquer
	     */
	    public function enviaEmail(){
			$data['var1'] = 'bla bla bla';
			$data['var2'] = 'ble ble ble';
			
			Mail::to('email@destinatario.com')->send(new SeuMailable($data));
			
			ou
			
			Mail::to('email@destinatario.com')
				->cc($moreUsers)
				->bcc($evenMoreUsers)
				->send(new SeuMailable($data));
			
	    }
	}

## Visualizando mailables no navegador

Para fins de desenvolvimento vc pode visualizar seus mailables no navegador simplesmente retornando-o na rota de testes

	Route::get('/mailable_teste', function () {
		$data['var1'] = 'bla bla bla';
		$data['var2'] = 'ble ble ble';

		return new App\Mail\SeuMailable($data);
	});

























