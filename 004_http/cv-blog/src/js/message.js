
!function () {
    let view = View('section.message')
    // let view = document.querySelector('section.message');

    let model = Model({ resourceName: 'Message' })

    let controller = Controller({
        init: function (view, controller) {
            this.messageList = document.querySelector('#messageList')
            this.form = document.querySelector('#postMessageForm')
            this.loadMessages()
        },
        loadMessages: function () {
            this.model.fetch().then((messages) => {
                let array = messages.map((item) => { return item.attributes })
                array.forEach((item) => {
                    let li = document.createElement('li');
                    li.innerText = `${item.username}: ${item.content} `;
                    this.messageList.prepend(li)
                })
            },
                (err) => { alert('submit fail~! please try again...') })
        },
        bindEvents: function () {
            this.form.addEventListener('submit', (e) => {
                e.preventDefault()
                this.saveMessage()
            })
        },
        saveMessage: function () {
            let myForm = this.form
            let username = myForm.querySelector('input[name=username]').value;
            let phone = myForm.querySelector('input[name=phone]').value;
            let email = myForm.querySelector('input[name=email]').value;
            let content = myForm.querySelector('input[name = content]').value;
            this.model.save({
                'username': username,
                'phone': phone,
                'email': email,
                'content': content
            }).then(function (obj) {
                console.log('save successful~!')
                // window.location.reload()
                let li = document.createElement('li');
                li.innerText = `${obj.attributes.username}: ${obj.attributes.content} `;
                let messageList = document.querySelector('#messageList');
                messageList.prepend(li)
                // this.myForm.querySelector('input[name=username]').value ='';
                // this.myForm.querySelector('input[name=phone]').value ='';
                // this.myForm.querySelector('input[name=email]').value ='';
                myForm.querySelector('input[name = content]').value = '';
            })
        }
    })



    controller.init(view, model)









}.call();


