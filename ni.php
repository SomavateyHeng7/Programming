<script>
	// Get the first paragraph using document.querySelector(tag name)
	const firstParagraph = document.querySelector('p');

	// Get the second paragraph using document.querySelector('#id') and by their id
	const secondParagraph = document.querySelector('#second');

	// Get the third paragraph using document.querySelector('#id') and by their id
	const thirdParagraph = document.querySelector('#third');

	// Get all the p as node List using document.querySelectorAll(tag name) and by their tag name
	const allParagraphs = document.querySelectorAll('p');

	// Loop through the node list and get the text content of each paragraph
	allParagraphs.forEach((paragraph) => {
		console.log(paragraph.textContent);
	});

	// Set a text content to paragraph the fourth paragraph, Fourth Paragraph
	const fourthParagraph = document.querySelector('.fourth');
	fourthParagraph.textContent = 'Fourth Paragraph';

	// Set id and class attribute for all the paragraphs using different attribute setting methods
	firstParagraph.id = 'first';
	secondParagraph.className = 'second';
	thirdParagraph.setAttribute('class', 'third');

	// Create a div container on an HTML document and create 100 to 100 numbers dynamically and append to the container div
	const containerDiv = document.createElement('div');

	for (let i = 1; i <= 100; i++) {
		const numberDiv = document.createElement('div');
		numberDiv.textContent = i;

		if (i % 2 === 0) {
			numberDiv.classList.add('green');
		} else {
			numberDiv.classList.add('yellow');
		}

		if (isPrime(i)) {
			numberDiv.classList.add('red');
		}

		containerDiv.appendChild(numberDiv);
	}

	document.body.appendChild(containerDiv);

	// Check if a number is prime
	function isPrime(num) {
		if (num <= 1) {
			return false;
		}

		for (let i = 2; i <= Math.sqrt(num); i++) {
			if (num % i === 0) {
				return false;
			}
		}

		return true;
	}
</script>