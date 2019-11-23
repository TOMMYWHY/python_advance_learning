!function () {
    let view = document.querySelector('nav.menu')
    let controller = {
        view: null,
        aTags: null,
        init: function (view) {
            this.view = view
            this.initAnimation()
            this.bindEvents();
        },
        initAnimation: function () {
            /*tween.js*/
            // Setup the animation loop.
            function animate(time) {
                requestAnimationFrame(animate);
                TWEEN.update(time);
            }
            requestAnimationFrame(animate);
        },
        scrollToElement: function (element) {

            let top = element.offsetTop;
            let targetTop = top - 80;
            let currentTop = window.scrollY;
            let s = targetTop - currentTop //向上滑动 s 为负值
            let t = Math.abs((s / 100) * 300); // 时间不能是负数，所以取绝对值
            if (t > 500) {
                t = 500
            }
            const coords = { x: 0, y: currentTop };

            const tween = new TWEEN.Tween(coords)
                .to({ x: 0, y: targetTop }, t)
                .easing(TWEEN.Easing.Quadratic.InOut)
                .onUpdate(() => {
                    //                        box.style.setProperty('transform', `translate(${coords.x}px, ${coords.y}px)`);
                    window.scrollTo(0, coords.y)
                })
                .start();
        },
        bindEvents: function () {
            let aTags = this.view.querySelectorAll(' nav.menu > ul > li > a')

            for (let i = 0; i < aTags.length; i++) {
                aTags[i].onclick = (e) => {
                    //                e.preventDefault()
                    /*======================*/
                    // console.log(e.currentTarget.getAttribute('href')) //打印 锚点
                    let href = e.currentTarget.getAttribute('href')
                    let element = document.querySelector(href)
                    this.scrollToElement(element);
                }
            }
        },
    }



    controller.init(view)


}.call()

