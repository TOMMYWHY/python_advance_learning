window.Controller = function (options) {
    let init = options.init
    // let bindEvents = options.bindEvents

    let object = {
        view: null,
        model: null,
        init: function (view, model) {
            this.view = view
            this.model = model
            this.model.init()
            init.call(this, view, model)
            this.bindEvents.call(this)
            // this.bindEvents()
        },
    }
    console.log(object);
    console.log(options);

    for (const key in options) {
        if (key !== 'init') {
            object[key] = options[key];
        }
    }
    console.log(object);
    return object;



}
