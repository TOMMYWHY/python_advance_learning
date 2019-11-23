let book = {
    name: 'nonviolent communication',
    number: 2,
    id: 1
}

axios.interceptors.response.use(function (response) {
    console.log(response.config);

    let { method, url, data } = response.config
    if (url === '/books/1' && method === 'get') {
        response.data = book
    }
    return response
}, function (error) {
    console.log(error);
})

console.log(axios);


axios.get('/books/1').then(({ data }) => {
    let orgHtml = $('#app').html()
    let newHtml = orgHtml.replace('__name__', data.name)
    newHtml = orgHtml.replace('__number__', data.number)
    $('#app').html(newHtml)
})

$('#app').on('click','#add', function () {
    let orgNumber = $('#number').text();
    let newNumber = orgNumber - 0 + 1
    $('#number').text(newNumber);
})

$('#app').on('click','#minus', function () {
    let orgNumber = $('#number').text();
    let newNumber = orgNumber - 0 - 1
    $('#number').text(newNumber);
})

$('#app').on('click','#reset', function () {
    $('#number').text(0);
})

