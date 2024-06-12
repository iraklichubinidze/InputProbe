<h1 align="center" id="title">InputProbe</h1>

<p align="center"><img src="https://i.postimg.cc/X7SGdyT5/86d8d3b6995ddad46f5d9142354b65b1.png" alt="project-image"></p>

<p id="description">InputProbe is a powerful tool designed for penetration testers to enhance their attack vector by gathering URLs recursively from a specified webpage. It intelligently parses the source code of the provided page extracting URLs and displaying all input fields found within these URLs. This tool is invaluable for conducting a variety of attacks including SQL injection (SQLi) cross-site scripting (XSS) server-side template injection (SSTI) code injection and many other injection attacks.</p>

<h2>Usage</h2>
<p>Run the script with the following command:</p>
<pre><code>python inputprobe.py &lt;url&gt; [--recursive] [-o OUTPUT_FILE] [-u USER_AGENT] [-t THREADS]</code></pre>
    <ul>
        <li><code>&lt;url&gt;</code>: The URL to start with.</li>
        <li><code>--recursive</code>: (Optional) Enable recursive URL grabbing.</li>
        <li><code>-o OUTPUT_FILE</code>: (Optional) Specify an output file to write input fields.</li>
        <li><code>-u USER_AGENT</code>: (Optional) Specify a custom user agent.</li>
        <li><code>-t THREADS</code>: (Optional) Specify the number of threads to use (default: 5).</li>
    </ul>
<p>For example:</p>
<pre><code>python inputprobe.py https://example.com --recursive -o output.txt -u "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" -t 10</code></pre>
<p>This will fetch URLs from the given webpage recursively, display input fields found within those URLs, and write the input fields to the specified output file if provided. It will also use 10 threads for concurrent URL fetching.</p>
<br>
<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the repository:</p>

```
git clone https://github.com/iraklichubinidze/inputprobe.git
```

<p>2. Navigate to the directory:</p>

```
cd inputprobe
```

<p>3. Install the dependencies:</p>

```
pip install -r requirements.txt
```
