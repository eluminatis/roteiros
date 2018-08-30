# Faker laravel

Faker oferece um meio prático de criar dados falsos para pupular seus bancos de dados para teste, em qualquer lugar do laravel você pode gerar uma instancia em pt-BR da biblioteca faker fazendo
```php

$faker = Faker\Factory::create('pt_BR');

```
	
Uma vez gerada vc pode chamar os atributos dela mesmo dentro de um loop que sempre vai sair diferente

## Principais tipos de dados

### Dados especificos para brasileiros
	
```php
	// Generates a random region name
	$faker->region; // 'Nordeste'

	// Generates a random region abbreviation
	$faker->regionAbbr; // 'NE'
	
	$faker->areaCode;  // 21
	$faker->cellphone; // 9432-5656
	$faker->landline;  // 2654-3445
	$faker->phone;     // random landline, 8-digit or 9-digit cellphone number

	// Using the phone functions with a false argument returns unformatted numbers
	$faker->cellphone(false); // 74336667

	// cellphone() has a special second argument to add the 9th digit. Ignored if generated a Radio number
	$faker->cellphone(true, true); // 98983-3945 or 7343-1290

	// Using the "Number" suffix adds area code to the phone
	$faker->cellphoneNumber;       // (11) 98309-2935
	$faker->landlineNumber(false); // 3522835934
	$faker->phoneNumber;           // formatted, random landline or cellphone (obeying the 9th digit rule)
	$faker->phoneNumberCleared;    // not formatted, random landline or cellphone (obeying the 9th digit rule)
	
	// The name generator may include double first or double last names, plus title and suffix
	$faker->name; // 'Sr. Luis Adriano Sepúlveda Filho'

	// Valid document generators have a boolean argument to remove formatting
	$faker->cpf;        // '145.343.345-76'
	$faker->cpf(false); // '45623467866'
	$faker->rg;         // '84.405.736-3'
	$faker->rg(false);  // '844057363'
	
	// Generates a Brazilian formatted and valid CNPJ
	$faker->cnpj;        // '23.663.478/0001-24'
	$faker->cnpj(false); // '23663478000124'
```	

### Textos
	
```php
	$faker->text;
	// Dolores sit sint laboriosam dolorem culpa et autem. Beatae nam sunt fugit
	// et sit et mollitia sed.
	// Fuga deserunt tempora facere magni omnis. Omnis quia temporibus laudantium
	// sit minima sint.
	
	$faker->word                                             // 'aut'
	$faker->words($nb = 3, $asText = false)                  // array('porro', 'sed', 'magni')
	$faker->sentence($nbWords = 6, $variableNbWords = true)  // 'Sit vitae voluptas sint non voluptates.'
	$faker->sentences($nb = 3, $asText = false)              // array('Optio quos qui illo error.', 'Laborum vero a officia id corporis.', 'Saepe provident esse hic eligendi.')
	$faker->paragraph($nbSentences = 3, $variableNbSentences = true) // 'Ut ab voluptas sed a nam. Sint autem inventore aut officia aut aut blanditiis. Ducimus eos odit amet et est ut eum.'
	$faker->paragraphs($nb = 3, $asText = false)             // array('Quidem ut sunt et quidem est accusamus aut. Fuga est placeat rerum ut. Enim ex eveniet facere sunt.', 'Aut nam et eum architecto fugit repellendus illo. Qui ex esse veritatis.', 'Possimus omnis aut incidunt sunt. Asperiores incidunt iure sequi cum culpa rem. Rerum exercitationem est rem.')
	$faker->text($maxNbChars = 200)
	// 'Fuga totam reiciendis qui architecto fugiat nemo. Consequatur recusandae qui cupiditate eos quod.'
	
```

### Empresas

```php
	$faker->catchPhrase             // 'Monitored regional contingency'
	$faker->bs                      // 'e-enable robust architectures'
	$faker->company                 // 'Bogan-Treutel'
	$faker->companySuffix           // 'and Sons'
	$faker->jobTitle                // 'Cashier'
```

### Pessoas

```php
	$faker->title($gender = null|'male'|'female')     // 'Ms.'
	$faker->titleMale                                 // 'Mr.'
	$faker->titleFemale                               // 'Ms.'
	$faker->suffix                                    // 'Jr.'
	$faker->name($gender = null|'male'|'female')      // 'Dr. Zane Stroman'
	$faker->firstName($gender = null|'male'|'female') // 'Maynard'
	$faker->firstNameMale                             // 'Maynard'
	$faker->firstNameFemale                           // 'Rachel'
	$faker->lastName                                  // 'Zulauf'
```
	
### Endereços

```php
	$faker->cityPrefix                          // 'Lake'
	$faker->secondaryAddress                    // 'Suite 961'
	$faker->state                               // 'NewMexico'
	$faker->stateAbbr                           // 'OH'
	$faker->citySuffix                          // 'borough'
	$faker->streetSuffix                        // 'Keys'
	$faker->buildingNumber                      // '484'
	$faker->city                                // 'West Judge'
	$faker->streetName                          // 'Keegan Trail'
	$faker->streetAddress                       // '439 Karley Loaf Suite 897'
	$faker->postcode                            // '17916'
	$faker->address                             // '8888 Cummings Vista Apt. 101, Susanbury, NY 95473'
	$faker->country                             // 'Falkland Islands (Malvinas)'
	$faker->latitude($min = -90, $max = 90)     // 77.147489
	$faker->longitude($min = -180, $max = 180)  // 86.211205
```

### Datas

```php
	$faker->unixTime($max = 'now')                // 58781813
	$faker->dateTime($max = 'now', $timezone = null) // DateTime('2008-04-25 08:37:17', 'UTC')
	$faker->dateTimeAD($max = 'now', $timezone = null) // DateTime('1800-04-29 20:38:49', 'Europe/Paris')
	$faker->iso8601($max = 'now')                 // '1978-12-09T10:10:29+0000'
	$faker->date($format = 'Y-m-d', $max = 'now') // '1979-06-09'
	$faker->time($format = 'H:i:s', $max = 'now') // '20:49:42'
	$faker->dateTimeBetween($startDate = '-30 years', $endDate = 'now', $timezone = null) // DateTime('2003-03-15 02:00:49', 'Africa/Lagos')
	$faker->dateTimeInInterval($startDate = '-30 years', $interval = '+ 5 days', $timezone = null) // DateTime('2003-03-15 02:00:49', 'Antartica/Vostok')
	$faker->dateTimeThisCentury($max = 'now', $timezone = null)     // DateTime('1915-05-30 19:28:21', 'UTC')
	$faker->dateTimeThisDecade($max = 'now', $timezone = null)      // DateTime('2007-05-29 22:30:48', 'Europe/Paris')
	$faker->dateTimeThisYear($max = 'now', $timezone = null)        // DateTime('2011-02-27 20:52:14', 'Africa/Lagos')
	$faker->dateTimeThisMonth($max = 'now', $timezone = null)       // DateTime('2011-10-23 13:46:23', 'Antarctica/Vostok')
	$faker->amPm($max = 'now')                    // 'pm'
	$faker->dayOfMonth($max = 'now')              // '04'
	$faker->dayOfWeek($max = 'now')               // 'Friday'
	$faker->month($max = 'now')                   // '06'
	$faker->monthName($max = 'now')               // 'January'
	$faker->year($max = 'now')                    // '1993'
	$faker->century                               // 'VI'
	$faker->timezone                              // 'Europe/Paris'
```

### Internet

```php
	$faker->email                   // 'tkshlerin@collins.com'
	$faker->safeEmail               // 'king.alford@example.org'
	$faker->freeEmail               // 'bradley72@gmail.com'
	$faker->companyEmail            // 'russel.durward@mcdermott.org'
	$faker->freeEmailDomain         // 'yahoo.com'
	$faker->safeEmailDomain         // 'example.org'
	$faker->userName                // 'wade55'
	$faker->password                // 'k&|X+a45*2['
	$faker->domainName              // 'wolffdeckow.net'
	$faker->domainWord              // 'feeney'
	$faker->tld                     // 'biz'
	$faker->url                     // 'http://www.skilesdonnelly.biz/aut-accusantium-ut-architecto-sit-et.html'
	$faker->slug                    // 'aut-repellat-commodi-vel-itaque-nihil-id-saepe-nostrum'
	$faker->ipv4                    // '109.133.32.252'
	$faker->localIpv4               // '10.242.58.8'
	$faker->ipv6                    // '8e65:933d:22ee:a232:f1c1:2741:1f10:117c'
	$faker->macAddress              // '43:85:B7:08:10:CA'
```

### Cartão de credito

```php
	$faker->creditCardType          // 'MasterCard'
	$faker->creditCardNumber        // '4485480221084675'
	$faker->creditCardExpirationDate // 04/13
	$faker->creditCardExpirationDateString // '04/13'
	$faker->creditCardDetails       // array('MasterCard', '4485480221084675', 'Aleksander Nowak', '04/13')
```

### Cores

```php
	$faker->hexcolor               // '#fa3cc2'
	$faker->rgbcolor               // '0,255,122'
	$faker->rgbColorAsArray        // array(0,255,122)
	$faker->rgbCssColor            // 'rgb(0,255,122)'
	$faker->safeColorName          // 'fuchsia'
	$faker->colorName              // 'Gainsbor'
```

### Arquivos

```php
	$faker->fileExtension          // 'avi'
	$faker->mimeType               // 'video/x-msvideo'
	// Copy a random file from the source to the target directory and returns the fullpath or filename
	$faker->file($sourceDir = '/tmp', $targetDir = '/tmp') // '/path/to/targetDir/13b73edae8443990be1aa8f1a483bc27.jpg'
	$faker->file($sourceDir, $targetDir, false) // '13b73edae8443990be1aa8f1a483bc27.jpg'
```

### Imagens

```php
	// Image generation provided by LoremPixel (http://lorempixel.com/)
	$faker->imageUrl($width = 640, $height = 480) // 'http://lorempixel.com/640/480/'
	$faker->imageUrl($width, $height, 'cats')     // 'http://lorempixel.com/800/600/cats/'
	$faker->imageUrl($width, $height, 'cats', true, 'Faker') // 'http://lorempixel.com/800/400/cats/Faker'
	$faker->imageUrl($width, $height, 'cats', true, 'Faker', true) // 'http://lorempixel.com/grey/800/400/cats/Faker/' Monochrome image
	$faker->image($dir = '/tmp', $width = 640, $height = 480) // '/tmp/13b73edae8443990be1aa8f1a483bc27.jpg'
	$faker->image($dir, $width, $height, 'cats')  // 'tmp/13b73edae8443990be1aa8f1a483bc27.jpg' it's a cat!
	$faker->image($dir, $width, $height, 'cats', false) // '13b73edae8443990be1aa8f1a483bc27.jpg' it's a filename without path
	$faker->image($dir, $width, $height, 'cats', true, false) // it's a no randomize images (default: `true`)
	$faker->image($dir, $width, $height, 'cats', true, true, 'Faker') // 'tmp/13b73edae8443990be1aa8f1a483bc27.jpg' it's a cat with 'Faker' text. Default, `null`.
```

### Html

```php
	//Generate HTML document which is no more than 2 levels deep, and no more than 3 elements wide at any level.
	$faker->randomHtml(2,3)   
	
	
	<html><head><title>Aut illo dolorem et accusantium eum.</title></head><body><form action="example.com" method="POST"><label for="username">sequi</label><input type="text" id="username"><label for="password">et</label><input type="password" id="password"></form><b>Id aut saepe non mollitia voluptas voluptas.</b><table><thead><tr><tr>Non consequatur.</tr><tr>Incidunt est.</tr><tr>Aut voluptatem.</tr><tr>Officia voluptas rerum quo.</tr><tr>Asperiores similique.</tr></tr></thead><tbody><tr><td>Sapiente dolorum dolorem sint laboriosam commodi qui.</td><td>Commodi nihil nesciunt eveniet quo repudiandae.</td><td>Voluptates explicabo numquam distinctio necessitatibus repellat.</td><td>Provident ut doloremque nam eum modi aspernatur.</td><td>Iusto inventore.</td></tr><tr><td>Animi nihil ratione id mollitia libero ipsa quia tempore.</td><td>Velit est officia et aut tenetur dolorem sed mollitia expedita.</td><td>Modi modi repudiandae pariatur voluptas rerum ea incidunt non molestiae eligendi eos deleniti.</td><td>Exercitationem voluptatibus dolor est iste quod molestiae.</td><td>Quia reiciendis.</td></tr><tr><td>Inventore impedit exercitationem voluptatibus rerum cupiditate.</td><td>Qui.</td><td>Aliquam.</td><td>Autem nihil aut et.</td><td>Dolor ut quia error.</td></tr><tr><td>Enim facilis iusto earum et minus rerum assumenda quis quia.</td><td>Reprehenderit ut sapiente occaecati voluptatum dolor voluptatem vitae qui velit.</td><td>Quod fugiat non.</td><td>Sunt nobis totam mollitia sed nesciunt est deleniti cumque.</td><td>Repudiandae quo.</td></tr><tr><td>Modi dicta libero quisquam doloremque qui autem.</td><td>Voluptatem aliquid saepe laudantium facere eos sunt dolor.</td><td>Est eos quis laboriosam officia expedita repellendus quia natus.</td><td>Et neque delectus quod fugit enim repudiandae qui.</td><td>Fugit soluta sit facilis facere repellat culpa magni voluptatem maiores tempora.</td></tr><tr><td>Enim dolores doloremque.</td><td>Assumenda voluptatem eum perferendis exercitationem.</td><td>Quasi in fugit deserunt ea perferendis sunt nemo consequatur dolorum soluta.</td><td>Maxime repellat qui numquam voluptatem est modi.</td><td>Alias rerum rerum hic hic eveniet.</td></tr><tr><td>Tempore voluptatem.</td><td>Eaque.</td><td>Et sit quas fugit iusto.</td><td>Nemo nihil rerum dignissimos et esse.</td><td>Repudiandae ipsum numquam.</td></tr><tr><td>Nemo sunt quia.</td><td>Sint tempore est neque ducimus harum sed.</td><td>Dicta placeat atque libero nihil.</td><td>Et qui aperiam temporibus facilis eum.</td><td>Ut dolores qui enim et maiores nesciunt.</td></tr><tr><td>Dolorum totam sint debitis saepe laborum.</td><td>Quidem corrupti ea.</td><td>Cum voluptas quod.</td><td>Possimus consequatur quasi dolorem ut et.</td><td>Et velit non hic labore repudiandae quis.</td></tr></tbody></table></body></html>
```