# Z-Score-Analysis-based-Smart-Street-lighting-System
We have often seen the street lights kept 'turn on' during the day and sometime there is no one to switch it on. Now the manual approach needs to be replaced with automated technologies.  So, here is the way to automate on/off ,automate brightness and save some energy using Anomaly Detection on the basis of Z-Score Method.
In this, I have tried to implement the automation with the  approach of <strong>Anomaly Detection</strong> on the basis of <strong> Z-Score Method </strong>using LDR sensor.
The optimity with this method is that it regulates the 'ON' or 'OFF' of lights and the intensity (brightness) of light  on the analysis of few datas recorded by the sensor just sometime before and  then prediction is made whether to turn ON/OFF the lights. 
<!-- wp:heading -->
<h2>Things used in the project</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":3} -->
<h3>Hardware components</h3>
<!-- /wp:heading -->

<!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:heading {"level":4} -->
<h4>1. Bolt wi-fi module </h4>
<!-- /wp:heading -->

<!-- wp:image {"id":15331,"width":568,"height":264,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/wifi-module-rotated.jpg" alt="" class="wp-image-15331" width="568" height="264"/></figure>
<!-- /wp:image --></div></div>
<!-- /wp:group -->

<!-- wp:heading {"level":4} -->
<h4>2. LDR</h4>
<!-- /wp:heading -->

<!-- wp:image {"id":15332,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/ldr-2.jpg" alt="" class="wp-image-15332"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4>3.RESISTOR 10k ohm(brown black orange color code)</h4>
<!-- /wp:heading -->

<!-- wp:image {"id":15333,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/R.jpg" alt="" class="wp-image-15333"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4>4.USB cable</h4>
<!-- /wp:heading -->

<!-- wp:image {"id":15334,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/usb-cable.jpg" alt="" class="wp-image-15334"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4>5.LEDs----x2</h4>
<!-- /wp:heading -->

<!-- wp:image {"id":15335,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/LEDS.jpg" alt="" class="wp-image-15335"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4>6.Breadboard</h4>
<!-- /wp:heading -->

<!-- wp:image {"id":15336,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/BREADBOARD.jpg" alt="" class="wp-image-15336"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4>7.Connecting wires</h4>
<!-- /wp:heading -->

<!-- wp:image {"id":15337,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/WIRES.jpg" alt="" class="wp-image-15337"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":3} -->
<h3>Software Used</h3>
<!-- /wp:heading -->

<!-- wp:heading {"level":4} -->
<h4>1.Replit online IDE</h4>
<!-- /wp:heading -->

<!-- wp:heading -->
<h2>Hardware Setup</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>Step 1.- Connect the LDR's one leg to the A0 pin and the other leg to the 3V3 pin.</li><li>Step-2.- Connect the resistors one leg to the A0 pin and  the other leg to the gnd pin. Breadboard is used for obtaining better stability:-</li></ul>
<!-- /wp:list -->

<!-- wp:image {"id":15322,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/1-rotated.jpg" alt="" class="wp-image-15322"/></figure>
<!-- /wp:image -->

<!-- wp:list -->
<ul><li>Step-3.- Now connect the LEDs longer leg to the '0' pin and the shorter leg to the gnd pin. Refer to the image for breadboard connection:- </li></ul>
<!-- /wp:list -->

<!-- wp:image {"id":15323,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/cover-image-1-rotated.jpg" alt="" class="wp-image-15323"/></figure>
<!-- /wp:image -->

<!-- wp:list -->
<ul><li>Step-4.- Connect the wi-fi module to the source using a USB cable and to a proper wifi. </li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Software Programming</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For this I have used an online IDE Replit. **One can  use DigitalOcean droplet /VirtualBox/VMWare or Linux as per them accordingly.**</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p> The steps for software programming using Replit is given:-</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Step-1.- Open the Replit website-&gt; SIGN UP/SIGN IN -&gt; Create a new repl of python.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Step-2.- In the shell install boltiot library using command 'pip3 install boltiot'.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Step-3.- Write down the code in main.py.</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><strong>A) importing all the required libraries</strong>

<code>import json, time, math, statistics
from boltiot import  Bolt</code>

<strong>B).The following code helps define a function which calculates the Z-score and the using the Z-score calculates the boundaries required for anomaly detection.</strong>

def compute_bounds(history_data,frame_size,factor):

<strong>The above line helps define a function, which takes 3 input variables: hisotry_data, frame_size and factor.</strong>

if len(history_data)&lt;frame_size : return None if len(history_data)&gt;frame_size : del history_data[0:len(history_data)-frame_size]

 <strong>This abovecode checks whether enough data has been accumulated to calculate the Z-score, and if there is too much data, then the code deletes the older data.</strong>

<strong>C). Now calculating mean,variance, Zn and lower bound /upper bound :-</strong>

Mn=statistics.mean(history_data)
Variance=0 
for data in history_data : Variance += math.pow((data-Mn),2)
Zn = factor * math.sqrt(Variance / frame_size)
High_bound = history_data[frame_size-1]+Zn 
Low_bound = history_data[frame_size-1]-Zn return [High_bound,Low_bound]

D). Now declare the vlues of FRAME_SIZE,MUL_FACTOR,your api_key and your device_id.
Code snippet is shared for reference:-</pre>
<!-- /wp:preformatted -->

<!-- wp:image {"id":15338,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/Screenshot-162.png" alt="" class="wp-image-15338"/></figure>
<!-- /wp:image -->

<!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:paragraph -->
<p><strong>E). This code is to initiate Bolt</strong> <strong>by creating an object of bolt.</strong></p>
<!-- /wp:paragraph -->

<!-- wp:group -->
<div class="wp-block-group"><div class="wp-block-group__inner-container"><!-- wp:paragraph -->
<p>mybolt = Bolt(api_key,device_id)</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p> history_data=[]</p>
<!-- /wp:paragraph --></div></div>
<!-- /wp:group --></div></div>
<!-- /wp:group -->

<!-- wp:paragraph -->
<p>F). Now write down the code as shown in snippet for while loop. All the logics to automate brightness and ON/OFF of the lights are written inside the while loop. </p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":15339,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/Screenshot-163.png" alt="" class="wp-image-15339"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":15340,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/Screenshot-170.png" alt="" class="wp-image-15340"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Step-4.- Go to the shell and run the program using the command 'python3 main.py'.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The output in my case is as follows:-</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":15341,"width":462,"height":481,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/Screenshot-171.png" alt="" class="wp-image-15341" width="462" height="481"/></figure>
<!-- /wp:image -->

<!-- wp:image {"id":15342,"width":475,"height":432,"sizeSlug":"large"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/06/Screenshot-172.png" alt="" class="wp-image-15342" width="475" height="432"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Conclusion</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In this project ,I managed to control the LEDs brightness and their ON/OFF time using Anomaly Detection on the basis of Z-Score calculation Method. I managed to get the desired result that can be seen from the output snippet above. Thus, this can be used as a model to automate brightness &amp; ON/OFF  a street lights which can save electricity to a extent and can even make our day to day life somewhat easy. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->
