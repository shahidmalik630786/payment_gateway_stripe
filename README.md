<h1>Django Payment Gateway with Stripe</h1>

<p>This project implements a payment gateway using Stripe within a Django application. It is designed for testing and development purposes, following the official Stripe documentation. The project enables seamless payment processing and can be extended for production use with proper configuration.</p>

<h2>📑 Table of Contents</h2>

<ul>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#prerequisites">Prerequisites</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#configuration">Configuration</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#important-notes">Important Notes</a></li>
  <li><a href="#testing">Testing</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h2 id="overview">📌 Overview</h2>

<p>The Django Payment Gateway with Stripe project integrates Stripe's payment processing capabilities into a Django web application. It supports payment transfers for testing purposes and is built to handle client requirements where Stripe is a preferred payment gateway.</p>

<h3>Key Features:</h3>
<ul>
  <li>✅ Stripe payment gateway integration.</li>
  <li>✅ Test mode for safe payment simulations.</li>
  <li>✅ Easy-to-configure Django settings for Stripe API keys.</li>
  <li>✅ Follows Stripe's official documentation for secure and reliable implementation.</li>
</ul>

<h2 id="prerequisites">🧰 Prerequisites</h2>

<ul>
  <li>Python 3.8+</li>
  <li>Django 3.2+</li>
  <li>Stripe account (Test or Live mode)</li>
  <li>Stripe Python library (<code>stripe</code>)</li>
  <li>A valid Stripe API key (Test or Live)</li>
  <li>Virtual environment (recommended)</li>
</ul>

<p><strong>Note:</strong> Stripe is not available in India. To create a Stripe account, use a location such as the United States or any other supported country. Refer to Stripe's <a href="https://stripe.com/global">supported countries</a> for details.</p>

<h2 id="installation">⚙️ Installation</h2>

<ol>
  <li><strong>Clone the repository:</strong></li>

<pre><code>git clone https://github.com/your-username/django-payment-gateway-stripe.git
cd django-payment-gateway-stripe</code></pre>

  <li><strong>Set up a virtual environment:</strong></li>

<pre><code>python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate</code></pre>

  <li><strong>Install dependencies:</strong></li>

<pre><code>pip install -r requirements.txt</code></pre>

  <li><strong>Install the Stripe Python library:</strong></li>

<pre><code>pip install stripe</code></pre>
</ol>

<h2 id="configuration">🔧 Configuration</h2>

<ol>
  <li>Set up Stripe API keys:</li>
  <p>Obtain your Test or Live API keys from the <a href="https://dashboard.stripe.com/apikeys">Stripe Dashboard</a>.</p>

  <p>Add the keys to your Django <code>settings.py</code>:</p>

<pre><code>STRIPE_PUBLIC_KEY = 'your-publishable-key'
STRIPE_SECRET_KEY = 'your-secret-key'</code></pre>

  <li>Apply database migrations:</li>
<pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>

  <li>Create a superuser (optional):</li>
<pre><code>python manage.py createsuperuser</code></pre>

  <li>Run the development server:</li>
<pre><code>python manage.py runserver</code></pre>
</ol>

<h2 id="usage">🚀 Usage</h2>

<ol>
  <li>Navigate to the payment page (e.g., <code>http://localhost:8000/payment/</code>).</li>
  <li>Enter test card details:
    <ul>
      <li>Card Number: <code>4242 4242 4242 4242</code></li>
      <li>Expiry Date: Any future date</li>
      <li>CVC: Any 3-digit number</li>
    </ul>
  </li>
  <li>Submit the payment to simulate a transaction.</li>
  <li>Check the Stripe Dashboard to verify the payment status.</li>
</ol>

<h2 id="important-notes">❗ Important Notes</h2>

<ul>
  <li><strong>Stripe Availability:</strong> Stripe does not operate in India. Use a supported country (e.g., US, UK, Canada) to create and test your Stripe account.</li>
  <li><strong>Test Mode:</strong> Always use Stripe's test keys during development to avoid real transactions.</li>
  <li><strong>Client Requirements:</strong> Stripe is a popular choice for clients due to its reliability and global support. Ensure you configure the project to meet specific client needs.</li>
  <li><strong>Security:</strong> Never expose your Stripe secret key in client-side code or public repositories.</li>
</ul>

<h2 id="testing">🧪 Testing</h2>

<ul>
  <li>Use Stripe's test card numbers for payment simulations.</li>
  <li>Monitor logs in the Stripe Dashboard to debug issues.</li>
  <li>Run Django tests (if implemented):</li>
</ul>

<pre><code>python manage.py test</code></pre>

<h2 id="contributing">🤝 Contributing</h2>

<p>Contributions are welcome! Please follow these steps:</p>

<ol>
  <li>Fork the repository.</li>
  <li>Create a new branch: <code>git checkout -b feature/your-feature</code></li>
  <li>Commit your changes: <code>git commit -m "Add your feature"</code></li>
  <li>Push to the branch: <code>git push origin feature/your-feature</code></li>
  <li>Open a pull request.</li>
</ol>

<h2 id="license">📄 License</h2>

<p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>
