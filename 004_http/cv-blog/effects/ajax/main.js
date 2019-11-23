window.jQuery = function (nodeOrSelector) {
    let nodes = {}
    nodes.addClass = function () {

    }
    return nodes;
}

window.jQuery.ajax = function ({url,method,body,successFn,failFn}) {
  /*  let url = options.url;
    let method = options.method;
    let body =options.body;
    let successFn = options.successFn;
    let failFn= options.failFn;*/

    // let {url,method,body,successFn,failFn} = options


    let request = new XMLHttpRequest();
    request.open(method,url)
    request.onreadystatechange  = ()=>{
        if(request.readyState === 4){
            if(request.status >=200 && request.status<300){
                successFn.call(undefined,request.responseText)
            }else if(request.status >=400){
                failFn.call(undefined,request)
            }
        }
    }
    request.send(body)

}

window.$ = window.jQuery;




myButton.addEventListener('click',function (e) {
    window.jQuery.ajax({
        url: '/xxx',
        method: 'Post',
        params: 'a=1&b=2',
        successFn: (x) => {
            console.log(x)
        },
        failFn: () => {
        }
    })
})



