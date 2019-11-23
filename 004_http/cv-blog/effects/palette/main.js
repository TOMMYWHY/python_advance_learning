// document.body.ontouchstart = function (e) {
//     e.preventDefault()
// }

var main = document.getElementById('main');
var context = main.getContext('2d')
autoSetCanvas(main);

listenToUser(main);

var eraserEnabled = false;
eraser.onclick = function (e) {
    eraserEnabled = true;
    eraser.classList.add('active')
    pen.classList.remove('active')
}
pen.onclick = function (e) {
    eraserEnabled = false;
    pen.classList.add('active')
    eraser.classList.remove('active')

}

red.onclick = function (e) {
    context.strokeStyle = 'red'
    red.classList.add('active')
    green.classList.remove('active')
    blue.classList.remove('active')
}
green.onclick = function (e) {
    context.strokeStyle = 'green'
    red.classList.remove('active')
    green.classList.add('active')
    blue.classList.remove('active')
}
blue.onclick = function (e) {
    context.strokeStyle = 'blue'
    red.classList.remove('active')
    green.classList.remove('active')
    blue.classList.add('active')
}


var lineWidth = 5;
thin.onclick = function (e) {
    lineWidth = 5
    thin.classList.add('active')
    thick.classList.remove('active')
}
thick.onclick = function (e) {
    lineWidth = 10
    thin.classList.remove('active')
    thick.classList.add('active')
}
clear.onclick = function (e) {
    context.clearRect(0,0,main.width,main.height)
}
download.onclick = function (e) {
    var url = main.toDataURL('image/png')
    var  a = document.createElement('a')
    document.body.appendChild(a)
    a.href = url;
    a.download = 'myCanvas'
    a.target = '_blank'
    a.click()
}
/*==============*/
function listenToUser(canvas) {

    var penDown = false;
    var lastPoint = {x:undefined,y:undefined}
    if(document.body.ontouchstart !== undefined){
        canvas.ontouchstart = function (e) {

            var x = e.touches[0].clientX;
            var y = e.touches[0].clientY;
            penDown = true;
            if(!eraserEnabled){
                lastPoint = {x:x, y:y}
            }else {
                context.clearRect(x-5,y-5,10,10)
            }
        }
        canvas.ontouchmove = function (e) {
            var x = e.touches[0].clientX;
            var y = e.touches[0].clientY;
            var newPoint = {x:x,y:y};
            if(!penDown){return}
            if(eraserEnabled){
                context.clearRect(x-5,y-5,10,10)
            }else{
                drawLine(lastPoint.x,lastPoint.y,newPoint.x,newPoint.y)
            }
            lastPoint = newPoint //新旧交换
        }
        canvas.ontouchend = function (e) {
            penDown = false
        }
    }else {
        canvas.onmousedown =function (e) {
            var x = e.clientX;
            var y = e.clientY;
            penDown = true;
            if(!eraserEnabled){
                lastPoint = {x:x, y:y}
            }else {
                context.clearRect(x-5,y-5,10,10)
            }
        }
        canvas.onmousemove = function (e) {
            var x = e.clientX;
            var y = e.clientY;
//                var newPoint = {x:x,y:y};
            if(!penDown){return}
            if(eraserEnabled){
                context.clearRect(x-5,y-5,10,10)
            }else{
                var newPoint = {x:x,y:y};
                drawLine(lastPoint.x,lastPoint.y,newPoint.x,newPoint.y)
                lastPoint = newPoint //新旧交换
            }
//                lastPoint = newPoint //新旧交换
        }
        canvas.onmouseup  =function (e) {
            penDown = false
        }
    }


}
function drawLine(startX,startY,endX,endY) {
    context.beginPath();
    context.moveTo(startX,startY)
    context.lineWidth =lineWidth;
    context.lineTo(endX,endY)
    context.stroke()
//        context.closePath()
}
function autoSetCanvas(canvas) {
    setCanvasSize();

    window.onresize = function () {
        setCanvasSize();
    }

    function setCanvasSize() {
        var pageWidth = document.documentElement.clientWidth;
        var pageHeight = document.documentElement.clientHeight;
        canvas.width = pageWidth;
        canvas.height = pageHeight;
    }
}

/*    function drawCircle(x,y,radius) {
        context.beginPath()
        context.arc(x,y,radius,0,Math.PI*2)
        context.stroke()
    }*/

