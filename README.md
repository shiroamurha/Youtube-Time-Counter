# Youtube-Time-Counter
The script crawler.py go into someone's Youtube profile and sums all the video time they have and displays it in the terminal.

<h2>Dependencies</h2>
<p>You must install some dependencies before running the code:</p>
<ul>
  <li>Python 3.10+ - can be downloaded at its <a href="https://www.python.org">website</a></li>
  <li>BeautifulSoup - to install open cmd/terminal and type <code>pip install bs4</code></li>
  <li>Playwright - to install open cmd/terminal and type <code>pip install playwright</code> and then <code>playwright install webkit</code></li>
</ul>
<h2>Usage</h2>
<p>After making sure all dependencies were installed correctly, download the repository <a href="https://github.com/shiroamurha/Youtube-Time-Counter/archive/refs/heads/main.zip">clicking here</a>. Windows may mark it as "virus" because it has python code, you may have to disable Windows Defender or add it to the exceptions of threats to be able to download it.</p>
<ul>
  <li>Unzip the repository file</li>
  <li>Open cmd/terminal on the file directory</li>
  <li>Run <code>py crawler.py</code>, then it should start the script</li>
  <li>It would ask you for the Youtube ID of the profile, that can be find at the profile's main page like this: </br></br><img src="https://raw.githubusercontent.com/shiroamurha/Youtube-Time-Counter/343fbdbdf264e1b12defbf06a3c0cfcdac1ea712/tutorial%20images/id_sample.png" height="300px"></li>
  <li>And finally it should take about 30 seconds to run, because it has to scroll all the Youtube page several times to load all the videos. When it's complete, it should look like this: <br><br><img src="https://github.com/shiroamurha/Youtube-Time-Counter/blob/343fbdbdf264e1b12defbf06a3c0cfcdac1ea712/tutorial%20images/output_sample.png?raw=true"> </li>
</ul>

