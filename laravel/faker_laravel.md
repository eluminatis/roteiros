# Faker laravel

Faker oferece um meio prático de criar dados falsos para pupular seus bancos de dados para teste, em qualquer lugar do laravel você pode gerar uma instancia em pt-BR da biblioteca faker fazendo

	$faker = Faker\Factory::create('pt_BR');
	
Uma vez gerada vc pode chamar os atributos dela mesmo dentro de um loop que sempre vai sair diferente

## Principais tipos de dados

### Dados especificos para brasileiros
	
	// Generates a random region name
	echo $faker->region; // 'Nordeste'

	// Generates a random region abbreviation
	echo $faker->regionAbbr; // 'NE'
	
	echo $faker->areaCode;  // 21
	echo $faker->cellphone; // 9432-5656
	echo $faker->landline;  // 2654-3445
	echo $faker->phone;     // random landline, 8-digit or 9-digit cellphone number

	// Using the phone functions with a false argument returns unformatted numbers
	echo $faker->cellphone(false); // 74336667

	// cellphone() has a special second argument to add the 9th digit. Ignored if generated a Radio number
	echo $faker->cellphone(true, true); // 98983-3945 or 7343-1290

	// Using the "Number" suffix adds area code to the phone
	echo $faker->cellphoneNumber;       // (11) 98309-2935
	echo $faker->landlineNumber(false); // 3522835934
	echo $faker->phoneNumber;           // formatted, random landline or cellphone (obeying the 9th digit rule)
	echo $faker->phoneNumberCleared;    // not formatted, random landline or cellphone (obeying the 9th digit rule)
	
	// The name generator may include double first or double last names, plus title and suffix
	echo $faker->name; // 'Sr. Luis Adriano Sepúlveda Filho'

	// Valid document generators have a boolean argument to remove formatting
	echo $faker->cpf;        // '145.343.345-76'
	echo $faker->cpf(false); // '45623467866'
	echo $faker->rg;         // '84.405.736-3'
	echo $faker->rg(false);  // '844057363'
	
	// Generates a Brazilian formatted and valid CNPJ
	echo $faker->cnpj;        // '23.663.478/0001-24'
	echo $faker->cnpj(false); // '23663478000124'
	
### Textos
	
	echo $faker->text;
	// Dolores sit sint laboriosam dolorem culpa et autem. Beatae nam sunt fugit
	// et sit et mollitia sed.
	// Fuga deserunt tempora facere magni omnis. Omnis quia temporibus laudantium
	// sit minima sint.
	
	word                                             // 'aut'
	words($nb = 3, $asText = false)                  // array('porro', 'sed', 'magni')
	sentence($nbWords = 6, $variableNbWords = true)  // 'Sit vitae voluptas sint non voluptates.'
	sentences($nb = 3, $asText = false)              // array('Optio quos qui illo error.', 'Laborum vero a officia id corporis.', 'Saepe provident esse hic eligendi.')
	paragraph($nbSentences = 3, $variableNbSentences = true) // 'Ut ab voluptas sed a nam. Sint autem inventore aut officia aut aut blanditiis. Ducimus eos odit amet et est ut eum.'
	paragraphs($nb = 3, $asText = false)             // array('Quidem ut sunt et quidem est accusamus aut. Fuga est placeat rerum ut. Enim ex eveniet facere sunt.', 'Aut nam et eum architecto fugit repellendus illo. Qui ex esse veritatis.', 'Possimus omnis aut incidunt sunt. Asperiores incidunt iure sequi cum culpa rem. Rerum exercitationem est rem.')
	text($maxNbChars = 200)
	// 'Fuga totam reiciendis qui architecto fugiat nemo. Consequatur recusandae qui cupiditate eos quod.'
	
### Empresas

	catchPhrase             // 'Monitored regional contingency'
	bs                      // 'e-enable robust architectures'
	company                 // 'Bogan-Treutel'
	companySuffix           // 'and Sons'
	jobTitle                // 'Cashier'
	
### Pessoas

	title($gender = null|'male'|'female')     // 'Ms.'
	titleMale                                 // 'Mr.'
	titleFemale                               // 'Ms.'
	suffix                                    // 'Jr.'
	name($gender = null|'male'|'female')      // 'Dr. Zane Stroman'
	firstName($gender = null|'male'|'female') // 'Maynard'
	firstNameMale                             // 'Maynard'
	firstNameFemale                           // 'Rachel'
	lastName                                  // 'Zulauf'

	
### Endereços

	cityPrefix                          // 'Lake'
	secondaryAddress                    // 'Suite 961'
	state                               // 'NewMexico'
	stateAbbr                           // 'OH'
	citySuffix                          // 'borough'
	streetSuffix                        // 'Keys'
	buildingNumber                      // '484'
	city                                // 'West Judge'
	streetName                          // 'Keegan Trail'
	streetAddress                       // '439 Karley Loaf Suite 897'
	postcode                            // '17916'
	address                             // '8888 Cummings Vista Apt. 101, Susanbury, NY 95473'
	country                             // 'Falkland Islands (Malvinas)'
	latitude($min = -90, $max = 90)     // 77.147489
	longitude($min = -180, $max = 180)  // 86.211205
	
### Datas

	unixTime($max = 'now')                // 58781813
	dateTime($max = 'now', $timezone = null) // DateTime('2008-04-25 08:37:17', 'UTC')
	dateTimeAD($max = 'now', $timezone = null) // DateTime('1800-04-29 20:38:49', 'Europe/Paris')
	iso8601($max = 'now')                 // '1978-12-09T10:10:29+0000'
	date($format = 'Y-m-d', $max = 'now') // '1979-06-09'
	time($format = 'H:i:s', $max = 'now') // '20:49:42'
	dateTimeBetween($startDate = '-30 years', $endDate = 'now', $timezone = null) // DateTime('2003-03-15 02:00:49', 'Africa/Lagos')
	dateTimeInInterval($startDate = '-30 years', $interval = '+ 5 days', $timezone = null) // DateTime('2003-03-15 02:00:49', 'Antartica/Vostok')
	dateTimeThisCentury($max = 'now', $timezone = null)     // DateTime('1915-05-30 19:28:21', 'UTC')
	dateTimeThisDecade($max = 'now', $timezone = null)      // DateTime('2007-05-29 22:30:48', 'Europe/Paris')
	dateTimeThisYear($max = 'now', $timezone = null)        // DateTime('2011-02-27 20:52:14', 'Africa/Lagos')
	dateTimeThisMonth($max = 'now', $timezone = null)       // DateTime('2011-10-23 13:46:23', 'Antarctica/Vostok')
	amPm($max = 'now')                    // 'pm'
	dayOfMonth($max = 'now')              // '04'
	dayOfWeek($max = 'now')               // 'Friday'
	month($max = 'now')                   // '06'
	monthName($max = 'now')               // 'January'
	year($max = 'now')                    // '1993'
	century                               // 'VI'
	timezone                              // 'Europe/Paris'
	
### Internet

	email                   // 'tkshlerin@collins.com'
	safeEmail               // 'king.alford@example.org'
	freeEmail               // 'bradley72@gmail.com'
	companyEmail            // 'russel.durward@mcdermott.org'
	freeEmailDomain         // 'yahoo.com'
	safeEmailDomain         // 'example.org'
	userName                // 'wade55'
	password                // 'k&|X+a45*2['
	domainName              // 'wolffdeckow.net'
	domainWord              // 'feeney'
	tld                     // 'biz'
	url                     // 'http://www.skilesdonnelly.biz/aut-accusantium-ut-architecto-sit-et.html'
	slug                    // 'aut-repellat-commodi-vel-itaque-nihil-id-saepe-nostrum'
	ipv4                    // '109.133.32.252'
	localIpv4               // '10.242.58.8'
	ipv6                    // '8e65:933d:22ee:a232:f1c1:2741:1f10:117c'
	macAddress              // '43:85:B7:08:10:CA'
	
### Cartão de credito

	creditCardType          // 'MasterCard'
	creditCardNumber        // '4485480221084675'
	creditCardExpirationDate // 04/13
	creditCardExpirationDateString // '04/13'
	creditCardDetails       // array('MasterCard', '4485480221084675', 'Aleksander Nowak', '04/13')
	
### Cores

	hexcolor               // '#fa3cc2'
	rgbcolor               // '0,255,122'
	rgbColorAsArray        // array(0,255,122)
	rgbCssColor            // 'rgb(0,255,122)'
	safeColorName          // 'fuchsia'
	colorName              // 'Gainsbor'
	
### Arquivos

	fileExtension          // 'avi'
	mimeType               // 'video/x-msvideo'
	// Copy a random file from the source to the target directory and returns the fullpath or filename
	file($sourceDir = '/tmp', $targetDir = '/tmp') // '/path/to/targetDir/13b73edae8443990be1aa8f1a483bc27.jpg'
	file($sourceDir, $targetDir, false) // '13b73edae8443990be1aa8f1a483bc27.jpg'
	
### Imagens

	// Image generation provided by LoremPixel (http://lorempixel.com/)
	imageUrl($width = 640, $height = 480) // 'http://lorempixel.com/640/480/'
	imageUrl($width, $height, 'cats')     // 'http://lorempixel.com/800/600/cats/'
	imageUrl($width, $height, 'cats', true, 'Faker') // 'http://lorempixel.com/800/400/cats/Faker'
	imageUrl($width, $height, 'cats', true, 'Faker', true) // 'http://lorempixel.com/grey/800/400/cats/Faker/' Monochrome image
	image($dir = '/tmp', $width = 640, $height = 480) // '/tmp/13b73edae8443990be1aa8f1a483bc27.jpg'
	image($dir, $width, $height, 'cats')  // 'tmp/13b73edae8443990be1aa8f1a483bc27.jpg' it's a cat!
	image($dir, $width, $height, 'cats', false) // '13b73edae8443990be1aa8f1a483bc27.jpg' it's a filename without path
	image($dir, $width, $height, 'cats', true, false) // it's a no randomize images (default: `true`)
	image($dir, $width, $height, 'cats', true, true, 'Faker') // 'tmp/13b73edae8443990be1aa8f1a483bc27.jpg' it's a cat with 'Faker' text. Default, `null`.
	
### Html

	//Generate HTML document which is no more than 2 levels deep, and no more than 3 elements wide at any level.
	randomHtml(2,3)   
	
	
	<html><head><title>Aut illo dolorem et accusantium eum.</title></head><body><form action="example.com" method="POST"><label for="username">sequi</label><input type="text" id="username"><label for="password">et</label><input type="password" id="password"></form><b>Id aut saepe non mollitia voluptas voluptas.</b><table><thead><tr><tr>Non consequatur.</tr><tr>Incidunt est.</tr><tr>Aut voluptatem.</tr><tr>Officia voluptas rerum quo.</tr><tr>Asperiores similique.</tr></tr></thead><tbody><tr><td>Sapiente dolorum dolorem sint laboriosam commodi qui.</td><td>Commodi nihil nesciunt eveniet quo repudiandae.</td><td>Voluptates explicabo numquam distinctio necessitatibus repellat.</td><td>Provident ut doloremque nam eum modi aspernatur.</td><td>Iusto inventore.</td></tr><tr><td>Animi nihil ratione id mollitia libero ipsa quia tempore.</td><td>Velit est officia et aut tenetur dolorem sed mollitia expedita.</td><td>Modi modi repudiandae pariatur voluptas rerum ea incidunt non molestiae eligendi eos deleniti.</td><td>Exercitationem voluptatibus dolor est iste quod molestiae.</td><td>Quia reiciendis.</td></tr><tr><td>Inventore impedit exercitationem voluptatibus rerum cupiditate.</td><td>Qui.</td><td>Aliquam.</td><td>Autem nihil aut et.</td><td>Dolor ut quia error.</td></tr><tr><td>Enim facilis iusto earum et minus rerum assumenda quis quia.</td><td>Reprehenderit ut sapiente occaecati voluptatum dolor voluptatem vitae qui velit.</td><td>Quod fugiat non.</td><td>Sunt nobis totam mollitia sed nesciunt est deleniti cumque.</td><td>Repudiandae quo.</td></tr><tr><td>Modi dicta libero quisquam doloremque qui autem.</td><td>Voluptatem aliquid saepe laudantium facere eos sunt dolor.</td><td>Est eos quis laboriosam officia expedita repellendus quia natus.</td><td>Et neque delectus quod fugit enim repudiandae qui.</td><td>Fugit soluta sit facilis facere repellat culpa magni voluptatem maiores tempora.</td></tr><tr><td>Enim dolores doloremque.</td><td>Assumenda voluptatem eum perferendis exercitationem.</td><td>Quasi in fugit deserunt ea perferendis sunt nemo consequatur dolorum soluta.</td><td>Maxime repellat qui numquam voluptatem est modi.</td><td>Alias rerum rerum hic hic eveniet.</td></tr><tr><td>Tempore voluptatem.</td><td>Eaque.</td><td>Et sit quas fugit iusto.</td><td>Nemo nihil rerum dignissimos et esse.</td><td>Repudiandae ipsum numquam.</td></tr><tr><td>Nemo sunt quia.</td><td>Sint tempore est neque ducimus harum sed.</td><td>Dicta placeat atque libero nihil.</td><td>Et qui aperiam temporibus facilis eum.</td><td>Ut dolores qui enim et maiores nesciunt.</td></tr><tr><td>Dolorum totam sint debitis saepe laborum.</td><td>Quidem corrupti ea.</td><td>Cum voluptas quod.</td><td>Possimus consequatur quasi dolorem ut et.</td><td>Et velit non hic labore repudiandae quis.</td></tr></tbody></table></body></html>
