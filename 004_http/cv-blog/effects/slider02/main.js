
let $buttons = $('#buttonWrapper>button');
let $slides = $('#images')
let $images = $slides.children('img')
let current = 0;

makeFakeSlides($images,$slides)

$slides.hide().offset()
$slides.css({transform:'translateX(-400px)'}).show()

bindEvents()


$('#next').on('click',function () {
    goToSlide(current +1)
})
$('#previous').on('click',function () {
    goToSlide(current -1)
})
let timer = setInterval(function () {
    goToSlide(current +1)
},3000)
$('.container').on('mouseenter',function () {
    window.clearInterval(timer)
}).on('mouseleave',function () {
    timer = setInterval(function () {
        goToSlide(current +1)
    },3000)
})


function makeFakeSlides($images,$slides) {
    let $firstCopy = $images.eq(0).clone(true)
    let $lastCopy = $images.eq($images.length-1).clone(true)
    $slides.append($firstCopy)
    $slides.prepend($lastCopy)
}
function goToSlide(index) {
    if(index > $buttons.length-1){
        index = 0
    }else if(index < 0) {
        index = $buttons.length -1;
    }
    if(current === $buttons.length-1 && index ===0){
        $slides.css({transform:`translateX(-${($buttons.length+1)*400}px)`}).one('transitionend',function () {
            $slides.hide().offset()
            $slides.css({transform:`translateX(-${(index+1)*400}px)` }).show();
        })
    }else if(current ===0  && index===$buttons.length-1){
        console.log(3)
        $slides.css({transform:`translateX(0)`}).one('transitionend',function () {
            $slides.hide().offset()
            $slides.css({transform:`translateX(-${(index+1)*400}px)` }).show();
        })
    }else {
        $slides.css({transform:`translateX(-${(index+1)*400}px)` })
    }
    current = index
}

function bindEvents() {

    //事件委托
     $('#buttonWrapper').on('click','button',function (e) {
         let $button = $(e.currentTarget)
         let index = $button.index()
         goToSlide(index)
    })
    /*$buttons.eq(0).on('click',function (e) {
        console.log(current)
        if(current == 2){
            $slides.css({
                transform:'translateX(-1600px)'
            }).one('transitionend',function () {
                $slides.hide().offset()
                $slides.css({transform:'translateX(-400px)' }).show();
            })
        }else{
            $slides.css({
                transform:'translateX(-400px)'
            })
            current = 0;
        }
    })

    $buttons.eq(1).on('click',function (e) {
        console.log(current)
        $slides.css({
            transform:'translateX(-800px)'
        })
        current = 1;

    })

    $buttons.eq(2).on('click',function (e) {
        console.log(current)
        if(current == 0){
            $slides.css({
                transform:'translateX(0)'
            }).one('transitionend',function () {
                $slides.hide().offset()
                $slides.css({transform:'translateX(-1200px)' }).show();
            })
        }
        $slides.css({
            transform:'translateX(-1200px)'
        })
        current = 2;

    })*/
}




/*
let n;
init();
let timer = setInterval(()=>{
    makeLeave(getImage(n))
        .one('transitionend',(e)=>{
            makeEnter($(e.currentTarget))
    })
    makeCurrent(getImage(n+1));
    n+=1
},3000)

document.addEventListener('visibilitychange',function (e) {
    console.log(document.hidden)
    if(document.hidden){
         window.clearInterval(timer)
        console.log('stop')
    }else {
        timer = setInterval(()=>{
            makeLeave(getImage(n))
                .one('transitionend',(e)=>{
                    makeEnter($(e.currentTarget))
                })
            makeCurrent(getImage(n+1));
            n+=1
        },3000)
        console.log('start')
    }
})


function init() {
    n = 1;
    $(`.images > img:nth-child(${n})`).addClass('current').siblings().addClass('enter')
}
function x(n) {
    if(n>3){
        n = n%3
        if(n===0)
            n = 3
    }
    return n
}

function getImage(n) {
    return $( `.images > img:nth-child(${x(n)})`)
}

function makeCurrent($node) {
    $node.addClass('current ').removeClass('enter leave')
}
function makeLeave($node) {
    $node.addClass('leave').removeClass('current enter')
    return $node;
}
function makeEnter($node) {
    $node.addClass('enter').removeClass('current leave')
}
*/

/*setTimeout(()=>{
    $('.images > img:nth-child(1)').addClass('leave').removeClass('current').one('transitionend',(e)=>{
        $(e.currentTarget).removeClass('leave').addClass('enter')
    })
    $('.images > img:nth-child(2)').addClass('current').removeClass('enter')
    // $('.images > img:nth-child(3)').addClass('enter')

},1000)

setTimeout(()=>{
    $('.images > img:nth-child(2)').addClass('leave').removeClass('current').one('transitionend',(e)=>{
        $(e.currentTarget).removeClass('leave').addClass('enter')
    })
    $('.images > img:nth-child(3)').addClass('current').removeClass('enter')
    // $('.images > img:nth-child(3)').addClass('enter')

},3000)

setTimeout(()=>{
    $('.images > img:nth-child(3)').addClass('leave').removeClass('current').one('transitionend',(e)=>{
        $(e.currentTarget).removeClass('leave').addClass('enter')
    })
    $('.images > img:nth-child(1)').addClass('current').removeClass('enter')
    // $('.images > img:nth-child(3)').addClass('enter')

},6000)*/

/*
setTimeout(function () {
    $('.images>img:nth-child(1)').css({
        transform:'translateX(-100%)'
    })

    $('.images>img:nth-child(2)').css({
        transform:'translateX(-100%)'
    })
    $('.images>img:nth-child(1)').one('transitionend',function (e) {
        console.log(1)
        $(e.currentTarget).addClass('right').css({transform:'none'})
    })
},3000)

setTimeout(function () {
    $('.images>img:nth-child(2)').css({
        transform:'translateX(-200%)'
    })

    $('.images>img:nth-child(3)').css({
        transform:'translateX(-100%)'
    })
    $('.images>img:nth-child(2)').one('transitionend',function (e) {
        console.log(1)
        $(e.currentTarget).addClass('right').css({transform:'none'})
    })
},6000)

setTimeout(function () {
    $('.images>img:nth-child(3)').css({
        transform:'translateX(-200%)'
    })

    $('.images>img:nth-child(1)').css({
        transform:'translateX(-100%)'
    })
    $('.images>img:nth-child(3)').one('transitionend',function (e) {
        console.log(1)
        $(e.currentTarget).addClass('right').css({transform:'none'})
    })
},9000)*/
