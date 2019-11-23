let img = $('#img')
let Rotate = 0;
let invert = false;
$('#obtn').on('click',function (e) {
    Rotate = 0
    img.css('-webkit-transform',`rotate(${Rotate}deg)`)
})
$('#xbtn').on('click',function (e) {
    Rotate = Rotate + 90
    img.css('-webkit-transform',`rotate(${Rotate}deg)`)
})

$('#ybtn').on('click',function (e) {
    Rotate = Rotate - 90
    img.css('-webkit-transform',`rotate(${Rotate}deg)`)
})


$('#invertColor').on('click',function (e) {
    invert = ! invert
    img.css('filter',`invert(${invert?100:0}%)`)
})

$('.container').on('mousemove',function (e) {
    let xx = e.clientX;
    let yy = e.clientY;
    xInput.value = xx;
    yInput.value = yy;



var img = document.getElementById('img');
var canvas = document.createElement('canvas');
canvas.width = img.width;
canvas.height = img.height;
canvas.getContext('2d').drawImage(img, 0, 0, img.width, img.height);
var pixelData = canvas.getContext('2d').getImageData(event.offsetX, event.offsetY, 1, 1).data;
console.log(pixelData);
rInput.value = pixelData[0]
gInput.value = pixelData[1]
bInput.value = pixelData[2]
aInput.value = pixelData[3]

})
