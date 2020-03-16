## CS 1XA3 Project02 - mooret12

This web page is a personal CV for myself. I used a resume template that can be found [here](https://startbootstrap.com/themes/resume/).  The languages used are JavaScript, HTML and CSS


### **Custom JavaScript Code**  #1

```javascript
$('#theme_1').click(function () {

if ($("link[id='styles']").attr('href') == 'css/theme2.css'){

$("link[id='styles']").attr('href', 'css/resume.css');

} else {

$("link[id='styles']").attr('href', 'css/theme2.css');

}

});
```
I used this code to alternate color themes. Once the button with the
id "theme_1" is clicked, the webpage changes its color theme; in this case it changes to a color theme from the "theme2.css" file and will switch back to the original color theme when clicked again.



### **Custom JavaScript Code**  #2

```javascript
function  showhide() {

var  div = document.getElementById("themes");

div.classList.toggle('hidden');

toggle();

}

 
function  toggle() {

var  change = document.getElementById("1");

if (change.innerHTML == "Open")

{

change.innerHTML = "Toggle";

}

else {

change.innerHTML = "Open";

}
}
```

```javascript 
function showhide(); 
```
This Function hid a div containing the buttons to switch themes, and when you clicked the button associated with this function it would "open" and display the div containing the theme buttons. 

It can be toggled back and forth so you can open and close the theme page, I did this to try and clean up the design and hide the themes if you wanted to.

```javascript
function  toggle()
``` 
This function just changed the text of the button that the showhide function used.

### References 

 I used and altered code from these  stackoverflow links:
 [Link 1](https://stackoverflow.com/questions/47655563/hide-and-show-text-by-click-on-div), [Link 2](https://stackoverflow.com/questions/60698485/toggle-text-of-a-button-when-clicked)(https://stackoverflow.com/questions/60698485/toggle-text-of-a-button-when-clicked), [Link 3](https://stackoverflow.com/questions/16025138/call-two-functions-from-same-onclick).
 Resume template from [startbootstrap](https://startbootstrap.com/themes/resume/).
