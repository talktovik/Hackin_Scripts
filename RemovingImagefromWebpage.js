//#1
var images = document.getElementsByTagName('img');
var l = images.length;
for (var i = 0; i < l; i++) {
    images[0].parentNode.removeChild(images[0]);
}

//#2
for (var i= document.images.length; i-->0;)
    document.images[i].parentNode.removeChild(document.images[i]);
