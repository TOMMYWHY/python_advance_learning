!function () {
    let view = View('#topNavBar')
    // let view = document.querySelector('#topNavBar')
    let controller = {
        view: null,
        init: function (view) {
            this.view = view  //this === controller
            this.bindEvents()
            // this.bindEvents.call(this)
        },
        bindEvents: function () {
            // let view = this.view // this === this.bindEvents.call(this)
            window.addEventListener('scroll',  (e)=> {
                if (window.scrollY > 0) { 
                    this.active()// 上面 view 的 this 是同一个
                } else {
                    this.deactive()
                }
            })
        },
        active: function () {
            this.view.classList.add('sticky')
        },
        deactive: function () {
            this.view.classList.remove('sticky')
        }
    }

    controller.init.call(controller, view)
}.call()

