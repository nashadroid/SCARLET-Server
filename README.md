SCARLET Python Webserver
========================

A simple web server to transfer objects between machines in the lab


This page details how to set up, update, and test the Scarlet Data Server. Note: This is not the instructions for the client side devices.
<h2></h2>
<h2>Prerequisites:</h2>
<strong>Python</strong> - I have tested with Python 3.6 - 3.8. The server uses only the standard library, so no additional packages need to be installed.

<strong>Git -</strong> Recommended, but not required.

&nbsp;

&nbsp;
<h1><strong>Part 1: Downloading the Code</strong></h1>
<span style="color: #ff0000;"><strong>This part requires you to be connected to the internet.</strong></span>

&nbsp;
<h2>a) Fresh Install (Skip to Part b if previously installed)</h2>
<h3>Option 1: Download with Git (recommended)</h3>
The easiest way to do this is by using Git. This will allow for easy updating and back ups in the future.

To do this, open a terminal and navigate to the folder where you want the server folder to be in (Git will create a new folder containing all the project files):
<blockquote>cd path/to/where/to/install</blockquote>
In the terminal, run the command:
<blockquote>git clone https://github.com/nashadroid/SCARLET-Server</blockquote>
&nbsp;
<h3>Option 2: Direct download from Github.com</h3>
Using a browser, navigate to https://github.com/nashadroid/SCARLET-Server .

Click the green download code button

<a href="https://u.osu.edu/laserdocs/files/2020/11/Screen-Shot-2020-11-19-at-6.01.40-PM.png"><img class="size-medium wp-image-393 aligncenter" src="https://u.osu.edu/laserdocs/files/2020/11/Screen-Shot-2020-11-19-at-6.01.40-PM-300x74.png" alt="" width="300" height="74" /></a>

Move the downloaded zip file to where you want the server folder to be. Then, open a terminal and navigate to the zip file:
<blockquote>cd path/to/folder/containing/zip</blockquote>
Then unzip the folder:
<blockquote>unzip SCARLET-Server.zip</blockquote>
&nbsp;
<h2>b) Update/Refresh Code (Skip this part if you just did Part a)</h2>
Open a terminal and navigate to the folder where you have ScarletServer:
<blockquote>cd path/to/SCARLET-Server/</blockquote>
Use git to update from the origin:
<blockquote>git pull origin master</blockquote>
This should be all you have to do. <strong>Only if the above does not work and it gives you conflicts:</strong>
<blockquote>git stash

git pull</blockquote>
&nbsp;

&nbsp;
<h1><strong>Part 2: Configuring the Server</strong></h1>
<span style="color: #ff0000;"><strong>This part requires you to be connected to SCARLETNET (No www internet connection)</strong></span>

There are some options which can be toggled in the server. The main one that should be worried about is the ip address.

&nbsp;
<h3>Setting Server IP</h3>
The IP address of the machine running the server must be saved in the file titled "ip.txt". This will be the local IP, not the public IP, so it will be different than the one displayed on whatismyip.com .

The local ip can be found in several different ways, an easy one being
<blockquote>
<p class="p1"><span class="s1">hostname –I</span></p>
</blockquote>
If that doesn't work, try some of the other options described <a href="https://phoenixnap.com/kb/how-to-find-ip-address-linux">here</a>. The local IP address can also be found in network settings/preferences. <strong>Note: This is not the router ip, which likely ends in .0 or .1</strong>
<h4></h4>
<h3>Other settings</h3>
Other settings which can be toggled are at the top of the file titled "ScarletServer.py". This includes:
<ul>
 	<li>overWriteFiles - Default is False, which means files cannot be overwritten from the client side. Set to True to enable overwriting of files.</li>
 	<li>sortFilesByDay - Default is False, set to True if you would like the server to force sorting files by day.</li>
 	<li>port - Default is 8080 , probably don't change this one.</li>
</ul>
&nbsp;
<h1><strong>Part 3: Running the Server</strong></h1>
Navigate to within the Server folder:
<blockquote>cd SCARLET-Server/</blockquote>
Start Running the server. This may be different based on what your Python is aliased as:
<blockquote>python ScarletServer.py</blockquote>
And then you should receive a message similar to "<span class="s1">Starting server at ip: 192.168.0.9:8080</span><span class="s1">"</span>

<span class="s1">If no errors are thrown after that line and Python continues running, the server should be working.</span>

&nbsp;
<h1><strong>Part 4: Check the server is running</strong></h1>
Use a web browser and go to the ip address and port listed by the server. You should enter exactly where the server says it's running into the URL bar of your browser, something along the lines of: <span class="s1">192.168.0.9:8080</span>

You should see a plain text webpage that looks similar to this:

<a href="https://u.osu.edu/laserdocs/files/2020/11/Screen-Shot-2020-11-19-at-10.29.10-PM.png"><img class="alignnone size-medium wp-image-396" src="https://u.osu.edu/laserdocs/files/2020/11/Screen-Shot-2020-11-19-at-10.29.10-PM-300x98.png" alt="" width="300" height="98" /></a>

The Placeholder text is just there for testing purposes. Any text values sent to the server will also end up here. Test this on other devices on the same network to ensure the ports are working properly. If using within the Scarlet-intranet, this means needing a wired connection to the local network (without access to internet).

Next set up the client on any device on the same network to send data to the server. Any device that can access the webpage at the server url should be able to send data through the clients.

&nbsp;
